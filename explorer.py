"""
DB Explorer — visual overview of how knowledge is stored in LanceDB.

Tabs:
  1. Embedding Space  — 2D PCA projection of all 1310 chunk vectors
  2. Distributions    — bar/pie charts for category, section type, contact team, status
  3. Feature Map      — per-feature chunk breakdown (what sections each feature has)
  4. Browse Chunks    — searchable table of raw DB rows
"""

import json
import lancedb
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder

DB_PATH = "lancedb_store"
TABLE_NAME = "knowledge"

st.set_page_config(
    page_title="Vector Data Visualization Dashboard",
    page_icon="🗄️",
    layout="wide",
)
st.title("🗄️ Vector Data Visualization Dashboard")
st.caption("1310 chunks · 100 features · 7 section types · sentence-transformers/all-MiniLM-L6-v2 (384-dim)")

# ── Load data ─────────────────────────────────────────────────────────────────
@st.cache_data(show_spinner="Loading all rows from LanceDB...")
def load_data():
    db = lancedb.connect(DB_PATH)
    t = db.open_table(TABLE_NAME)
    rows = t.search([0.0] * 384).limit(2000).to_list()
    return rows

rows = load_data()

# Build flat lists for easy charting
vectors      = np.array([r["vector"] for r in rows], dtype=np.float32)
feature_names = [r["feature_name"]  for r in rows]
section_types = [r["section_type"]  for r in rows]
categories    = [r["category"]      for r in rows]
contact_teams = [r["contact_team"]  for r in rows]
statuses      = [r["status"]        for r in rows]
chunk_texts   = [r["chunk_text"]    for r in rows]
chunk_ids     = [r["chunk_id"]      for r in rows]
source_files  = [r["source_file"]   for r in rows]
tags_raw      = [json.loads(r["tags"]) for r in rows]
tags_flat     = [", ".join(t[:4]) for t in tags_raw]  # first 4 tags for display

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🧭 Embedding Space",
    "📊 Distributions",
    "🗺️ Feature Map",
    "🔍 Browse Chunks",
    "🔄 Sync",
])

# ─────────────────────────────────────────────────────────────────────────────
# TAB 1 — Embedding Space (2D PCA projection)
# ─────────────────────────────────────────────────────────────────────────────
with tab1:
    st.subheader("2D PCA projection of all 1310 chunk embeddings")
    st.caption(
        "Each dot = one chunk stored in LanceDB. PCA reduces 384 dimensions → 2. "
        "Nearby dots have similar semantic meaning."
    )

    color_by = st.selectbox(
        "Color dots by",
        ["category", "section_type", "contact_team", "status"],
        key="emb_color",
    )

    @st.cache_data(show_spinner="Computing PCA (one-time)...")
    def compute_pca(vecs):
        pca = PCA(n_components=2, random_state=42)
        return pca.fit_transform(vecs)

    coords = compute_pca(vectors)

    color_map = {
        "category": categories,
        "section_type": section_types,
        "contact_team": contact_teams,
        "status": statuses,
    }[color_by]

    # Truncate chunk text for hover tooltip
    hover_text = [f"<b>{fn}</b><br>{st_}<br>{ct[:80]}..." for fn, st_, ct in zip(feature_names, section_types, chunk_texts)]

    fig = px.scatter(
        x=coords[:, 0],
        y=coords[:, 1],
        color=color_map,
        hover_name=feature_names,
        hover_data={
            "section": section_types,
            "category": categories,
            "contact": contact_teams,
            "status": statuses,
            "tags": tags_flat,
        },
        labels={"x": "PC1", "y": "PC2", "color": color_by},
        title=f"Embedding Space — colored by {color_by}",
        height=600,
        opacity=0.75,
    )
    fig.update_traces(marker=dict(size=6))
    fig.update_layout(legend=dict(itemsizing="constant"))
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total chunks", len(rows))
    with col2:
        st.metric("Total features", len(set(feature_names)))

# ─────────────────────────────────────────────────────────────────────────────
# TAB 2 — Distributions
# ─────────────────────────────────────────────────────────────────────────────
with tab2:
    st.subheader("How chunks are distributed across metadata dimensions")

    from collections import Counter

    col1, col2 = st.columns(2)

    with col1:
        # Category breakdown
        cat_counts = Counter(categories)
        fig_cat = px.bar(
            x=list(cat_counts.values()),
            y=list(cat_counts.keys()),
            orientation="h",
            title="Chunks by Category",
            labels={"x": "Count", "y": ""},
            color=list(cat_counts.keys()),
            color_discrete_sequence=px.colors.qualitative.Pastel,
            height=500,
        )
        fig_cat.update_layout(showlegend=False)
        st.plotly_chart(fig_cat, use_container_width=True)

    with col2:
        # Section type breakdown
        sec_counts = Counter(section_types)
        fig_sec = px.pie(
            names=list(sec_counts.keys()),
            values=list(sec_counts.values()),
            title="Chunks by Section Type",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set2,
            height=500,
        )
        st.plotly_chart(fig_sec, use_container_width=True)

    col3, col4 = st.columns(2)

    with col3:
        # Contact team
        team_counts = Counter(contact_teams)
        fig_team = px.pie(
            names=list(team_counts.keys()),
            values=list(team_counts.values()),
            title="Chunks by Contact Team",
            hole=0.4,
            color_discrete_sequence=["#2ecc71", "#3498db"],
            height=400,
        )
        st.plotly_chart(fig_team, use_container_width=True)

    with col4:
        # Status
        status_counts = Counter(statuses)
        fig_status = px.bar(
            x=list(status_counts.keys()),
            y=list(status_counts.values()),
            title="Chunks by Status",
            labels={"x": "Status", "y": "Count"},
            color=list(status_counts.keys()),
            color_discrete_map={"live": "#2ecc71", "in-development": "#e74c3c"},
            height=400,
        )
        fig_status.update_layout(showlegend=False)
        st.plotly_chart(fig_status, use_container_width=True)

# ─────────────────────────────────────────────────────────────────────────────
# TAB 3 — Feature Map (heatmap: feature × section_type)
# ─────────────────────────────────────────────────────────────────────────────
with tab3:
    st.subheader("Which sections are stored per feature")
    st.caption("Each cell = number of chunks stored for that feature × section combination.")

    from collections import defaultdict

    all_sections = sorted(set(section_types))
    all_features = sorted(set(feature_names))

    # Build matrix
    matrix = defaultdict(lambda: defaultdict(int))
    for fn, st_ in zip(feature_names, section_types):
        matrix[fn][st_] += 1

    z = [[matrix[fn][sec] for sec in all_sections] for fn in all_features]

    fig_heat = go.Figure(data=go.Heatmap(
        z=z,
        x=all_sections,
        y=all_features,
        colorscale="Blues",
        hoverongaps=False,
        hovertemplate="Feature: %{y}<br>Section: %{x}<br>Chunks: %{z}<extra></extra>",
    ))
    fig_heat.update_layout(
        title="Feature × Section Chunk Count",
        xaxis_title="Section Type",
        yaxis_title="Feature",
        height=max(500, len(all_features) * 14),
        margin=dict(l=280),
        yaxis=dict(tickfont=dict(size=10)),
    )
    st.plotly_chart(fig_heat, use_container_width=True)

# ─────────────────────────────────────────────────────────────────────────────
# TAB 4 — Browse raw chunks
# ─────────────────────────────────────────────────────────────────────────────
with tab4:
    st.subheader("Browse raw chunks stored in LanceDB")

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        filter_category = st.selectbox("Filter by category", ["All"] + sorted(set(categories)))
    with col_b:
        filter_section = st.selectbox("Filter by section type", ["All"] + sorted(set(section_types)))
    with col_c:
        filter_status = st.selectbox("Filter by status", ["All", "live", "in-development"])

    filtered = [
        r for r in rows
        if (filter_category == "All" or r["category"] == filter_category)
        and (filter_section == "All" or r["section_type"] == filter_section)
        and (filter_status == "All" or r["status"] == filter_status)
    ]

    st.markdown(f"**{len(filtered)} chunks** match the filters.")

    for r in filtered[:50]:  # cap at 50 to keep UI fast
        badge = "🟢" if r["status"] == "live" else "🔴"
        with st.expander(f"{badge} **{r['feature_name']}** — {r['section_type']}  |  `{r['chunk_id']}`"):
            col1, col2, col3 = st.columns(3)
            col1.markdown(f"**Category**  \n{r['category']}")
            col2.markdown(f"**Contact**  \n{r['contact_team']}")
            col3.markdown(f"**Status**  \n{r['status']}")
            st.divider()
            st.markdown(r["chunk_text"])
            with st.popover("Show vector (first 16 dims)"):
                st.code(str(np.round(r["vector"][:16], 4).tolist()))

    if len(filtered) > 50:
        st.info(f"Showing 50 of {len(filtered)} results. Use filters to narrow down.")

# ─────────────────────────────────────────────────────────────────────────────
# TAB 5 — Sync
# ─────────────────────────────────────────────────────────────────────────────
with tab5:
    st.subheader("Sync knowledge base with .md files")
    st.caption(
        "Hard sync drops and rebuilds the entire DB. "
        "Soft sync only re-embeds files that changed since the last sync."
    )

    from sync import hard_sync, soft_sync, get_sync_status

    # ── Status panel ─────────────────────────────────────────────────────────
    status = get_sync_status()
    s_col1, s_col2, s_col3, s_col4 = st.columns(4)
    s_col1.metric("Last sync", status["last_sync"].split("T")[0] if status["last_sync"] else "Never")
    s_col2.metric("Tracked files", status["tracked_files"])
    s_col3.metric("Files on disk", status["disk_files"])
    s_col4.metric("Pending changes", status["pending_changes"])

    if status["pending_changes"]:
        d = status["detail"]
        with st.expander("Show pending changes", expanded=True):
            if d["new"]:
                st.markdown("**New files:**")
                for f in d["new"]: st.markdown(f"  - `{f}`")
            if d["modified"]:
                st.markdown("**Modified files:**")
                for f in d["modified"]: st.markdown(f"  - `{f}`")
            if d["deleted"]:
                st.markdown("**Deleted files:**")
                for f in d["deleted"]: st.markdown(f"  - `{f}`")
    else:
        st.success("All files are in sync.")

    st.divider()

    # ── Sync buttons ──────────────────────────────────────────────────────────
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 🔴 Hard Sync")
        st.markdown("Drops and rebuilds the **entire** DB from all `.md` files. Always safe, always correct.")
        if st.button("Run Hard Sync", type="primary", key="hard_sync_btn"):
            with st.spinner("Rebuilding entire knowledge DB — this takes ~30 seconds..."):
                hard_sync()
                st.cache_data.clear()
            st.success("Hard sync complete. Refresh the page to see updated stats.")

    with col2:
        st.markdown("#### 🟡 Soft Sync")
        st.markdown("Re-embeds **only** new, modified, or deleted files. Fast for small changes.")
        if st.button("Run Soft Sync", key="soft_sync_btn"):
            with st.spinner("Scanning for changes..."):
                result = soft_sync()
                st.cache_data.clear()
            st.success(
                f"Soft sync complete: "
                f"**{result['new']}** new · "
                f"**{result['modified']}** modified · "
                f"**{result['deleted']}** deleted · "
                f"**{result['unchanged']}** unchanged."
            )
