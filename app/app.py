
import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline

# ---- Page setup ----
st.set_page_config(page_title="Anime Recommender", page_icon="🎌", layout="wide")

# ---- Minimal custom CSS (cards, spacing, dark-friendly) ----
# Make the sidebar wider and increase UI sizes
st.markdown("""
<style>
/* Wider sidebar */
section[data-testid="stSidebar"] {width: 360px !important; min-width: 360px !important;}
/* Tighter padding inside the sidebar */
section[data-testid="stSidebar"] .block-container {padding: 1.2rem 1rem !important;}
/* Bigger labels and helper text in the sidebar */
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] .stMarkdown,
section[data-testid="stSidebar"] p {font-size: 1rem !important; line-height: 1.35;}
/* Bigger inputs/buttons in the sidebar */
section[data-testid="stSidebar"] [data-baseweb],
section[data-testid="stSidebar"] input,
section[data-testid="stSidebar"] textarea {font-size: 1rem !important;}
section[data-testid="stSidebar"] button {font-size: 1rem !important; padding: .55rem .8rem;}
/* (Optional) bump main title a bit too */
h1 {font-size: 2.2rem;}
</style>
""", unsafe_allow_html=True)



# ---- Lazy init pipeline (keeps cold start fast) ----
@st.cache_resource(show_spinner=False)
def init_pipeline():
    return AnimeRecommendationPipeline()


# ---- Sidebar ----
# ---- Sidebar ----
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    st.caption("Tune the query to guide the model.")
    genres = st.multiselect(
        "Preferred genres (optional)",
        [
            "Action",
            "Adventure",
            "Comedy",
            "Drama",
            "Fantasy",
            "Horror",
            "Isekai",
            "Mecha",
            "Mystery",
            "Psychological",
            "Romance",
            "Sci-Fi",
            "Seinen",
            "Shounen",
            "Slice of Life",
            "Sports",
            "Supernatural",
        ],
        [],
    )
    tone = st.selectbox(
        "Tone", ["Any", "Epic", "Dark/Serious", "High-energy", "Bittersweet"], index=0
    )
    length = st.selectbox(
        "Episode length",
        ["Any", "Short (<15m)", "Standard (24m)", "Long (45m+)"],
        index=0,
    )
    st.divider()
    st.caption("Try a real prompt:")
    ex1, ex2, ex3 = st.columns(3)
    if ex1.button("⚔️ Epic historical saga like Vinland Saga", use_container_width=True):
        st.session_state.query = "Epic historical anime with deep character arcs and moral dilemmas like Vinland Saga"
    if ex2.button(
        "🎯 Strategic adventure like Hunter x Hunter", use_container_width=True
    ):
        st.session_state.query = "Adventure anime with intricate power systems and clever strategies like Hunter x Hunter"
    if ex3.button("🏴‍☠️ Grand pirate journey like One Piece", use_container_width=True):
        st.session_state.query = "Long-running adventure with found family, emotional moments, and epic battles like One Piece"


# ---- Header ----
st.markdown('<div class="hero-title">Anime Recommender</div>', unsafe_allow_html=True)
st.markdown(
    '<p class="help">Describe what you’re in the mood for and get three curated picks with reasons.</p>',
    unsafe_allow_html=True,
)

# ---- Query input row ----
q_col, btn_col = st.columns([4, 1])
query = q_col.text_input(
    "What are you in the mood for?",
    key="query",
    placeholder="e.g., wholesome slice‑of‑life with strong character growth",
)
search_clicked = btn_col.button("✨ Get Recommendations", use_container_width=True)


# ---- Build a richer prompt from sidebar filters ----
def enrich_query(q: str) -> str:
    parts = [q.strip()] if q else []
    if genres:
        parts.append("Genres: " + ", ".join(genres))
    if tone != "Any":
        parts.append(f"Tone: {tone}")
    if length != "Any":
        parts.append(f"Episode length: {length}")
    return " | ".join(parts)


# ---- History storage ----
if "history" not in st.session_state:
    st.session_state.history = []

# ---- Run recommender ----
if search_clicked and query.strip():
    st.toast("Finding great matches…", icon="🔎")
    with st.spinner("Analyzing your preferences and searching the catalog…"):
        pipeline = init_pipeline()
        final_query = enrich_query(query)
        try:
            result = pipeline.recommend(final_query)
            st.session_state.history.insert(0, {"q": final_query, "r": result})
        except Exception as e:
            st.error(
                "Something went wrong while generating recommendations. Please try again."
            )
            st.stop()

# ---- Results ----
if st.session_state.history:
    latest = st.session_state.history[0]
    st.markdown("### Recommendations")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    # The recommender already returns a nicely formatted list; render as markdown.
    st.markdown(latest["r"])
    st.markdown("</div>", unsafe_allow_html=True)

    # Quick feedback
    fb1, fb2, fb3 = st.columns(3)
    with fb1:
        st.button("👍 Helpful", key="upvote")
    with fb2:
        st.button("🤔 Okay", key="meh")
    with fb3:
        st.button("👎 Not relevant", key="downvote")

# ---- Previous searches ----
with st.expander("Previous searches"):
    if st.session_state.history:
        for i, item in enumerate(st.session_state.history[:6], start=1):
            st.markdown(f"**{i}.** {item['q']}")
    else:
        st.caption("No searches yet.")

# ---- Footer hint ----
st.markdown(
    '<p class="small">Tip: Use the sidebar to steer genre, tone, and length. Results update on **Get Recommendations**.</p>',
    unsafe_allow_html=True,
)
