"""
Shared UI Elements for Riyadh Architecture Explorer.

Reusable Streamlit components used across all pages.
These are architectural demonstration components only.
"""

import html
import textwrap
import uuid

import streamlit as st
from demo_components.constants import (
    WATERMARK_TEXT,
    PRIMARY,
    ACCENT,
    BACKGROUND,
    SUCCESS,
    WARNING,
    CRITICAL,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    CARD_BACKGROUND,
    BORDER,
    CARD_SPACING,
)


# ── Global CSS Variables ─────────────────────────────────────────

def inject_css():
    """Inject shared CSS custom properties once per session.

    Provides ``--rae-*`` design-token variables so that page-level
    inline styles can reference them without repeating hex values.
    Does NOT define any layout classes — visual fidelity is
    preserved through existing inline styles on each page.
    """
    if "_rae_css_injected" in st.session_state:
        return
    st.markdown(
        f"""\
        <style>
        :root {{
            --rae-primary:          {PRIMARY};
            --rae-accent:           {ACCENT};
            --rae-bg:               {BACKGROUND};
            --rae-success:          {SUCCESS};
            --rae-warning:          {WARNING};
            --rae-critical:         {CRITICAL};
            --rae-text:             {TEXT_PRIMARY};
            --rae-text-secondary:   {TEXT_SECONDARY};
            --rae-card-bg:          {CARD_BACKGROUND};
            --rae-border:           {BORDER};
            --rae-radius:           {CARD_SPACING['border_radius']};
            --rae-padding:          {CARD_SPACING['padding']};
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.session_state["_rae_css_injected"] = True


# ── Page Header ─────────────────────────────────────────────────

def page_header(title: str, subtitle: str | None = None):
    """
    Render a styled page title with optional subtitle.

    Uses the design system's primary color for the title accent bar
    and the secondary text color for the subtitle.
    """
    subtitle_html = (
        f'<p style="color: {TEXT_SECONDARY}; font-size: 1.1rem; '
        f'margin: 0; padding: 0;">{subtitle}</p>'
        if subtitle
        else ""
    )
    st.markdown(
        f"""
        <div style="
            border-left: 4px solid {PRIMARY};
            padding: 12px 0 12px 20px;
            margin-bottom: 24px;
        ">
            <h1 style="
                color: {TEXT_PRIMARY};
                font-size: 2rem;
                font-weight: 700;
                margin: 0;
                padding: 0;
            ">{title}</h1>
            {subtitle_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Section Title ───────────────────────────────────────────────

def section_title(text: str):
    """
    Render a consistent section heading with a full-width accent underline.

    The underline spans the entire column width for a clean, professional look.
    """
    st.markdown(
        f"""
        <h2 style="
            color: {TEXT_PRIMARY};
            font-size: 1.35rem;
            font-weight: 600;
            margin: 28px 0 16px 0;
            padding-bottom: 10px;
            border-bottom: 2px solid {ACCENT};
        ">{text}</h2>
        """,
        unsafe_allow_html=True,
    )


# ── Info Callout ────────────────────────────────────────────────

def info_callout(text: str, callout_type: str = "info"):
    """
    Render a colored callout box with context-appropriate styling.

    Args:
        text: The message to display inside the callout.
        callout_type: One of "info", "warning", "success", "protected".
            Determines the border color and icon.
    """
    type_config = {
        "info": {
            "border_color": PRIMARY,
            "bg_color": "rgba(0, 180, 216, 0.08)",
            "icon": "ℹ️",
        },
        "warning": {
            "border_color": WARNING,
            "bg_color": "rgba(243, 156, 18, 0.08)",
            "icon": "⚠️",
        },
        "success": {
            "border_color": SUCCESS,
            "bg_color": "rgba(46, 204, 113, 0.08)",
            "icon": "✅",
        },
        "protected": {
            "border_color": ACCENT,
            "bg_color": "rgba(255, 107, 53, 0.08)",
            "icon": "🔒",
        },
    }

    config = type_config.get(callout_type, type_config["info"])

    st.markdown(
        f"""
        <div style="
            background-color: {config['bg_color']};
            border-left: 4px solid {config['border_color']};
            border-radius: 6px;
            padding: 14px 18px;
            margin: 16px 0;
            color: {TEXT_PRIMARY};
            font-size: 0.95rem;
            line-height: 1.6;
        ">
            <span style="margin-right: 8px;">{config['icon']}</span>
            {text}
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Footer ──────────────────────────────────────────────────────

def render_footer():
    """
    Render a thin footer bar with copyright and disclaimer.

    Displays a consistent footer across all pages, positioned
    above the watermark.
    """
    st.markdown("---")
    st.markdown(
        f"""
        <div style="
            text-align: center;
            color: {TEXT_SECONDARY};
            font-size: 0.7rem;
            opacity: 0.6;
            padding: 8px 0;
            margin-bottom: 8px;
        ">
            © 2026 Mohamed Alwedaa. All rights reserved. | Architecture Explorer — Not the Production Platform
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Watermark ───────────────────────────────────────────────────

def render_watermark():
    """
    Render a persistent semi-transparent mark at the bottom of every page.

    Displays the demo scale disclaimer and production comparison.
    Must be called at the end of every page's main() function.
    """
    st.markdown("---")
    st.markdown(
        f"""
        <div style="
            text-align: center;
            color: {TEXT_SECONDARY};
            font-size: 0.75rem;
            opacity: 0.6;
            padding: 8px 0;
        ">
            {WATERMARK_TEXT}
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Gated Button ────────────────────────────────────────────────

def gated_button(label: str, tooltip_text: str = "Available under NDA"):
    """
    Return a disabled button with a lock icon and tooltip.

    Used to indicate features that exist in the Production Platform
    but cannot be demonstrated in this public portfolio.

    Args:
        label: Button label text.
        tooltip_text: Tooltip shown on hover. Defaults to NDA notice.

    Returns:
        bool: Always False (button is never clickable).
    """
    # Ensure a unique key even if the same label is used in multiple places
    unique_suffix = uuid.uuid4().hex[:6]
    key = f"gated_{label.lower().replace(' ', '_')}_{unique_suffix}"

    disabled = st.button(
        f"🔒 {label}",
        disabled=True,
        help=tooltip_text,
        key=key,
    )
    return False


# ── Metric Cards ────────────────────────────────────────────────

def _build_metric_card_html(
    title: str,
    value,
    subtitle: str | None = None,
    annotation: str | None = None,
) -> str:
    """
    Build an HTML string for a single metric card.

    Designed to be used inside :func:`metric_card_row` which wraps all
    cards in a single flexbox container for equal heights.

    Args:
        title: Metric label (14px, 600 weight, left-aligned).
        value: Primary value (30px, 700 weight, centered).
        subtitle: Optional subtitle below value (13px).
        annotation: Optional small annotation (11px, secondary, 0.75 opacity).

    Returns:
        str: HTML string for the card ``<div>``.
    """
    subtitle_html = (
        f'<div class="metcard-subtitle">{html.escape(subtitle)}</div>'
        if subtitle
        else ""
    )
    annotation_html = (
        f'<div class="metcard-annotation">{html.escape(annotation)}</div>'
        if annotation
        else ""
    )

    return textwrap.dedent(f"""\
    <div class="metcard">
        <div class="metcard-title">{html.escape(title)}</div>
        <div class="metcard-value">{html.escape(str(value))}</div>
        {subtitle_html}
        {annotation_html}
    </div>""")


def metric_card(title: str, value, subtitle: str | None = None, annotation: str | None = None):
    """
    Render a single metric card via :func:`metric_card_row`.

    Convenience wrapper — builds a single-card list and delegates to
    :func:`metric_card_row` so all cards use the same CSS class and
    flexbox layout.

    Args:
        title: Metric label.
        value: Primary value to display.
        subtitle: Optional subtitle below the value.
        annotation: Optional small annotation (e.g., "Demo scale: 97").
    """
    metric_card_row([{"title": title, "value": value, "subtitle": subtitle, "annotation": annotation}])


def metric_card_row(cards: list[dict]):
    """
    Render a row of metric cards using ``st.columns`` for layout.

    Each card is rendered as custom HTML inside its own Streamlit column,
    ensuring a horizontal four-column layout.  All cards share the same
    CSS classes for consistent typography and styling.

    Each dict in *cards* may contain:

    - **title**      (str, required)  — 14px, 600 weight, left-aligned
    - **value**      (str, required)  — 30px, 700 weight, centered
    - **subtitle**   (str, optional)  — 13px, centered
    - **annotation** (str, optional)  — 11px, secondary, 0.75 opacity

    Args:
        cards: List of card definition dicts.

    Returns:
        None (renders inline via ``st.columns`` and ``st.markdown``).
    """
    # Inject CSS once — scoped class names avoid collisions
    st.markdown(
        f"""
        <style>
        .metcard {{
            background-color: {CARD_BACKGROUND};
            border: 1px solid {BORDER};
            border-radius: {CARD_SPACING['border_radius']};
            padding: {CARD_SPACING['padding']};
            box-shadow: 0 1px 3px rgba(0,0,0,0.3);
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            overflow: hidden;
            height: 100%;
            box-sizing: border-box;
        }}
        .metcard-title {{
            color: {TEXT_SECONDARY};
            font-size: 14px;
            font-weight: 600;
            text-align: left;
            margin-bottom: 8px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}
        .metcard-value {{
            color: {TEXT_PRIMARY};
            font-size: 30px;
            font-weight: 700;
            text-align: center;
            margin-bottom: 8px;
            line-height: 1.15;
            word-break: break-word;
        }}
        .metcard-subtitle {{
            color: {TEXT_SECONDARY};
            font-size: 13px;
            text-align: center;
            margin-bottom: 4px;
        }}
        .metcard-annotation {{
            color: {TEXT_SECONDARY};
            font-size: 11px;
            text-align: center;
            opacity: 0.75;
            margin-top: auto;
            padding-top: 4px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(len(cards))
    for col, card in zip(cols, cards):
        html = _build_metric_card_html(
            title=card.get("title", ""),
            value=card.get("value", ""),
            subtitle=card.get("subtitle"),
            annotation=card.get("annotation"),
        )
        with col:
            st.markdown(html, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
#  Architecture Flow Diagram (Mermaid — kept from refactor)
# ═══════════════════════════════════════════════════════════════════

def render_architecture_flow():
    """Render the layer-interaction flow diagram using Mermaid.

    Uses ``st.components.v1.html`` to embed a Mermaid graph showing
    the main execution flow (Computational Core → Orchestration →
    Decision & Policy → Analytics & Audit → Visualization & Control)
    with the Data Pipeline (Data Generation → Integration Layer)
    feeding into the Orchestration Engine.

    This replaces the previous HTML-flexbox flow diagram.  Mermaid
    provides a cleaner, more maintainable directed-graph layout
    without any HTML flexbox.
    """
    section_title("Layer Interaction")

    mermaid_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>
    mermaid.initialize({{
        startOnLoad: true,
        theme: 'dark',
        themeVariables: {{
            primaryColor: '{CARD_BACKGROUND}',
            primaryTextColor: '{TEXT_PRIMARY}',
            primaryBorderColor: '{PRIMARY}',
            lineColor: '{TEXT_SECONDARY}',
            secondaryColor: '{CARD_BACKGROUND}',
            tertiaryColor: '{CARD_BACKGROUND}',
            fontFamily: 'system-ui, -apple-system, sans-serif',
        }}
    }});
</script>
<style>
    body {{
        margin: 0;
        padding: 0;
        background-color: {BACKGROUND};
        display: flex;
        justify-content: center;
    }}
    .mermaid {{
        margin: 0 auto;
    }}
</style>
</head>
<body>
<div class="mermaid">
graph TD
    CC["⚙️  Computational Core"] --> OE["🎛️  Orchestration Engine"]
    DG["📡  Data Generation"] --> IL["🔗  Integration Layer"]
    IL --> OE
    OE --> DP["📋  Decision & Policy"]
    DP --> AA["📊  Analytics & Audit"]
    AA --> VC["🖥️  Visualization & Control"]

    style CC stroke:{PRIMARY},color:{TEXT_PRIMARY}
    style OE stroke:{PRIMARY},color:{TEXT_PRIMARY}
    style DG stroke:{ACCENT},color:{TEXT_PRIMARY}
    style IL stroke:{ACCENT},color:{TEXT_PRIMARY}
    style DP stroke:{PRIMARY},color:{TEXT_PRIMARY}
    style AA stroke:{PRIMARY},color:{TEXT_PRIMARY}
    style VC stroke:{PRIMARY},color:{TEXT_PRIMARY}
</div>
</body>
</html>"""

    st.components.v1.html(mermaid_html, height=460, scrolling=False)
