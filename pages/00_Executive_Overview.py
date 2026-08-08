"""Executive Overview — Landing page for Riyadh V2G Digital Twin — Architecture Explorer."""

import textwrap

import streamlit as st
from demo_components.ui_elements import (
    page_header,
    section_title,
    info_callout,
    render_footer,
    render_watermark,
    metric_card,
    metric_card_row,
)
from demo_components.constants import (
    PRIMARY,
    ACCENT,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    CARD_BACKGROUND,
    BORDER,
)


def main():
    # ── Page Header ──────────────────────────────────────────
    page_header(
        "Riyadh V2G Digital Twin — Architecture Explorer",
        "Interactive Engineering Portfolio — Architecture, Execution & Scale",
    )

    # ── Hero Tagline ─────────────────────────────────────────
    st.markdown(
        textwrap.dedent(f"""\
        <div style="
            text-align: center;
            margin: 0 0 12px 0;
            padding: 0;
        ">
            <p style="
                color: {PRIMARY};
                font-size: 1.55rem;
                font-weight: 700;
                margin: 0 0 6px 0;
                line-height: 1.3;
            ">From Architecture to Sovereign-Scale Grid Intelligence</p>
            <p style="
                color: {TEXT_SECONDARY};
                font-size: 1rem;
                margin: 0;
                line-height: 1.5;
            ">A production-scale Digital Twin engineered for grid flexibility, software architecture, and deterministic system design.</p>
        </div>
        """),
        unsafe_allow_html=True,
    )

    # ── Hero Illustration — Production → Explorer → Demo ────
    st.markdown(
        textwrap.dedent(f"""\
        <div style="
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 24px;
            margin: 20px 0 32px 0;
            padding: 24px;
            background: linear-gradient(135deg, rgba(0,180,216,0.05) 0%, rgba(255,107,53,0.05) 100%);
            border-radius: 12px;
            border: 1px solid {BORDER};
            flex-wrap: wrap;
        ">
            <div style="text-align: center; min-width: 140px;">
                <div style="font-size: 2rem; margin-bottom: 6px;">⚙️</div>
                <div style="color: {TEXT_PRIMARY}; font-weight: 600; font-size: 0.9rem;">Production Platform</div>
                <div style="color: {TEXT_SECONDARY}; font-size: 0.7rem;">60K Transformers · 1M EVs</div>
            </div>
            <div style="color: {ACCENT}; font-size: 1.5rem; font-weight: 700;">→</div>
            <div style="text-align: center; min-width: 140px;">
                <div style="font-size: 2rem; margin-bottom: 6px;">🏛️</div>
                <div style="color: {TEXT_PRIMARY}; font-weight: 600; font-size: 0.9rem;">Architecture Explorer</div>
                <div style="color: {TEXT_SECONDARY}; font-size: 0.7rem;">This Portfolio</div>
            </div>
            <div style="color: {ACCENT}; font-size: 1.5rem; font-weight: 700;">→</div>
            <div style="text-align: center; min-width: 140px;">
                <div style="font-size: 2rem; margin-bottom: 6px;">📊</div>
                <div style="color: {TEXT_PRIMARY}; font-weight: 600; font-size: 0.9rem;">Synthetic Demo</div>
                <div style="color: {TEXT_SECONDARY}; font-size: 0.7rem;">97 Transformers · 512 EVs</div>
            </div>
        </div>
        """),
        unsafe_allow_html=True,
    )

    # ── Engineering Highlights (5 badges) ────────────────────
    badges = [
        ("📦", "Modular Architecture"),
        ("🔁", "Reproducible Execution"),
        ("📐", "Scalable Design"),
        ("🔒", "Protected IP"),
        ("📄", "Published Research"),
    ]

    badge_items = "".join(
        f"""
        <div class="eng-badge">
            <span style="margin-right: 6px;">{icon}</span>{label}
        </div>"""
        for icon, label in badges
    )

    st.markdown(
        textwrap.dedent(f"""\
        <style>
        .eng-badges-row {{
            display: flex;
            gap: 12px;
            margin: 20px 0;
            flex-wrap: wrap;
            justify-content: center;
        }}
        .eng-badge {{
            background-color: {CARD_BACKGROUND};
            border: 1px solid {BORDER};
            border-radius: 20px;
            padding: 10px 22px;
            color: {TEXT_PRIMARY};
            font-size: 0.84rem;
            white-space: nowrap;
            display: flex;
            align-items: center;
            height: 42px;
            box-sizing: border-box;
        }}
        </style>
        <div class="eng-badges-row">
            {badge_items}
        </div>
        """),
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Metric Cards ─────────────────────────────────────────
    metric_card_row([
        {
            "title": "Infrastructure Scale",
            "value": "60,000",
            "subtitle": "Distribution Transformers",
            "annotation": "Demo scale: 97",
        },
        {
            "title": "Electric Vehicle Fleet",
            "value": "1,000,000",
            "subtitle": "EVs",
            "annotation": "Demo scale: 512",
        },
        {
            "title": "Workflow Complexity",
            "value": "29",
            "subtitle": "Processing Stages",
            "annotation": " ",
        },
        {
            "title": "Software Footprint",
            "value": "42,000+",
            "subtitle": "180+ Python Modules",
            "annotation": " ",
        },
    ])

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Trusted Evidence ─────────────────────────────────────
    section_title("Trusted Evidence")

    evidence = [
        ("📄", "Zenodo", "DOI Published"),
        ("🔒", "BOIP", "EU Registered IP"),
        ("💻", "GitHub", "Architecture Showcase"),
        ("📊", "ResearchGate", "Technical Report"),
    ]

    ev_cols = st.columns(len(evidence))
    for col, (icon, platform, detail) in zip(ev_cols, evidence):
        with col:
            st.markdown(
                textwrap.dedent(f"""\
                <div style="
                    text-align: center;
                    padding: 12px 8px;
                    background: transparent;
                ">
                    <div style="font-size: 1.6rem; margin-bottom: 6px;">{icon}</div>
                    <div style="color: {TEXT_PRIMARY}; font-weight: 600; font-size: 0.88rem;">
                        {platform}
                    </div>
                    <div style="color: {TEXT_SECONDARY}; font-size: 0.75rem;">
                        {detail}
                    </div>
                </div>
                """),
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── What This Is ─────────────────────────────────────────
    section_title("What This Is")
    st.markdown(
        textwrap.dedent(f"""\
        <p style="color: {TEXT_PRIMARY}; font-size: 1rem; line-height: 1.7; margin-bottom: 16px;">
        This is an interactive engineering portfolio demonstrating the <strong>software
        architecture</strong> of a large-scale infrastructure modelling platform. Built to
        showcase engineering quality, modular software design, and professional software
        development practices, it walks through the system's computational layers,
        operational pipeline, and the architectural decisions that enable deterministic,
        reproducible execution at scale.
        </p>
        """),
        unsafe_allow_html=True,
    )

    # ── What This Is NOT ─────────────────────────────────────
    section_title("What This Is NOT")
    st.markdown(
        textwrap.dedent(f"""\
        <p style="color: {TEXT_PRIMARY}; font-size: 1rem; line-height: 1.7; margin-bottom: 16px;">
        This is <strong>not a simulation</strong>. No production algorithms, dispatch logic,
        computational models, or calibration data are included. The production platform is
        protected intellectual property. All data shown is synthetic and at a reduced demo
        scale, intended solely to illustrate the architecture's structure and behaviour.
        </p>
        """),
        unsafe_allow_html=True,
    )

    # ── Callouts ─────────────────────────────────────────────
    info_callout(
        "For private demonstrations of the full-scale production platform, including "
        "proprietary computational models and protected engineering capabilities, "
        "please contact the author. Available under NDA.",
        callout_type="protected",
    )

    info_callout(
        "This project is registered intellectual property (EU Registered). "
        "Published on Zenodo (DOI: 10.5281/zenodo.21400746).",
        callout_type="info",
    )

    # ── Footer & Watermark ───────────────────────────────────
    render_footer()
    render_watermark()


main()
