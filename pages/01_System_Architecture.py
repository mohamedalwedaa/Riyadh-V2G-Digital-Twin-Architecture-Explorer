"""System Architecture — Seven-layer modular architecture with strict separation of concerns."""

import textwrap

import streamlit as st
from demo_components.ui_elements import (
    page_header,
    section_title,
    info_callout,
    render_footer,
    render_watermark,
    render_architecture_flow,
)
from demo_components.constants import (
    PRIMARY,
    ACCENT,
    SUCCESS,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    CARD_BACKGROUND,
    BORDER,
    CARD_SPACING,
)


# ── Architecture Card Builder ────────────────────────────────────

def _arch_card(icon: str, title: str, lines: list[str]) -> str:
    """Return a single architecture-layer card as an HTML string.

    All style attributes are collapsed to single lines so the Streamlit
    Markdown parser recognises every <div> tag immediately.
    """
    desc_html = "".join(
        f'<div style="color:{TEXT_SECONDARY};font-size:0.85rem;'
        f'line-height:1.55;margin-bottom:4px;">{line}</div>'
        for line in lines
    )
    return textwrap.dedent(f"""\
    <div style="background-color:{CARD_BACKGROUND};border:1px solid {BORDER};border-radius:10px;padding:28px 24px 24px 24px;display:flex;flex-direction:column;align-items:flex-start;height:100%;box-sizing:border-box;">
        <div style="font-size:1.5rem;margin-bottom:14px;">{icon}</div>
        <div style="color:{TEXT_PRIMARY};font-size:1.05rem;font-weight:700;margin-bottom:12px;line-height:1.3;">{title}</div>
        {desc_html}
    </div>
    """)


def main():
    # ── Page Header ──────────────────────────────────────────────
    page_header(
        "System Architecture",
        "Seven-layer modular architecture with strict separation of concerns",
    )

    # ── Section 1: Platform Architecture ─────────────────────────
    section_title("Platform Architecture")

    layers = [
        ("⚙️", "Computational Core", [
            "Physical and mathematical computation.",
            "Owns the domain logic.",
            "Independent from presentation.",
        ]),
        ("🎛️", "Orchestration Engine", [
            "Coordinates execution order.",
            "Manages deterministic workflow.",
            "Never owns business rules.",
        ]),
        ("📡", "Data Generation", [
            "Creates synthetic infrastructure.",
            "Generates demonstrator datasets.",
            "Provides versioned inputs.",
        ]),
        ("📋", "Decision & Policy", [
            "Applies operational rules.",
            "Produces decision outputs.",
            "Independent from computation.",
        ]),
        ("🔗", "Integration Layer", [
            "Boundary between platform and external consumers.",
            "Coordinates information exchange.",
            "No business ownership.",
        ]),
        ("📊", "Analytics & Audit", [
            "Produces reporting.",
            "Supports governance.",
            "Provides traceability.",
        ]),
        ("🖥️", "Visualization & Control", [
            "Presents information.",
            "Never owns computational logic.",
            "Consumes structured outputs only.",
        ]),
    ]

    # Row 1: 3 cards
    cols = st.columns(3)
    for col, (icon, title, lines) in zip(cols, layers[0:3]):
        with col:
            st.markdown(_arch_card(icon, title, lines), unsafe_allow_html=True)

    st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

    # Row 2: 2 cards (centered using 1-2-1 column trick)
    _, c1, c2, _ = st.columns([1, 4, 4, 1])
    for col, (icon, title, lines) in zip([c1, c2], layers[3:5]):
        with col:
            st.markdown(_arch_card(icon, title, lines), unsafe_allow_html=True)

    st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

    # Row 3: 2 cards
    _, c1, c2, _ = st.columns([1, 4, 4, 1])
    for col, (icon, title, lines) in zip([c1, c2], layers[5:7]):
        with col:
            st.markdown(_arch_card(icon, title, lines), unsafe_allow_html=True)

    st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

    # ── Section 2: Layer Interaction (Mermaid diagram) ───────────
    render_architecture_flow()

    st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

    # ── Section 3: Architectural Principles ──────────────────────
    section_title("Architectural Principles")

    principles = [
        ("🔒", "Strict Layer Separation",
         "No layer depends on presentation. Dependencies always point downward."),
        ("🎯", "Deterministic Execution",
         "Identical inputs produce identical outputs, enabling reproducibility and auditability."),
        ("🧩", "Stable Interfaces",
         "Architectural boundaries remain stable, allowing components to evolve independently."),
    ]

    _princ_icon_style = f"font-size:1.6rem;margin-bottom:12px;"
    _princ_title_style = (
        f"color:{TEXT_PRIMARY};font-size:1rem;font-weight:700;"
        f"margin-bottom:10px;line-height:1.3;"
    )
    _princ_body_style = (
        f"color:{TEXT_SECONDARY};font-size:0.88rem;line-height:1.6;"
    )
    _princ_card_style = (
        f"background-color:{CARD_BACKGROUND};border:1px solid {BORDER};"
        f"border-radius:10px;padding:28px 24px;height:100%;box-sizing:border-box;"
    )

    pcols = st.columns(3)
    for col, (icon, title, desc) in zip(pcols, principles):
        with col:
            st.markdown(
                textwrap.dedent(f"""\
                <div style="{_princ_card_style}">
                    <div style="{_princ_icon_style}">{icon}</div>
                    <div style="{_princ_title_style}">{title}</div>
                    <div style="{_princ_body_style}">{desc}</div>
                </div>
                """),
                unsafe_allow_html=True,
            )

    st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

    # ── Section 4: Why This Architecture ─────────────────────────
    section_title("Why This Architecture")

    st.markdown(
        textwrap.dedent(f"""\
        <p style="color:{TEXT_PRIMARY};font-size:1rem;line-height:1.7;margin-bottom:16px;">
        This architecture was designed so that individual domains can evolve
        independently without introducing cascading changes across the platform.
        </p>
        <p style="color:{TEXT_PRIMARY};font-size:1rem;line-height:1.7;margin-bottom:16px;">
        Clear boundaries between computation, orchestration, analytics and
        presentation make the platform maintainable, testable and scalable
        over long development lifecycles.
        </p>
        """),
        unsafe_allow_html=True,
    )

    # ── Section 5: Scale Context ─────────────────────────────────
    info_callout(
        "This Architecture Explorer represents the full-scale architecture "
        "at demonstrator scale (97 transformers, 512 EVs). The full-scale "
        "platform applies the same architectural principles to significantly "
        "larger infrastructure models.",
        callout_type="info",
    )

    # ── Section 6: Protected Implementation ──────────────────────
    info_callout(
        "The detailed implementation of each architectural layer — including "
        "execution workflow, internal models and full platform components — is "
        "protected intellectual property. The Architecture Explorer illustrates "
        "the structural organisation without exposing implementation details.",
        callout_type="info",
    )

    # ── Footer & Watermark ───────────────────────────────────────
    render_footer()
    render_watermark()


main()
