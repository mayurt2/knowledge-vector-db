import streamlit as st
from search import search, load_model, load_table

st.set_page_config(page_title="Feature Knowledge Retrieval Data", page_icon="🔍", layout="centered")

st.title("🔍 Feature Knowledge Retrieval Data")
st.caption("Returns raw knowledge chunks from the vector DB — no LLM processing.")


# Model is expensive to load — cache it for the lifetime of the process.
@st.cache_resource(show_spinner="Loading embedding model...")
def get_model():
    return load_model()


# Table is NOT cached — it's cheap to reopen and must always reflect the
# latest DB state (hard/soft sync drops and recreates the table).
def get_table():
    return load_table()


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("Search settings")
    top_k = st.slider("Results to return", 1, 10, 5)
    threshold = st.slider(
        "Relevance threshold",
        min_value=0.0, max_value=1.0, value=0.3, step=0.05,
        help="Minimum cosine similarity (0–1). Below this → 'not found'.",
    )
    include_dev = st.checkbox("Include in-development features", value=True)
    use_fts = st.checkbox("Keyword/exact-key mode", value=False,
                          help="Enable for exact technical key lookups e.g. `noOfApprovers`")


def render_results(results, threshold):
    if not results:
        st.error(
            "**No relevant information found in the knowledge base.**\n\n"
            f"No chunks scored above threshold `{threshold}`. "
            "This topic may not be covered in the current feature documentation."
        )
        return

    for r in results:
        badge = "🟢 live" if r["status"] == "live" else "🔴 in-development"
        with st.expander(
            f"{badge}  **{r['feature_name']}** — {r['section_heading']}  `score: {r['score']}`",
            expanded=True,
        ):
            st.markdown(
                f"**Category:** {r['category']}  \n"
                f"**Contact:** {r['contact_team']}  \n"
                f"**Config source:** {r['config_source']}"
            )
            st.divider()
            st.markdown(r["chunk_text"])


# ── Single query — no history ─────────────────────────────────────────────────
if query := st.chat_input("Ask about a feature or functionality..."):
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        with st.spinner("Searching..."):
            results = search(
                query,
                top_k=top_k,
                threshold=threshold,
                status=None if include_dev else "live",
                use_fts=use_fts,
                _model=get_model(),
                _table=get_table(),
            )
        render_results(results, threshold)
