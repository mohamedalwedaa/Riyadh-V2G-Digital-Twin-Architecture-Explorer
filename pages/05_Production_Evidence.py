"""Production Evidence — Public artefacts and measurable engineering indicators."""

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
    CARD_SPACING,
)


# ═══════════════════════════════════════════════════════════════════
#  Section 3 — Engineering Practices 2×2 grid
# ═══════════════════════════════════════════════════════════════════

def _render_practice_card(icon: str, title: str, body: str):
    """Return an HTML string for a single engineering-practice card."""
    return textwrap.dedent(f"""\
    <div style="
        background-color:{CARD_BACKGROUND};
        border:1px solid {BORDER};
        border-radius:{CARD_SPACING['border_radius']};
        padding:24px 22px;
        height:100%;
        box-sizing:border-box;
    ">
        <div style="font-size:1.4rem;margin-bottom:12px;">{icon}</div>
        <div style="
            color:{PRIMARY};
            font-size:1rem;
            font-weight:700;
            margin-bottom:10px;
            line-height:1.3;
        ">{title}</div>
        <div style="
            color:{TEXT_SECONDARY};
            font-size:0.88rem;
            line-height:1.6;
        ">{body}</div>
    </div>
    """)


# ═══════════════════════════════════════════════════════════════════
#  Section 4 — Public Artefacts table
# ═══════════════════════════════════════════════════════════════════

def _render_artefacts_table(rows: list[tuple[str, str]]):
    """Render a simple artefacts verification table."""
    tbody = ""
    for artefact, verification in rows:
        tbody += f"""<tr>
            <td style="
                color:{TEXT_PRIMARY};
                padding:12px 16px;
                background-color:{CARD_BACKGROUND};
                border:1px solid {BORDER};
                border-radius:6px;
                font-size:0.92rem;
                font-weight:500;
                width:50%;
            ">{artefact}</td>
            <td style="
                color:{PRIMARY};
                padding:12px 16px;
                background-color:{CARD_BACKGROUND};
                border:1px solid {BORDER};
                border-radius:6px;
                font-size:0.92rem;
                font-weight:600;
                width:50%;
            ">{verification}</td>
        </tr>"""

    st.markdown(
        f"""<table style="
            width:100%;
            border-collapse:separate;
            border-spacing:0 8px;
            margin:8px 0 24px 0;
        ">{tbody}</table>""",
        unsafe_allow_html=True,
    )


# ═══════════════════════════════════════════════════════════════════
#  Page
# ═══════════════════════════════════════════════════════════════════

def main():
    # ── Page Header ──────────────────────────────────────────
    page_header(
        "Production Evidence",
        "Public artefacts and measurable engineering indicators",
    )

    st.markdown(
        f'<p style="color:{TEXT_SECONDARY};font-size:0.92rem;'
        f'margin:-12px 0 24px 24px;line-height:1.5;">'
        'Every indicator shown on this page references a publicly verifiable '
        'artefact or a measurable engineering metric. No proprietary '
        'implementation details are disclosed.'
        '</p>',
        unsafe_allow_html=True,
    )

    # ── Section 1: Codebase Overview ─────────────────────────
    section_title("Codebase Overview")

    metric_card_row([
        {
            "title": "Engineering Modules",
            "value": "180+",
            "subtitle": " ",
            "annotation": "Repository-derived metric",
        },
        {
            "title": "Lines of Code",
            "value": "42,000+",
            "subtitle": " ",
            "annotation": "Repository-derived metric",
        },
        {
            "title": "Automated Tests",
            "value": "60+",
            "subtitle": " ",
            "annotation": "Repository-derived metric",
        },
        {
            "title": "Public Artefacts",
            "value": "4",
            "subtitle": " ",
            "annotation": "Defined architectural layers",
        },
    ])

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Section 2: Intellectual Property ─────────────────────
    section_title("Intellectual Property")

    metric_card_row([
        {
            "title": "EU IP Registration",
            "value": "BOIP i-DEPOT",
            "subtitle": "#161617",
            "annotation": "Public registration record",
        },
        {
            "title": "Research Publication",
            "value": "Zenodo DOI",
            "subtitle": " ",
            "annotation": "10.5281/zenodo.21400746",
        },
    ])

    st.markdown(
        textwrap.dedent(f"""\
        <p style="color:{TEXT_PRIMARY};font-size:1rem;line-height:1.7;margin-bottom:16px;">
        The platform architecture is protected through formal intellectual property
        registration, while the underlying research framework is archived through a
        permanent DOI. Together, these artefacts establish authorship, provide long-term
        traceability, and enable independent citation without exposing proprietary
        implementation details.
        </p>
        """),
        unsafe_allow_html=True,
    )

    # ── Section 3: Engineering Practices ─────────────────────
    section_title("Engineering Practices")

    practices = [
        ("🎯", "Deterministic Execution",
         "Every execution follows a fixed sequence of validated stages. Identical "
         "inputs always produce identical outputs, enabling reproducibility, "
         "auditing, and reliable scenario comparison."),
        ("🧱", "Layered Architecture",
         "Strict separation between computational logic, orchestration, analytics, "
         "and presentation allows each layer to evolve independently while preserving "
         "system stability."),
        ("📐", "Production-Scale Design",
         "The computational architecture is designed for large-scale infrastructure "
         "modelling through efficient data-oriented processing and disciplined "
         "execution contracts."),
        ("📋", "Audit Trail",
         "The architecture supports reproducible execution records designed for "
         "traceability, allowing scenarios to be reproduced, compared, and "
         "independently reviewed."),
    ]

    # Row 1
    cols = st.columns(2)
    for col, (icon, title, body) in zip(cols, practices[0:2]):
        with col:
            st.markdown(
                _render_practice_card(icon, title, body),
                unsafe_allow_html=True,
            )

    st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)

    # Row 2
    cols = st.columns(2)
    for col, (icon, title, body) in zip(cols, practices[2:4]):
        with col:
            st.markdown(
                _render_practice_card(icon, title, body),
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Section 4: Public Artefacts ──────────────────────────
    section_title("Public Artefacts")

    _render_artefacts_table([
        ("Zenodo Research Publication", "Permanent DOI"),
        ("BOIP Intellectual Property Registration", "Public Registration"),
        ("GitHub Architecture Showcase", "Public Repository"),
        ("ResearchGate Technical Report", "Public Publication"),
    ])

    # ── Section 5: Independent Verification ──────────────────
    section_title("Independent Verification")

    verification_items = [
        "Intellectual Property Registration",
        "Permanent Research DOI",
        "Public Architecture Repository",
        "Public Technical Publication",
    ]

    for item in verification_items:
        st.markdown(
            f'<div style="color:{SUCCESS};font-size:0.95rem;'
            f'line-height:2.0;font-weight:500;">✓ {item}</div>',
            unsafe_allow_html=True,
        )

    st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)

    st.markdown(
        textwrap.dedent(f"""\
        <p style="color:{TEXT_PRIMARY};font-size:1rem;line-height:1.7;margin-bottom:16px;">
        Each artefact can be independently verified without access to the Production
        Platform or its proprietary implementation.
        </p>
        """),
        unsafe_allow_html=True,
    )

    # ── Section 6: Interpreting the Evidence ─────────────────
    section_title("Interpreting the Evidence")

    st.markdown(
        textwrap.dedent(f"""\
        <p style="color:{TEXT_PRIMARY};font-size:1rem;line-height:1.7;margin-bottom:16px;">
        Taken together, these artefacts demonstrate that the platform has been developed
        using professional engineering practices, documented through formal research
        outputs, and protected as intellectual property.
        </p>
        <p style="color:{TEXT_PRIMARY};font-size:1rem;line-height:1.7;margin-bottom:16px;">
        The evidence is independently verifiable. Public registrations establish
        authorship, research publications provide permanent references, and
        repository-derived metrics demonstrate the scale and maturity of the
        engineering effort without revealing proprietary implementation.
        </p>
        """),
        unsafe_allow_html=True,
    )

    # ── Section 7: Protected Implementation ──────────────────
    section_title("Protected Implementation")

    st.markdown(
        textwrap.dedent(f"""\
        <p style="color:{TEXT_PRIMARY};font-size:1rem;line-height:1.7;margin-bottom:16px;">
        This portfolio intentionally does not expose source code, algorithms,
        calibration datasets, optimisation strategies, production configuration,
        or implementation details. These remain protected intellectual property
        and are available only through private technical demonstrations under NDA.
        </p>
        """),
        unsafe_allow_html=True,
    )

    # ── Section 8: Callout ───────────────────────────────────
    info_callout(
        "A private technical demonstration of the complete production platform "
        "— including live execution, architecture walkthrough, engineering discussion, "
        "and implementation review — is available under NDA.",
        callout_type="protected",
    )

    # ── Footer & Watermark ───────────────────────────────────
    render_footer()
    render_watermark()


main()
