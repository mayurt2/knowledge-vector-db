from lancedb.pydantic import LanceModel, Vector


class KnowledgeChunk(LanceModel):
    chunk_id: str           # "{feature_id}__{section_slug}"
    feature_id: str         # from frontmatter
    feature_name: str       # from frontmatter
    category: str           # from frontmatter — usable as scalar filter
    config_source: str      # from frontmatter
    configurable: bool      # from frontmatter
    status: str             # "live" | "in-development"
    contact_team: str       # "Onboarding Team" | "Tech Team"
    tags: str               # JSON-encoded list
    related_services: str   # JSON-encoded list
    technical_keys: str     # JSON-encoded list
    source_file: str        # "feature-name.md"
    section_heading: str    # original H2 heading text
    section_type: str       # summary | customer_experience | configurability |
                            # contact_team | related_settings | technical_reference | sample_question
    chunk_text: str         # searchable content
    vector: Vector(384)     # sentence-transformers/all-MiniLM-L6-v2 output dim
