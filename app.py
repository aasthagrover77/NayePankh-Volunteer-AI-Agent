import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from ai_agent import ask_agent
from volunteer_db import (
    init_db,
    add_volunteer,
    get_volunteers
)

# ==========================
# Initialize Database
# ==========================

init_db()

# ==========================
# Page Config
# ==========================

st.set_page_config(
    page_title="NayePankh AI Agent",
    page_icon="🤖",
    layout="wide"
)

# ==========================
# Sidebar
# ==========================

st.sidebar.title("🤖 NayePankh AI Agent")

st.sidebar.info("""
### Features

✅ Volunteer Registration

✅ AI Role Recommendation

✅ Volunteer Dashboard

✅ Volunteer Analytics

✅ AI Assistant

✅ SQLite Database
""")

# ==========================
# Title Section
# ==========================

st.title("🤖 NayePankh Volunteer AI Agent")

st.markdown("""
### Empowering NGOs with AI-Powered Volunteer Management

This AI Agent helps NayePankh Foundation:

- Register Volunteers
- Recommend Suitable Roles
- Track Volunteer Data
- Analyze Volunteer Interests
- Answer Common Questions
- Improve Volunteer Engagement
""")

# ==========================
# Load Knowledge Base
# ==========================

with open("data/ngo_info.txt", "r", encoding="utf-8") as f:
    context = f.read()

# ==========================
# Volunteer Registration
# ==========================

st.header("📝 Volunteer Registration")

with st.form(
    "registration_form",
    clear_on_submit=True
):

    name = st.text_input(
        "Full Name"
    )

    email = st.text_input(
        "Email"
    )

    interest = st.selectbox(
        "Area of Interest",
        [
            "Select Interest",
            "Teaching",
            "Content Writing",
            "Social Media",
            "Graphic Design",
            "Event Management"
        ],
        index=0
    )

    submit = st.form_submit_button(
        "Register"
    )

    if submit:

        errors = []

        if not name.strip():
            errors.append(
                "Full Name is required."
            )

        if not email.strip():
            errors.append(
                "Email is required."
            )

        elif "@" not in email or "." not in email:
            errors.append(
                "Please enter a valid email address."
            )

        if interest == "Select Interest":
            errors.append(
                "Please select an Area of Interest."
            )

        if errors:

            for error in errors:
                st.error(error)

        else:

            add_volunteer(
                name,
                email,
                interest
            )

            st.success(
                "Volunteer Registered Successfully!"
            )

            recommendations = {
                "Teaching":
                "Education Support Program",

                "Content Writing":
                "Awareness Campaign Team",

                "Social Media":
                "Digital Outreach Team",

                "Graphic Design":
                "Creative Design Team",

                "Event Management":
                "Community Events Team"
            }

            st.info(
                f"🎯 Recommended Role: {recommendations[interest]}"
            )

# ==========================
# Statistics
# ==========================

volunteers = get_volunteers()

total_volunteers = len(volunteers)

teaching_count = sum(
    1 for v in volunteers
    if v[2] == "Teaching"
)

content_count = sum(
    1 for v in volunteers
    if v[2] == "Content Writing"
)

social_count = sum(
    1 for v in volunteers
    if v[2] == "Social Media"
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Volunteers",
        total_volunteers
    )

with col2:
    st.metric(
        "Teaching",
        teaching_count
    )

with col3:
    st.metric(
        "Content Writing",
        content_count
    )

with col4:
    st.metric(
        "Social Media",
        social_count
    )

st.divider()

# ==========================
# Volunteer Interest Chart
# ==========================

interest_counts = {}

for volunteer in volunteers:

    interest = volunteer[2]

    interest_counts[interest] = (
        interest_counts.get(interest, 0) + 1
    )

if interest_counts:

    st.subheader(
        "📊 Volunteer Interest Distribution"
    )

    fig, ax = plt.subplots(
        figsize=(6, 6)
    )

    ax.pie(
        interest_counts.values(),
        labels=interest_counts.keys(),
        autopct="%1.1f%%",
        startangle=90
    )

    ax.axis("equal")

    st.pyplot(fig)

st.divider()

# ==========================
# Volunteer Dashboard
# ==========================

st.header("📋 Registered Volunteers")

if volunteers:

    df = pd.DataFrame(
        volunteers,
        columns=[
            "Name",
            "Email",
            "Interest"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No volunteers registered yet."
    )

st.divider()

# ==========================
# AI Assistant
# ==========================

st.header("🤖 NayePankh AI Volunteer Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input(
    "Ask about volunteering, internships, or the foundation..."
)

if user_input:

    answer = ask_agent(
        user_input,
        context
    )

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])