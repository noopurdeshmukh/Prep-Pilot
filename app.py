import streamlit as st


def apply_custom_css() -> None:
    """Apply the green monochrome UI styles for Prep-Pilot."""
    st.markdown(
        """
        <style>
        :root {
            color-scheme: light;
            color: #16482A;
            font-family: 'Inter', sans-serif;
        }

        body, .main, [data-testid='stAppViewContainer'] {
            background: linear-gradient(180deg, #F2FBF4 0%, #E5F7E9 100%);
        }

        .block-container {
            padding: 2rem 2rem 1rem;
            max-width: 1180px;
        }

        .sidebar .sidebar-content {
            background: rgba(255, 255, 255, 0.95) !important;
            border: 1px solid rgba(58, 132, 65, 0.14);
            border-radius: 28px;
            box-shadow: 0 20px 50px rgba(31, 89, 43, 0.08);
        }

        .hero-card,
        .auth-card,
        .feature-card,
        .dashboard-panel {
            background: rgba(255, 255, 255, 0.96);
            border: 1px solid rgba(53, 126, 62, 0.16);
            box-shadow: 0 24px 50px rgba(52, 112, 66, 0.08);
            border-radius: 32px;
        }

        .hero-card {
            padding: 2.2rem;
        }

        .section-title {
            color: #2F7F46;
            text-transform: uppercase;
            letter-spacing: 0.22em;
            font-size: 0.85rem;
            font-weight: 800;
            margin-bottom: 1rem;
        }

        .hero-headline {
            color: #12391F;
            font-size: clamp(2.5rem, 4vw, 3.8rem);
            line-height: 1.02;
            margin: 0;
        }

        .hero-text,
        .feature-description,
        .welcome-text,
        .sidebar-note {
            color: #2F5F3F;
            font-size: 1rem;
            line-height: 1.7;
        }

        .hero-stat {
            color: #1F5D34;
            font-size: 1.05rem;
            font-weight: 600;
            margin-top: 1.75rem;
        }

        .stButton>button {
            border-radius: 999px !important;
            font-weight: 700;
            padding: 0.9rem 1.8rem !important;
            min-width: 170px;
            transition: transform 0.22s ease, box-shadow 0.22s ease;
            border: none !important;
            color: white !important;
            background: linear-gradient(135deg, #2F8F4E 0%, #69C785 100%) !important;
        }

        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 18px 36px rgba(38, 89, 45, 0.18);
        }

        .secondary-button .stButton>button,
        .secondary-button button {
            background: #E8F8ED !important;
            color: #2F7F46 !important;
            border: 1px solid rgba(63, 147, 80, 0.18) !important;
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 1.1rem;
            margin-top: 1.75rem;
        }

        .feature-card {
            padding: 1.5rem;
            min-height: 155px;
        }

        .feature-title {
            margin: 0 0 0.75rem;
            font-size: 1.05rem;
            color: #154025;
            font-weight: 800;
        }

        .welcome-panel {
            padding: 1.75rem;
            margin-top: 1.5rem;
        }

        .auth-card {
            padding: 1.75rem;
            margin-top: 1.5rem;
        }

        .sidebar-divider {
            margin: 1.5rem 0;
            border-top: 1px solid rgba(47, 133, 66, 0.12);
        }

        .footer-note {
            text-align: center;
            color: #4B6F52;
            margin-top: 2rem;
            font-size: 0.95rem;
        }

        .stTextInput>div>div>input,
        .stTextInput>div>div>textarea {
            border-radius: 18px;
            border: 1px solid rgba(62, 143, 74, 0.2);
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


def show_sidebar() -> None:
    """Render the app sidebar with single login/signup navigation."""
    st.sidebar.markdown("# Prep-Pilot")
    st.sidebar.markdown("Your green AI study companion for calm planning and better habits.")

    if st.session_state.logged_in:
        st.sidebar.success(f"Logged in as {st.session_state.user_name}")

    st.sidebar.markdown("---")

    pages = ["Home"]
    if st.session_state.logged_in:
        pages.append("Dashboard")
    else:
        pages.extend(["Login", "Sign Up"])

    choice = st.sidebar.radio("Navigation", pages, index=pages.index(_normalize_page_name(st.session_state.page)))
    selected = _page_key_from_label(choice)
    st.session_state.page = selected

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Features")
    st.sidebar.markdown(
        "- 📚 Study Planner  \n"
        "- 🤖 AI Study Assistant  \n"
        "- 📊 Progress Tracker  \n"
        "- 📝 Notes Manager  \n"
        "- 🎯 Goal Tracker"
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("#### Need a quick start?")
    if st.sidebar.button("Go to Home"):
        st.session_state.page = "home"
    if st.session_state.logged_in and st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_name = "Study Pilot"
        st.session_state.page = "home"
        st.success("Logged out successfully. See you soon! 🌿")


def _normalize_page_name(page: str) -> str:
    return {
        "home": "Home",
        "dashboard": "Dashboard",
        "login": "Login",
        "signup": "Sign Up",
    }.get(page, "Home")


def _page_key_from_label(label: str) -> str:
    return {
        "Home": "home",
        "Dashboard": "dashboard",
        "Login": "login",
        "Sign Up": "signup",
    }.get(label, "home")


def show_home_page() -> None:
    """Render the landing page hero section."""
    st.markdown('<div class="hero-card">', unsafe_allow_html=True)
    left, right = st.columns([2, 1], gap="large")

    with left:
        st.markdown('<div class="section-title">Prep-Pilot</div>', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-headline">Your AI-Powered Study Companion</h1>', unsafe_allow_html=True)
        st.markdown(
            '<p class="hero-text">A calm, green learning workspace designed to feel friendly, supportive, and easy to use.</p>',
            unsafe_allow_html=True,
        )
        if st.session_state.logged_in:
            st.markdown('<p class="hero-stat">You are signed in. Open your dashboard from the sidebar to explore your study tools.</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="hero-stat">Use the sidebar to log in or sign up, then explore dashboards, study planners, and progress tools.</p>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown('<h3 class="feature-title">Study companion mood</h3>', unsafe_allow_html=True)
        st.markdown('<p class="feature-description">Soft green tones, warm guidance, and a clean study surface that feels like a supportive partner.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="feature-grid">', unsafe_allow_html=True)
    for title, description in [
        ("Study Planner", "Plan your week with gentle reminders and smart session blocks."),
        ("AI Study Assistant", "Ask for explanations, summaries, and custom study tips."),
        ("Progress Tracker", "Track your streaks, milestones, and learning energy."),
    ]:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="feature-title">{title}</div>', unsafe_allow_html=True)
        st.markdown(f'<p class="feature-description">{description}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="footer-note">The app is intentionally simple today: everything starts from the sidebar navigation and grows from there.</div>', unsafe_allow_html=True)


def show_login() -> None:
    """Render the login placeholder page."""
    st.markdown('<div class="auth-card">', unsafe_allow_html=True)
    st.subheader("Login to Prep-Pilot")
    st.markdown('<p class="hero-text">Enter your name to join your calming study dashboard.</p>', unsafe_allow_html=True)

    with st.form(key="login_form"):
        name = st.text_input("Your name", value="", placeholder="e.g. Alex")
        submitted = st.form_submit_button("Login")
        if submitted:
            if name.strip():
                st.session_state.logged_in = True
                st.session_state.user_name = name.strip()
                st.session_state.page = "dashboard"
                st.success(f"Welcome back, {st.session_state.user_name}! 🌿")
            else:
                st.warning("Please enter a name to continue.")

    st.markdown('</div>', unsafe_allow_html=True)


def show_signup() -> None:
    """Render the signup placeholder page."""
    st.markdown('<div class="auth-card">', unsafe_allow_html=True)
    st.subheader("Sign up for Prep-Pilot")
    st.markdown('<p class="hero-text">Create your friendly study companion profile with just a name.</p>', unsafe_allow_html=True)

    with st.form(key="signup_form"):
        name = st.text_input("Your name", value="", placeholder="e.g. Mia")
        email = st.text_input("Email address", value="", placeholder="optional for now")
        submitted = st.form_submit_button("Sign up")
        if submitted:
            if name.strip():
                st.session_state.logged_in = True
                st.session_state.user_name = name.strip()
                st.session_state.page = "dashboard"
                st.success(f"Welcome aboard, {st.session_state.user_name}! 🌱")
            else:
                st.warning("Please enter a name to continue.")

    st.markdown('</div>', unsafe_allow_html=True)


def show_dashboard() -> None:
    """Render the logged-in dashboard section with feature placeholders."""
    if not st.session_state.logged_in:
        st.warning("Please log in through the sidebar to access your dashboard.")
        return

    st.markdown('<div class="dashboard-panel">', unsafe_allow_html=True)
    st.markdown(f"<h2>Welcome back, {st.session_state.user_name}!</h2>", unsafe_allow_html=True)
    st.markdown(
        '<p class="welcome-text">This is your study hub. Choose any feature from the sidebar, or explore the cards below.</p>',
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="feature-grid">', unsafe_allow_html=True)
    features = [
        ("📚 Study Planner", "Draft weekly study sessions and keep your schedule gentle and intentional."),
        ("🤖 AI Study Assistant", "Get quick answers, study tips, and concept summaries tailored to you."),
        ("📊 Progress Tracker", "See progress, streaks, and learning habits in a calming view."),
        ("📝 Notes Manager", "Store your study notes, reflections, and quick reminders in one place."),
        ("🎯 Goal Tracker", "Define your learning goals and celebrate each achievement."),
    ]
    for title, description in features:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="feature-title">{title}</div>', unsafe_allow_html=True)
        st.markdown(f'<p class="feature-description">{description}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="footer-note">Every placeholder above is ready to become your real study tool.</div>', unsafe_allow_html=True)


def main() -> None:
    """App entry point and page routing."""
    st.set_page_config(page_title="Prep-Pilot", page_icon="🧸", layout="wide")
    apply_custom_css()
    initialize_session_state()
    show_sidebar()

    if st.session_state.page == "login":
        show_login()
    elif st.session_state.page == "signup":
        show_signup()
    elif st.session_state.page == "dashboard":
        show_dashboard()
    else:
        show_home_page()


if __name__ == "__main__":
    main()
