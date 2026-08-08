"""Professional Record — Independent evidence of authorship, research, and engineering practice."""

import textwrap

import streamlit as st
from demo_components.ui_elements import (
    page_header,
    section_title,
    info_callout,
    render_footer,
    render_watermark,
    metric_card_row,
)
from demo_components.constants import (
    PRIMARY,
    ACCENT,
    SUCCESS,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    CARD_BACKGROUND,
    BORDER,
)


# ═══════════════════════════════════════════════════════════════════
#  Page
# ═══════════════════════════════════════════════════════════════════

def main():
    # ── Page Header ──────────────────────────────────────────
    page_header(
        "Professional Record",
        "Independent evidence of authorship, research, and engineering practice",
    )

    st.markdown(
        f'<p style="color:{TEXT_SECONDARY};font-size:0.92rem;'
        f'margin:-12px 0 24px 24px;line-height:1.5;">'
        'The Riyadh V2G Sovereign Digital Twin is supported by independently '
        'verifiable research publications, intellectual property registration, and '
        'public technical artefacts. Together they establish credibility without '
        'exposing proprietary implementation.'
        '</p>',
        unsafe_allow_html=True,
    )

    # ── Section 1: Professional Profile ──────────────────────
    section_title("Professional Profile")

    with st.container(border=True):
        st.markdown(
            textwrap.dedent(f"""\
            <div style="
                color:{TEXT_PRIMARY};
                font-size:1.25rem;
                font-weight:700;
                margin-bottom:6px;
            ">Mohamed Alwedaa</div>
            <div style="
                color:{PRIMARY};
                font-size:0.92rem;
                font-weight:500;
                margin-bottom:14px;
            ">Systems Architect &bull; Software Engineer &bull; Digital Twin Researcher</div>
            <div style="
                color:{TEXT_SECONDARY};
                font-size:0.92rem;
                line-height:1.7;
            ">Architect of the Riyadh V2G Sovereign Digital Twin — a production-scale
            digital twin platform for infrastructure planning, engineering analysis,
            and grid flexibility research. Developed as an independent engineering
            project with a strong emphasis on architecture, reproducibility, and
            software engineering discipline.</div>
            """),
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Section 2: Independent Evidence ──────────────────────
    section_title("Independent Evidence")

    metric_card_row([
        {
            "title": "EU Intellectual Property",
            "value": "BOIP i-DEPOT",
            "subtitle": "#161617",
            "annotation": "Public registration",
        },
        {
            "title": "Research Publication",
            "value": "Zenodo DOI",
            "subtitle":" ",
            "annotation": "Permanent DOI",
        },
        {
            "title": "Architecture Showcase",
            "value": "GitHub",
            "subtitle": " ",
            "annotation": "Public repository",
        },
        {
            "title": "Technical Report",
            "value": "ResearchGate",
            "subtitle": " ",
            "annotation": "Public publication",
        },
    ])

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Section 3: Public Artefacts ──────────────────────────
    section_title("Public Artefacts")

    artefacts = [
        ("📄", "Zenodo Research Publication",
         "Permanent DOI", "10.5281/zenodo.21400746",
         "https://zenodo.org/records/21400746"),
        ("🔒", "BOIP Intellectual Property Registration",
         "Public Registration", "i-DEPOT #161617",
         None),
        ("💻", "GitHub Architecture Showcase",
         "Public Architecture Repository", "github.com/mohamedalwedaa",
         "https://github.com/mohamedalwedaa"),
        ("📊", "ResearchGate Technical Report",
         "Public Research Publication", "ResearchGate",
         "https://www.researchgate.net/publication/400350737_Optimizing_Grid_Resilience_A_Data-Driven_V2G_Framework_for_Riyadh_Vision_2030_Scenarios"),
    ]

    for icon, title, meta_label, meta_value, href in artefacts:
        with st.container(border=True):
            value_html = (
                f"""<a href="{href}" target="_blank" rel="noopener noreferrer" style="
                    color:{PRIMARY};
                    text-decoration:none;
                    font-size:0.88rem;
                    font-weight:500;
                ">{meta_value}</a>"""
                if href
                else f"""<span style="
                    color:{PRIMARY};
                    font-size:0.88rem;
                    font-weight:500;
                ">{meta_value}</span>"""
            )
            st.markdown(
                textwrap.dedent(f"""\
                <div style="
                    display:flex;
                    align-items:flex-start;
                    gap:14px;
                ">
                    <span style="font-size:1.5rem;">{icon}</span>
                    <div style="flex:1;">
                        <div style="
                            color:{TEXT_PRIMARY};
                            font-size:0.95rem;
                            font-weight:600;
                            margin-bottom:4px;
                        ">{title}</div>
                        <div style="
                            color:{TEXT_SECONDARY};
                            font-size:0.82rem;
                            margin-bottom:2px;
                        ">{meta_label}</div>
                        {value_html}
                    </div>
                </div>
                """),
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Section 4: Engineering Philosophy ────────────────────
    section_title("Engineering Philosophy")

    st.markdown(
        textwrap.dedent(f"""\
        <p style="color:{TEXT_PRIMARY};font-size:1rem;line-height:1.7;margin-bottom:16px;">
        This platform was engineered as production software rather than academic
        software. Architectural clarity, deterministic execution, reproducibility,
        testing, and documentation were treated as first-class engineering
        requirements from the beginning.
        </p>
        <p style="color:{TEXT_PRIMARY};font-size:1rem;line-height:1.7;margin-bottom:16px;">
        Every public artefact presented in this portfolio contributes to a
        transparent engineering record while intentionally protecting the
        implementation details that constitute the platform's intellectual property.
        </p>
        """),
        unsafe_allow_html=True,
    )

    # ── Section 5: Transparency ──────────────────────────────
    section_title("Transparency")

    info_callout(
        "This portfolio intentionally demonstrates engineering methodology, "
        "architecture, and professional software practices while excluding "
        "production source code, implementation details, optimisation methods, "
        "calibration data, and proprietary workflows.",
        callout_type="info",
    )

    # ── Footer & Watermark ───────────────────────────────────
    render_footer()
    render_watermark()


main()
