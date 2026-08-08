"""Production Scale — Demo vs. production capacity comparison."""

import textwrap

import streamlit as st
from demo_components.ui_elements import (
    page_header,
    section_title,
    info_callout,
    gated_button,
    render_footer,
    render_watermark,
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
        "Scale Comparison",
        "Architecture Explorer vs Production Platform",
    )

    # ── Section 1: Infrastructure at Scale ───────────────────
    section_title("Infrastructure at Scale")

    comparison_rows = [
        ("Distribution Transformers", "97", "60,000"),
        ("Electric Vehicles", "512", "1,000,000"),
        ("Processing Pipeline", "6 stages", "29 stages"),
        ("Weather Dataset", "Synthetic Profile", "Annual Operational Dataset"),
        ("Geographic Coverage", "4 Demonstration Zones", "~15 Municipal Areas"),
        ("Grid Representation", "Simplified", "Municipal Distribution Network"),
    ]

    rows_html = ""
    for metric, explorer, full_scale in comparison_rows:
        rows_html += f"""
        <tr>
            <td class="scale-metric">{metric}</td>
            <td class="scale-explorer">{explorer}</td>
            <td class="scale-full">{full_scale}</td>
        </tr>"""

    st.markdown(
        textwrap.dedent(f"""\
        <style>
        .scale-table {{
            width: 100%;
            border-collapse: separate;
            border-spacing: 0 10px;
            margin: 8px 0 24px 0;
        }}
        .scale-table th {{
            color: {TEXT_SECONDARY};
            font-size: 0.72rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            padding: 0 16px 8px 16px;
            text-align: left;
        }}
        .scale-table td {{
            padding: 14px 16px;
            background-color: {CARD_BACKGROUND};
            border: 1px solid {BORDER};
            border-radius: 6px;
            font-size: 0.92rem;
        }}
        .scale-metric {{
            color: {TEXT_SECONDARY};
            font-weight: 500;
            width: 35%;
        }}
        .scale-explorer {{
            color: {TEXT_PRIMARY};
            font-weight: 600;
            width: 32.5%;
        }}
        .scale-full {{
            color: {PRIMARY};
            font-weight: 700;
            width: 32.5%;
        }}
        </style>
        <table class="scale-table">
            <thead>
                <tr>
                    <th>Metric</th>
                    <th>Architecture Explorer</th>
                    <th>Production Platform</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
        """),
        unsafe_allow_html=True,
    )

    # ── Section 2: Engineering Characteristics ───────────────
    section_title("Engineering Characteristics")

    characteristics = [
        "📐  Scalable Architecture",
        "🧩  Modular Design",
        "🎯  Deterministic Execution",
        "📊  Operational Analytics",
        "🏗  Infrastructure Planning",
        "🧠  Decision Support",
    ]

    for char in characteristics:
        left, _, right = st.columns([3, 1, 2])
        with left:
            st.markdown(
                f'<span style="color: {TEXT_PRIMARY}; font-size: 1rem; '
                f'line-height: 2.4;">{char}</span>',
                unsafe_allow_html=True,
            )
        with right:
            gated_button("Available in Full Platform")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Section 3: Why Scale Matters ─────────────────────────
    section_title("Why Scale Matters")

    st.markdown(
        textwrap.dedent(f"""\
        <p style="color: {TEXT_PRIMARY}; font-size: 1rem; line-height: 1.7; margin-bottom: 16px;">
        The Architecture Explorer demonstrates the engineering approach and software architecture.
        </p>
        <p style="color: {TEXT_PRIMARY}; font-size: 1rem; line-height: 1.7; margin-bottom: 16px;">
        The complete platform was designed for sovereign-scale infrastructure.
        </p>
        <p style="color: {TEXT_PRIMARY}; font-size: 1rem; line-height: 1.7; margin-bottom: 16px;">
        At this scale, engineering challenges become fundamentally different and cannot be
        represented inside a lightweight public demonstrator.
        </p>
        <p style="color: {TEXT_PRIMARY}; font-size: 1rem; line-height: 1.7; margin-bottom: 16px;">
        Managing millions of distributed assets, representing real-world operational
        constraints, and maintaining deterministic reproducibility at city scale require
        architectural decisions that a small demonstrator cannot realistically capture.
        </p>
        """),
        unsafe_allow_html=True,
    )

    # ── Section 4: Scale Reduction ───────────────────────────
    section_title("Scale Reduction")

    st.markdown(
        textwrap.dedent(f"""\
        <p style="color: {TEXT_PRIMARY}; font-size: 1rem; line-height: 1.7; margin-bottom: 16px;">
        The public Architecture Explorer uses a substantially reduced demonstrator
        scale while preserving the architectural organization and engineering workflow.
        </p>
        """),
        unsafe_allow_html=True,
    )

    # ── Section 5: Protected Platform ────────────────────────
    info_callout(
        "The public Architecture Explorer illustrates software architecture and "
        "engineering practices only. The complete Production Platform—including "
        "protected workflows, validation assets, and implementation details—is "
        "protected intellectual property.",
        callout_type="info",
    )

    # ── Footer & Watermark ───────────────────────────────────
    render_footer()
    render_watermark()


main()
