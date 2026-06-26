#!/usr/bin/env bash
set -e

echo "=== knowledge-vector-db setup ==="

# Python 3.9+ required
python3 --version

echo ""
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo ""
echo "Installing dependencies..."
pip install -q --upgrade pip
pip install -r requirements.txt

echo ""
if ls knowledge_files/*.md 1>/dev/null 2>&1; then
    echo "Running initial full ingest..."
    python3 ingest.py
else
    echo "No .md files found in knowledge_files/"
    echo "Add your .md files there, then run: python3 ingest.py"
fi

echo ""
echo "=== Setup complete ==="
echo "Start the apps with: bash start.sh"
echo "  Feature Knowledge Retrieval Data    → http://localhost:8501"
echo "  Vector Data Visualization Dashboard → http://localhost:8502"
