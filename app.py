import streamlit as st

from rag_pipeline import (
    build_rag_system,
    ask_rag
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Domain-Specific RAG Chatbot",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       GLOBAL
       ======================================================== */

    * {
        box-sizing: border-box;
    }

    html,
    body,
    [data-testid="stAppViewContainer"] {
        overflow-y: auto !important;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 75% 5%,
                rgba(225, 237, 255, 0.75),
                transparent 35%
            ),
            linear-gradient(
                135deg,
                #f8fbff 0%,
                #f4f8fd 50%,
                #eef4fc 100%
            );

        min-height: 100vh;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
    }


    /* ========================================================
       SIDEBAR
       ======================================================== */

    section[data-testid="stSidebar"] {

        background:
            linear-gradient(
                180deg,
                #f6f9ff 0%,
                #eef4fc 100%
            ) !important;

        border-right: 1px solid #d7e2f2;

        min-height: 100vh;
    }


    section[data-testid="stSidebar"] > div {

        padding-top: 10px;
    }


    /* Sidebar title */

    section[data-testid="stSidebar"]
    [data-testid="stMarkdownContainer"] h3 {

        color: #071d43 !important;

        font-size: 18px !important;

        font-weight: 800 !important;

        line-height: 1.2 !important;
    }


    section[data-testid="stSidebar"]
    [data-testid="stMarkdownContainer"] p {

        color: #30486e;

        font-size: 13px;

        line-height: 1.5;
    }


    /* ========================================================
       SIDEBAR BUTTONS
       ======================================================== */

    section[data-testid="stSidebar"]
    .stButton > button {

        width: 100% !important;

        min-height: 40px !important;

        border-radius: 9px !important;

        border: 1px solid #c8d9f2 !important;

        background: white !important;

        color: #071d43 !important;

        font-size: 13px !important;

        font-weight: 700 !important;

        box-shadow: none !important;
    }


    section[data-testid="stSidebar"]
    .stButton > button:hover {

        background: #f7faff !important;

        border-color: #8db2e9 !important;

        color: #071d43 !important;
    }


    /* ========================================================
       SIDEBAR HEADINGS
       ======================================================== */

    .sidebar-heading {

        color: #071d43 !important;

        font-size: 12px !important;

        font-weight: 800 !important;

        margin-top: 20px !important;

        margin-bottom: 10px !important;

        letter-spacing: 0.2px;
    }


    .sidebar-divider {

        height: 1px;

        background: #d6e2f2;

        margin: 18px 0;
    }


    .resource-text {

        color: #29456e;

        font-size: 13px;

        font-weight: 600;

        margin: 8px 0 2px 0;
    }


    .available-text {

        color: #15a66a;

        font-size: 10px;

        font-weight: 700;

        margin-bottom: 12px;
    }


    .pipeline-text {

        color: #334d75;

        font-size: 12.5px;

        margin: 9px 0;
    }


    .session-text {

        color: #29456e;

        font-size: 11.5px;

        font-weight: 700;

        margin-top: 5px;
    }


    .sidebar-note {

        color: #7086a6;

        font-size: 9.5px;

        line-height: 1.5;

        margin-top: 10px;
    }


    /* ========================================================
       MAIN PAGE
       ======================================================== */

    .main-title {

        color: #071d43 !important;

        text-align: center;

        font-size: 38px;

        font-weight: 800;

        line-height: 1.15;

        margin-top: 5px;

        margin-bottom: 7px;

        letter-spacing: -0.5px;
    }


    .ai-label {

        color: #071d43 !important;

        text-align: center;

        font-size: 13px;

        font-weight: 800;

        margin-top: 5px;

        margin-bottom: 7px;
    }


    .main-subtitle {

        color: #526a8d !important;

        text-align: center;

        font-size: 14px;

        font-weight: 500;

        margin-bottom: 22px;
    }


    /* ========================================================
       INFORMATION BOX
       ======================================================== */

    div[data-testid="stAlert"] {

        border-radius: 13px !important;

        border: 1px solid #bfd6f5 !important;

        background:
            linear-gradient(
                100deg,
                #edf6ff,
                #f7faff
            ) !important;

        color: #203d68 !important;
    }


    div[data-testid="stAlert"] p {

        color: #203d68 !important;

        font-size: 12.5px !important;

        line-height: 1.55 !important;
    }


    /* ========================================================
       WELCOME CARD
       ======================================================== */

    .welcome-title {

        color: #071d43 !important;

        text-align: center;

        font-size: 24px;

        font-weight: 800;

        margin-top: 8px;
    }


    .welcome-subtitle {

        color: #607795 !important;

        text-align: center;

        font-size: 13px;

        font-weight: 500;

        margin-top: 4px;

        margin-bottom: 8px;
    }


    .welcome-icon {

        text-align: center;

        font-size: 39px;

        margin-top: 2px;
    }


    /* ========================================================
       TRY ASKING
       ======================================================== */

    .try-title {

        color: #071d43 !important;

        font-size: 14px;

        font-weight: 800;

        margin-top: 10px;

        margin-bottom: 8px;
    }


    /* ========================================================
       SUGGESTED QUESTIONS
       ======================================================== */

    .suggested-question button {

        width: 100% !important;

        min-height: 47px !important;

        border-radius: 9px !important;

        border: 1px solid #c5daf5 !important;

        background: #ffffff !important;

        color: #29466f !important;

        font-size: 12.5px !important;

        font-weight: 500 !important;

        text-align: left !important;

        padding: 7px 14px !important;

        box-shadow: none !important;
    }


    .suggested-question button:hover {

        background: #f7faff !important;

        border-color: #8eb6e9 !important;

        color: #071d43 !important;
    }


    /* ========================================================
       CHATGPT STYLE MESSAGES
       ======================================================== */

    [data-testid="stChatMessage"] {

        padding-top: 8px;

        padding-bottom: 8px;

        margin-top: 4px;

        margin-bottom: 4px;
    }


    [data-testid="stChatMessage"] p {

        color: #263f68 !important;

        font-size: 14px !important;

        line-height: 1.65 !important;
    }


    [data-testid="stChatMessage"] strong {

        color: #071d43 !important;
    }


    /* User message */

    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-user"]
    ) {

        background: transparent !important;
    }


    /* Assistant message */

    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-assistant"]
    ) {

        background: #ffffff !important;

        border: 1px solid #dce5f2 !important;

        border-radius: 14px !important;

        box-shadow:
            0 3px 14px rgba(
                37,
                69,
                112,
                0.04
            );
    }


    /* ========================================================
       RETRIEVED TEXT
       ======================================================== */

    [data-testid="stExpander"] {

        border: 1px solid #dce5f2 !important;

        border-radius: 10px !important;

        background: #f8fbff !important;

        margin-top: 10px !important;
    }


    [data-testid="stExpander"] summary {

        color: #29466f !important;

        font-weight: 700 !important;
    }


    /* ========================================================
       CHAT INPUT
       ======================================================== */

    div[data-testid="stChatInput"] {

        background: transparent !important;
    }


    div[data-testid="stChatInput"] > div {

        background: #ffffff !important;

        border: 1px solid #cbdcf2 !important;

        border-radius: 15px !important;

        box-shadow:
            0 5px 20px rgba(
                40,
                70,
                115,
                0.09
            ) !important;
    }


    div[data-testid="stChatInput"] textarea {

        color: #243f68 !important;

        font-size: 13px !important;
    }


    div[data-testid="stChatInput"]
    textarea::placeholder {

        color: #91a4c0 !important;

        opacity: 1 !important;
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 800px) {

        .main-title {

            font-size: 29px;
        }

        .main-subtitle {

            font-size: 12px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


if "question_count" not in st.session_state:

    st.session_state.question_count = 0


if "documents_loaded" not in st.session_state:

    st.session_state.documents_loaded = False


if "chunks" not in st.session_state:

    st.session_state.chunks = []


if "index" not in st.session_state:

    st.session_state.index = None


if "embedder" not in st.session_state:

    st.session_state.embedder = None


if "pending_question" not in st.session_state:

    st.session_state.pending_question = None


# ============================================================
# LOAD RAG SYSTEM
# ============================================================

try:

    if not st.session_state.documents_loaded:

        index, chunks, embedder = (
            build_rag_system()
        )

        st.session_state.index = index

        st.session_state.chunks = chunks

        st.session_state.embedder = embedder

        if index is not None:

            st.session_state.documents_loaded = True

except Exception as e:

    print(
        f"RAG loading error: {e}"
    )

    st.session_state.index = None

    st.session_state.chunks = []

    st.session_state.embedder = None

    st.session_state.documents_loaded = False


# ============================================================
# PROCESS QUESTION
# ============================================================

def process_question(question):

    question = question.strip()

    if not question:

        return


    # --------------------------------------------------------
    # ADD USER MESSAGE
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    # --------------------------------------------------------
    # UPDATE QUESTION COUNT
    # --------------------------------------------------------

    st.session_state.question_count += 1


    # --------------------------------------------------------
    # RUN RAG PIPELINE
    # --------------------------------------------------------

    answer, sources = ask_rag(
        question,
        st.session_state.index,
        st.session_state.chunks,
        st.session_state.embedder,
        top_k=4
    )


    # --------------------------------------------------------
    # SAVE ASSISTANT MESSAGE
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": sources
        }
    )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:


    # --------------------------------------------------------
    # BRAND
    # --------------------------------------------------------

    st.markdown(
        "### 📚 Domain-Specific RAG Assistant"
    )

    st.caption(
        "College Academic Policies & "
        "Student Handbook"
    )


    # --------------------------------------------------------
    # NEW CHAT
    # --------------------------------------------------------

    if st.button(
        "＋ New Chat",
        use_container_width=True,
        key="new_chat"
    ):

        st.session_state.messages = []

        st.session_state.question_count = 0

        st.session_state.pending_question = None

        st.rerun()


    st.markdown(
        '<div class="sidebar-divider"></div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # AVAILABLE RESOURCES
    # --------------------------------------------------------

    st.markdown(
        "### 📖 AVAILABLE RESOURCES",
        help="Documents available to the RAG chatbot"
    )


    st.markdown(
        "📘 **Student Handbook**"
    )

    st.markdown(
        "🟢 Available"
    )


    st.markdown(
        "📗 **Academic Regulations**"
    )

    st.markdown(
        "🟢 Available"
    )


    st.markdown(
        "📕 **Examination Guidelines**"
    )

    st.markdown(
        "🟢 Available"
    )


    st.markdown(
        '<div class="sidebar-divider"></div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # RAG PIPELINE
    # --------------------------------------------------------

    st.markdown(
        "### 🔎 RAG PIPELINE"
    )


    st.markdown(
        "🔵 **1** &nbsp; Question"
    )


    st.markdown(
        "🔵 **2** &nbsp; Text Embedding"
    )


    st.markdown(
        "🔵 **3** &nbsp; FAISS Retrieval"
    )


    st.markdown(
        "🔵 **4** &nbsp; Gemini Generation"
    )


    st.markdown(
        '<div class="sidebar-divider"></div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # SESSION
    # --------------------------------------------------------

    st.markdown(
        "### 💬 SESSION"
    )


    st.caption(
        f"Questions asked: "
        f"{st.session_state.question_count}"
    )


    # --------------------------------------------------------
    # CLEAR CHAT
    # --------------------------------------------------------

    if st.button(
        "🗑 Clear Conversation",
        use_container_width=True,
        key="clear_chat"
    ):

        st.session_state.messages = []

        st.session_state.question_count = 0

        st.session_state.pending_question = None

        st.rerun()


    st.caption(
        "Answers are generated using information "
        "retrieved from the provided university documents."
    )


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    '<div class="ai-label">'
    '✨ AI-Powered Document Assistant'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="main-title">'
    'Domain-Specific RAG Chatbot'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="main-subtitle">'
    'Ask questions about your college academic policies, '
    'regulations, and student handbook.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# INFORMATION
# ============================================================

st.info(
    "This chatbot answers questions using the provided "
    "university documents. If the required information is "
    "not available in the documents, the chatbot will tell you."
)


# ============================================================
# WELCOME SCREEN
# ============================================================

if not st.session_state.messages:


    welcome_container = st.container(
        border=True
    )


    with welcome_container:

        st.markdown(
            '<div class="welcome-icon">📖</div>',
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="welcome-title">'
            'How can I help you?'
            '</div>',
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="welcome-subtitle">'
            'Ask a question about your university documents.'
            '</div>',
            unsafe_allow_html=True
        )


    # --------------------------------------------------------
    # TRY ASKING
    # --------------------------------------------------------

    st.markdown(
        '<div class="try-title">'
        '💡 &nbsp; Try asking'
        '</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # QUESTIONS 1 AND 2
    # --------------------------------------------------------

    col1, col2 = st.columns(
        2,
        gap="medium"
    )


    with col1:

        st.markdown(
            '<div class="suggested-question">',
            unsafe_allow_html=True
        )


        if st.button(
            "What is the minimum attendance requirement?",
            key="suggested_question_1",
            use_container_width=True
        ):

            st.session_state.pending_question = (
                "What is the minimum attendance requirement?"
            )


        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            '<div class="suggested-question">',
            unsafe_allow_html=True
        )


        if st.button(
            "What are the academic regulations?",
            key="suggested_question_2",
            use_container_width=True
        ):

            st.session_state.pending_question = (
                "What are the academic regulations?"
            )


        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


    # --------------------------------------------------------
    # QUESTIONS 3 AND 4
    # --------------------------------------------------------

    col3, col4 = st.columns(
        2,
        gap="medium"
    )


    with col3:

        st.markdown(
            '<div class="suggested-question">',
            unsafe_allow_html=True
        )


        if st.button(
            "What information is provided about academic records?",
            key="suggested_question_3",
            use_container_width=True
        ):

            st.session_state.pending_question = (
                "What information is provided about academic records?"
            )


        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


    with col4:

        st.markdown(
            '<div class="suggested-question">',
            unsafe_allow_html=True
        )


        if st.button(
            "What happens if a student does not meet the attendance requirement?",
            key="suggested_question_4",
            use_container_width=True
        ):

            st.session_state.pending_question = (
                "What happens if a student does not meet "
                "the attendance requirement?"
            )


        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


# ============================================================
# CHAT HISTORY
# ============================================================

for message in st.session_state.messages:


    # --------------------------------------------------------
    # USER MESSAGE
    # --------------------------------------------------------

    if message["role"] == "user":

        with st.chat_message(
            "user",
            avatar="👤"
        ):

            st.markdown(
                message["content"]
            )


    # --------------------------------------------------------
    # ASSISTANT MESSAGE
    # --------------------------------------------------------

    else:

        with st.chat_message(
            "assistant",
            avatar="📚"
        ):


            # ------------------------------------------------
            # AI ANSWER
            # ------------------------------------------------

            st.markdown(
                message["content"]
            )


            # ------------------------------------------------
            # RETRIEVED SOURCES
            # ------------------------------------------------

            sources = message.get(
                "sources",
                []
            )


            if sources:

                with st.expander(
                    "📚 View Retrieved Text",
                    expanded=False
                ):


                    for i, source in enumerate(
                        sources,
                        start=1
                    ):


                        st.markdown(
                            f"**Source {i}**"
                        )


                        st.markdown(
                            f"**Document:** "
                            f"`{source['source']}`"
                        )


                        st.markdown(
                            f"**Page:** "
                            f"`{source['page']}`"
                        )


                        st.markdown(
                            "**Retrieved text from the source:**"
                        )


                        retrieved_text = (
                            source.get(
                                "retrieved_text",
                                source.get(
                                    "text",
                                    ""
                                )
                            )
                        )


                        st.text(
                            retrieved_text
                        )


                        if i < len(sources):

                            st.divider()


# ============================================================
# PROCESS SUGGESTED QUESTION
# ============================================================

if st.session_state.pending_question:

    question = (
        st.session_state.pending_question
    )

    st.session_state.pending_question = None

    process_question(
        question
    )

    st.rerun()


# ============================================================
# CHAT INPUT
# ============================================================

user_question = st.chat_input(
    "Ask something about your documents..."
)


if user_question:

    process_question(
        user_question
    )

    st.rerun()