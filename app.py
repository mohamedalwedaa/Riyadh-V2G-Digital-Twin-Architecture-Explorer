"""
Riyadh V2G Digital Twin — Architecture Explorer — Multi-page Streamlit Application.

This is NOT a simulation. This is an architectural portfolio demonstrating
the software architecture of a proprietary Digital Twin platform.

The Production Platform is protected under EU BOIP i-DEPOT #161617.
No production algorithms, data, or implementation are included.
"""

import streamlit as st
from demo_components.ui_elements import inject_css

# ── Inject global design system early ────────────────────────────
inject_css()

# ── Page definitions (string paths for files starting with digits) ──
EXECUTIVE_OVERVIEW = st.Page(
    "pages/00_Executive_Overview.py",
    title="Executive Overview",
    icon=":material/dashboard:",
    default=True,
)

SYSTEM_ARCH = st.Page(
    "pages/01_System_Architecture.py",
    title="System Architecture",
    icon=":material/account_tree:",
)

PIPELINE_EXPLORER = st.Page(
    "pages/02_Pipeline_Explorer.py",
    title="Pipeline Explorer",
    icon=":material/timeline:",
)

PRODUCTION_SCALE = st.Page(
    "pages/03_Production_Scale.py",
    title="Production Scale",
    icon=":material/ssid_chart:",
)

ENGINEERING_DECISIONS = st.Page(
    "pages/04_Engineering_Decisions.py",
    title="Engineering Decisions",
    icon=":material/gavel:",
)

PRODUCTION_EVIDENCE = st.Page(
    "pages/05_Production_Evidence.py",
    title="Production Evidence",
    icon=":material/verified:",
)

EVOLUTION_ROADMAP = st.Page(
    "pages/06_Evolution_Roadmap.py",
    title="Evolution Roadmap",
    icon=":material/trending_up:",
)

CREDENTIALS = st.Page(
    "pages/07_Professional_Credentials.py",
    title="Professional Record",
    icon=":material/license:",
)

CONTACT = st.Page(
    "pages/08_Contact.py",
    title="Contact",
    icon=":material/mail:",
)

# ── Navigation ──────────────────────────────────────────────────
pg = st.navigation(
    {
        "Overview": [EXECUTIVE_OVERVIEW],
        "Architecture": [SYSTEM_ARCH, PIPELINE_EXPLORER, PRODUCTION_SCALE],
        "Evidence & Evolution": [
            ENGINEERING_DECISIONS,
            PRODUCTION_EVIDENCE,
            EVOLUTION_ROADMAP,
        ],
        "About": [CREDENTIALS, CONTACT],
    },
    position="sidebar",
)

pg.run()
