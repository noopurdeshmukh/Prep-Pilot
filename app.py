import streamlit as st


def apply_custom_css() -> None:
    """Apply the custom pastel UI styles for the Prep-Pilot landing page."""
    st.markdown(
        """
        <style>
        :root {
            color-scheme: light;
            color: #3B2B5B;
            font-family: 'Inter', sans-serif;
            background: #F7F2FF;
        }

        body, .main, [data-testid='stAppViewContainer'] {
            background: linear-gradient(180deg, #F9F4FF 0%, #F5EEFF 100%);
        }

        .block-container {
            padding-top: 1rem;
            padding-left: 1rem;
            padding-right: 1rem;
            padding-bottom: 1rem;
        }

        .hero-card,
        .login-card,
        .feature-card,
        .dashboard-card,
        .mascot-card {
            background: rgba(255, 255, 255, 0.92);
            border: 1px solid rgba(143, 116, 255, 0.16);
            box-shadow: 0 24px 60px rgba(105, 82, 255, 0.08);
            border-radius: 32px;
        }

        .hero-card {
            padding: 2rem;
        }

        .section-title {
            color: #8B6FF7;
            text-transform: uppercase;
            letter-spacing: 0.18em;
            font-size: 0.9rem;
            font-weight: 800;
            margin-bottom: 1rem;
        }

        .hero-headline {
            color: #2F1D55;
            font-size: clamp(2.5rem, 4vw, 4rem);
            line-height: 1.02;
            margin: 0;
        }

        .hero-text,
        .card-text,
        .feature-description,
        .welcome-text {
            color: #5E4C8A;
            font-size: 1rem;
            line-height: 1.75;
        }

        .cta-row {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            margin-top: 1.75rem;
        }

        .button-container button,
        .stButton>button {
            border-radius: 999px !important;
            font-weight: 700;
            padding: 0.95rem 1.7rem !important;
            min-width: 160px;
            transition: transform 0.22s ease, box-shadow 0.22s ease;
        }

        .stButton>button {
            border: none;
            color: white;
            background: linear-gradient(135deg, #9C83FF 0%, #C5A2FF 100%) !important;
        }

        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 18px 35px rgba(105, 82, 255, 0.18);
        }

        .secondary-button .stButton>button,
        .secondary-button button {
            background: #F4EFFF !important;
            color: #5E4C8A !important;
            border: 1px solid rgba(141, 119, 255, 0.24) !important;
        }

        .mascot-card {
            padding: 2rem;
            text-align: center;
        }

        .mascot-icon {
            font-size: 3.5rem;
            margin-bottom: 1rem;
        }

        .mascot-heading {
            margin: 0;
            font-size: 1.35rem;
            color: #3A2564;
            font-weight: 800;
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1rem;
            margin-top: 1.5rem;
        }

        .feature-card {
            padding: 1.5rem;
        }

        .feature-title {
            margin: 0 0 0.65rem;
            font-size: 1.05rem;
            color: #3A2564;
            font-weight: 800;
        }

        .welcome-panel {
            padding: 1.75rem;
            margin-top: 1.5rem;
        }

        .footer-note {
            text-align: center;
            color: #7B66A7;
            margin-top: 2rem;
            font-size: 0.95rem;
        }

        .stTextInput>div>div>input,
        .stTextInput>div>div>textarea {
            border-radius: 18px;
            border: 1px solid rgba(142, 119, 255, 0.22);
            padding: 0.9rem 1rem;
        }

        .stForm>div>button {
            width: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def initialize_session_state() -> None:
    """Initialize the session state values used by the app."""
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user_name" not in st.session_state:
        st.session_state.user_name = "Study Pilot"
    if "page" not in st.session_state:
        st.session_state.page = "home"


def show_home_page() -> None:
    """Render the landing page hero section and authentication prompts."""
    st.markdown('<div class="hero-card">', unsafe_allow_html=True)
    left, right = st.columns([2, 1], gap="large")

    with left:
        st.markdown('<div class="section-title">Prep-Pilot</div>', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-headline">Your AI-Powered Study Companion</h1>', unsafe_allow_html=True)
        st.markdown(
            '<p class="hero-text">Prep-Pilot helps you prepare, plan, and grow with warm, friendly study guidance tailored to your own learning style.</p>',
            unsafe_allow_html=True,
        )

        cta1, cta2 = st.columns([1, 1], gap="small")
        with cta1:
            if st.button("Login", key="hero_login"):
                st.session_state.page = "login"
        with cta2:
            if st.button("Sign up", key="hero_signup"):
                st.session_state.page = "signup"

    with right:
        st.markdown('<div class="mascot-card">', unsafe_allow_html=True)
        st.markdown('<div class="mascot-icon">🐻✨</div>', unsafe_allow_html=True)
        st.markdown('<h3 class="mascot-heading">Hello, friend!</h3>', unsafe_allow_html=True)
        st.markdown(
            '<p class="hero-text">A cozy study companion is here to keep your learning journey bright, calm, and confident.</p>',
            unsafe_allow_html=True,
        )
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if not st.session_state.logged_in:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        st.markdown('<h2>Welcome to Prep-Pilot</h2>', unsafe_allow_html=True)
        st.markdown(
            '<p class="welcome-text">Get started by logging in or creating a free account. Your study companion is ready to help you plan smarter and learn with confidence.</p>',
            unsafe_allow_html=True,
        )
        login_col, signup_col = st.columns(2, gap="large")
        with login_col:
            if st.button("Go to Login", key="home_login"):
                st.session_state.page = "login"
        with signup_col:
            if st.button("Create Account", key="home_signup"):
                st.session_state.page = "signup"
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        show_dashboard()


def show_login() -> None:
    """Render a simple login placeholder screen."""
    st.markdown('<div class="hero-card">', unsafe_allow_html=True)
    st.subheader("Login to Prep-Pilot")
    st.markdown(
        '<p class="hero-text">Use a friendly name to join your personalized study dashboard for now.</p>',
        unsafe_allow_html=True,
    )

    with st.form(key="login_form"):
        name = st.text_input("Your name", value="", placeholder="e.g. Alex")
        submitted = st.form_submit_button("Login")
        if submitted:
            if name.strip():
                st.session_state.logged_in = True
                st.session_state.user_name = name.strip()
                st.session_state.page = "home"
                st.success(f"Welcome back, {st.session_state.user_name}! 🎉")
            else:
                st.warning("Please enter a name to continue.")

    st.markdown("---")
    if st.button("Back to Home", key="login_back"):
        st.session_state.page = "home"
    st.markdown('</div>', unsafe_allow_html=True)


def show_signup() -> None:
    """Render a simple signup placeholder screen."""
    st.markdown('<div class="hero-card">', unsafe_allow_html=True)
    st.subheader("Sign up for Prep-Pilot")
    st.markdown(
        '<p class="hero-text">Create your friendly study account and begin building a calm, easy study routine.</p>',
        unsafe_allow_html=True,
    )

    with st.form(key="signup_form"):
        name = st.text_input("Your name", value="", placeholder="e.g. Mia")
        email = st.text_input("Email address", value="", placeholder="optional for now")
        submitted = st.form_submit_button("Sign up")
        if submitted:
            if name.strip():
                st.session_state.logged_in = True
                st.session_state.user_name = name.strip()
                st.session_state.page = "home"
                st.success(f"Welcome aboard, {st.session_state.user_name}! 🚀")
            else:
                st.warning("Please enter a name to continue.")

    st.markdown("---")
    if st.button("Back to Home", key="signup_back"):
        st.session_state.page = "home"
    st.markdown('</div>', unsafe_allow_html=True)


def show_dashboard() -> None:
    """Render the logged-in dashboard section with feature placeholders."""
    st.markdown('<div class="welcome-panel">', unsafe_allow_html=True)
    st.markdown(f"<h2>Welcome back, {st.session_state.user_name}!</h2>", unsafe_allow_html=True)
    st.markdown(
        '<p class="welcome-text">Your Prep-Pilot companion is ready to help with planning, progress tracking, notes, and study guidance.</p>',
        unsafe_allow_html=True,
    )

    button_col1, button_col2 = st.columns([1, 1], gap="large")
    with button_col1:
        if st.button("Dashboard Home", key="dashboard_home"):
            st.session_state.page = "home"
    with button_col2:
        if st.button("Logout", key="logout"):
            st.session_state.logged_in = False
            st.session_state.user_name = "Study Pilot"
            st.session_state.page = "home"
            st.success("You have been logged out. Come back soon! 💜")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="feature-grid">', unsafe_allow_html=True)

    features = [
        ("📚 Study Planner", "Build your weekly study schedule with calm reminders and friendly pacing."),
        ("🤖 AI Study Assistant", "Ask questions, review concepts, and personalize your learning style."),
        ("📊 Progress Tracker", "Watch your study streaks and growth in a warm, friendly dashboard."),
        ("📝 Notes Manager", "Keep your key ideas, summaries, and study snippets neatly organized."),
        ("🎯 Goal Tracker", "Set learning goals and celebrate progress with confidence."),
    ]

    for title, description in features:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="feature-title">{title}</div>', unsafe_allow_html=True)
        st.markdown(f'<p class="feature-description">{description}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="footer-note">Prepare with kindness, growth, and confidence. Prep-Pilot is here for every step of your study journey.</div>', unsafe_allow_html=True)


def main() -> None:
    """App entry point and page routing."""
    st.set_page_config(page_title="Prep-Pilot", page_icon="🧸", layout="wide")
    apply_custom_css()
    initialize_session_state()

    if st.session_state.page == "login":
        show_login()
    elif st.session_state.page == "signup":
        show_signup()
    else:
        show_home_page()


if __name__ == "__main__":
    main()
