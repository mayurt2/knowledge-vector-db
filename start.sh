#!/usr/bin/env bash

# Activate venv if present
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
fi

echo "Starting Feature Knowledge Retrieval Data    → http://localhost:8501"
echo "Starting Vector Data Visualization Dashboard → http://localhost:8502"
echo ""
echo "Press Ctrl+C to stop both apps."
echo ""

python3 -m streamlit run app.py --server.port 8501 &
PID1=$!

python3 -m streamlit run explorer.py --server.port 8502 &
PID2=$!

# Trap Ctrl+C and kill both
trap "kill $PID1 $PID2 2>/dev/null; exit 0" INT TERM

wait
