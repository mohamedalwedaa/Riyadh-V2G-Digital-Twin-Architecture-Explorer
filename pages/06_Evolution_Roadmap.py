"""Evolution Roadmap — The engineering journey from concept to production-grade platform."""

import textwrap

import streamlit as st
from demo_components.ui_elements import (
    page_header,
    section_title,
    info_callout,
    render_footer,
    render_watermark,
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
#  Phase Data
# ═══════════════════════════════════════════════════════════════════

PHASES = [
    {
        "icon": "🔬",
        "title": "Research",
        "question": "What problem should this platform solve?",
        "outcomes": [
            "Investigated infrastructure planning challenges",
            "Studied digital twin methodologies",
            "Defined the system vision",
            "Established engineering objectives",
        ],
    },
    {
        "icon": "🏗️",
        "title": "Architecture",
        "question": "How should the platform be designed?",
        "outcomes": [
            "Layered architecture",
            "Modular execution model",
            "Separation of concerns",
            "Deterministic execution principles",
        ],
    },
    {
        "icon": "⚙️",
        "title": "Engineering",
        "question": "How was the architecture transformed into software?",
        "outcomes": [
            "Engineering codebase",
            "Execution engine",
            "Technical documentation",
            "Automated testing framework",
        ],
    },
    {
        "icon": "✅",
        "title": "Validation",
        "question": "How was correctness demonstrated?",
        "outcomes": [
            "Synthetic demonstrator",
            "Architecture Explorer",
            "Repeatable execution",
            "Performance verification",
        ],
    },
    {
        "icon": "🌍",
        "title": "Publication",
        "question": "How was the work shared publicly?",
        "outcomes": [
            "Zenodo publication",
            "GitHub architecture showcase",
            "ResearchGate report",
            "Public technical artefacts",
        ],
    },
    {
        "icon": "🔒",
        "title": "Protection",
        "question": "How was the intellectual property protected?",
        "outcomes": [
            "BOIP i-DEPOT registration",
            "Formal authorship record",
            "Protected engineering assets",
            "NDA technical demonstrations",
        ],
    },
]


# ═══════════════════════════════════════════════════════════════════
#  Phase Card Renderer
# ═══════════════════════════════════════════════════════════════════

def _render_phase_card(phase: dict, index: int):
    """Render a single engineering phase card inside st.container(border=True)."""
    with st.container(border=True):
        # Phase badge row
        st.markdown(
            textwrap.dedent(f"""\
            <div style="
                display:flex;
                align-items:center;
                gap:12px;
                margin-bottom:14px;
            ">
                <span style="
                    background-color:{PRIMARY};
                    color:#0D1117;
                    font-size:0.75rem;
                    font-weight:700;
                    padding:3px 10px;
                    border-radius:4px;
                ">Phase {index + 1}</span>
                <span style="
                    color:{PRIMARY};
                    font-size:1.3rem;
                ">{phase['icon']}</span>
                <span style="
                    color:{TEXT_PRIMARY};
                    font-size:1.15rem;
                    font-weight:700;
                ">{phase['title']}</span>
            </div>
            """),
            unsafe_allow_html=True,
        )

        # Guiding question
        st.markdown(
            f'<div style="'
            f'color:{TEXT_SECONDARY};'
            f'font-size:0.82rem;'
            f'font-weight:600;'
            f'text-transform:uppercase;'
            f'letter-spacing:0.5px;'
            f'margin-bottom:6px;'
            f'">Guiding Question</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div style="'
            f'color:{TEXT_PRIMARY};'
            f'font-size:0.95rem;'
            f'font-weight:500;'
            f'font-style:italic;'
            f'line-height:1.5;'
            f'margin-bottom:14px;'
            f'">"{phase["question"]}"</div>',
            unsafe_allow_html=True,
        )

        # Outcome bullets
        st.markdown(
            f'<div style="'
            f'color:{TEXT_SECONDARY};'
            f'font-size:0.82rem;'
            f'font-weight:600;'
            f'text-transform:uppercase;'
            f'letter-spacing:0.5px;'
            f'margin-bottom:6px;'
            f'">Outcomes</div>',
            unsafe_allow_html=True,
        )
        for outcome in phase["outcomes"]:
            st.markdown(
                f'<div style="'
                f'color:{TEXT_PRIMARY};'
                f'font-size:0.9rem;'
                f'line-height:1.8;'
                f'padding-left:8px;'
                f'">• {outcome}</div>',
                unsafe_allow_html=True,
            )


def _render_arrow():
    """Render a centred downward arrow between phase cards."""
    st.markdown(
        f'<div style="'
        f'text-align:center;'
        f'color:{ACCENT};'
        f'font-size:1.4rem;'
        f'margin:6px 0;'
        f'">↓</div>',
        unsafe_allow_html=True,
    )


# ═══════════════════════════════════════════════════════════════════
#  Page
# ═══════════════════════════════════════════════════════════════════

def main():
    # ── Page Header ──────────────────────────────────────────
    page_header(
        "Evolution Roadmap",
        "The engineering journey from concept to production-grade platform",
    )

    st.markdown(
        f'<p style="color:{TEXT_SECONDARY};font-size:0.92rem;'
        f'margin:-12px 0 24px 24px;line-height:1.5;">'
        'The Riyadh V2G Sovereign Digital Twin evolved through a series of '
        'structured engineering phases. Each phase introduced new architectural '
        'capabilities, increased technical maturity, and produced independently '
        'verifiable artefacts.'
        '</p>',
        unsafe_allow_html=True,
    )

    # ── Section 1: Engineering Evolution ─────────────────────
    section_title("Engineering Evolution")

    for i, phase in enumerate(PHASES):
        _render_phase_card(phase, i)
        if i < len(PHASES) - 1:
            _render_arrow()

    st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)

    # ── Section 2: Platform Today ────────────────────────────
    section_title("Platform Today")

    with st.container(border=True):
        st.markdown(
            textwrap.dedent(f"""\
            <div style="
                font-size:1.3rem;
                font-weight:700;
                color:{TEXT_PRIMARY};
                margin-bottom:18px;
                text-align:center;
            ">Riyadh V2G Sovereign Digital Twin</div>
            """),
            unsafe_allow_html=True,
        )

        achievements = [
            "Production-scale architecture",
            "Published research",
            "Protected intellectual property",
            "Public architecture showcase",
            "Verifiable engineering evidence",
        ]

        for achievement in achievements:
            st.markdown(
                f'<div style="'
                f'color:{SUCCESS};'
                f'font-size:0.95rem;'
                f'line-height:2.0;'
                f'font-weight:500;'
                f'text-align:center;'
                f'">✔ {achievement}</div>',
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Section 3: Why This Matters ──────────────────────────
    section_title("Why This Matters")

    st.markdown(
        textwrap.dedent(f"""\
        <p style="color:{TEXT_PRIMARY};font-size:1rem;line-height:1.7;margin-bottom:16px;">
        This roadmap demonstrates a disciplined engineering process rather than
        isolated software development. Each phase built upon the previous one,
        progressively increasing architectural maturity while producing
        independently verifiable outcomes.
        </p>
        <p style="color:{TEXT_PRIMARY};font-size:1rem;line-height:1.7;margin-bottom:16px;">
        Research established the direction. Architecture defined the structure.
        Engineering transformed the design into software. Validation demonstrated
        correctness. Publication provided public transparency. Protection secured
        the resulting intellectual property.
        </p>
        """),
        unsafe_allow_html=True,
    )

    # ── Section 4: Public Evidence ───────────────────────────
    section_title("Public Evidence")

    info_callout(
        "Every milestone shown on this page is supported by independently "
        "verifiable artefacts, including public publications, intellectual "
        "property registration, and architecture documentation.",
        callout_type="info",
    )

    # ── Footer & Watermark ───────────────────────────────────
    render_footer()
    render_watermark()


main()
