"""Execution Architecture — How every execution tick transforms validated inputs into auditable outputs."""

import json
import pathlib
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
    BACKGROUND,
    BORDER,
    CARD_SPACING,
)


# ═══════════════════════════════════════════════════════════════════
#  Data
# ═══════════════════════════════════════════════════════════════════

@st.cache_data
def _load_trace() -> list[dict]:
    """Load the full synthetic execution trace once."""
    data_path = pathlib.Path("synthetic_data/demo_pipeline.json")
    if not data_path.exists():
        return []
    with open(data_path, encoding="utf-8") as fh:
        return json.load(fh)


# ═══════════════════════════════════════════════════════════════════
#  Stage Catalog
# ═══════════════════════════════════════════════════════════════════

_STAGE_CATALOG = [
    {
        "num": 1,
        "icon": "🌤️",
        "name": "Weather",
        "consumes": ["Time Index", "Weather Dataset"],
        "produces": ["Ambient Temperature"],
        "downstream": ["Mobility", "Grid State", "Thermal Assessment"],
        "output": "43.0 °C",
    },
    {
        "num": 2,
        "icon": "🚗",
        "name": "Mobility",
        "consumes": ["Ambient Temperature", "Vehicle Schedules", "Connection Profiles"],
        "produces": ["Connected Fleet State"],
        "downstream": ["Grid State"],
        "output": "412 Connected EVs",
    },
    {
        "num": 3,
        "icon": "⚡",
        "name": "Grid State",
        "consumes": ["Connected Fleet State", "Baseline Demand", "Weather Adjustment"],
        "produces": ["Transformer Loading", "Node Status"],
        "downstream": ["Decision & Policy"],
        "output": "7 Red Nodes",
    },
    {
        "num": 4,
        "icon": "📋",
        "name": "Decision & Policy",
        "consumes": ["Transformer Loading", "Node Status", "Vehicle Eligibility"],
        "produces": ["Dispatch Decisions"],
        "downstream": ["Thermal Assessment"],
        "output": "1.7 MW V2G Dispatch",
    },
    {
        "num": 5,
        "icon": "🌡️",
        "name": "Thermal Assessment",
        "consumes": ["Transformer Loading", "Dispatch Decisions", "Ambient Temperature"],
        "produces": ["Thermal Conditions"],
        "downstream": ["KPI Aggregation"],
        "output": "All Nodes Within Limits",
    },
    {
        "num": 6,
        "icon": "📊",
        "name": "KPIs",
        "consumes": ["Thermal Conditions", "Grid State", "Dispatch Results"],
        "produces": ["Operational Metrics"],
        "downstream": ["Analytics", "Visualization"],
        "output": "14.3 GW\n59.99 Hz",
    },
]

# Ordered edge labels matching the spec exactly
_EDGE_LABELS = [
    "Ambient Temperature",
    "Connected Fleet State",
    "Transformer Loading",
    "Dispatch Decisions",
    "Thermal Conditions",
    "Aggregated Infrastructure Metrics",
]


# ═══════════════════════════════════════════════════════════════════
#  Section 2 — Mermaid Execution Flow
# ═══════════════════════════════════════════════════════════════════

def _render_mermaid_flow():
    """Render the execution-flow Mermaid diagram with labelled edges."""
    section_title("Execution Flow")

    # Build graph: each edge carries a data-contract label
    nodes = [
        'W["{i}  🌤️  Weather"]',
        'M["{i}  🚗  Mobility"]',
        'G["{i}  ⚡  Grid State"]',
        'D["{i}  📋  Decision & Policy"]',
        'T["{i}  🌡️  Thermal Assessment"]',
        'K["{i}  📊  KPIs"]',
    ]
    node_defs = [n.format(i=i + 1) for i, n in enumerate(nodes)]
    edges = [
        f'W -->|"{_EDGE_LABELS[0]}"| M',
        f'M -->|"{_EDGE_LABELS[1]}"| G',
        f'G -->|"{_EDGE_LABELS[2]}"| D',
        f'D -->|"{_EDGE_LABELS[3]}"| T',
        f'T -->|"{_EDGE_LABELS[4]}"| K',
        f'K -->|"{_EDGE_LABELS[5]}"| OUT["📈  Planners & Operators"]',
    ]

    graph_lines = "\n    ".join(node_defs + edges)

    style_lines = "\n    ".join(
        f'style {n} stroke:{PRIMARY},color:{TEXT_PRIMARY}'
        for n in "WMGDTK"
    )
    style_lines += f'\n    style OUT stroke:{ACCENT},color:{TEXT_PRIMARY}'

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
    {graph_lines}
    {style_lines}
</div>
</body>
</html>"""

    st.components.v1.html(mermaid_html, height=580, scrolling=False)


# ═══════════════════════════════════════════════════════════════════
#  Section 3 — Single Expander
# ═══════════════════════════════════════════════════════════════════

def _render_stage_expander(stage: dict):
    """Render one execution-stage expander with two-column layout."""
    label = f"Stage {stage['num']}  —  {stage['icon']}  {stage['name']}"

    with st.expander(label, expanded=False):
        c_left, c_right = st.columns(2)

        with c_left:
            # Consumes
            st.markdown(
                f'<div style="color:{TEXT_SECONDARY};font-size:0.68rem;'
                f'font-weight:600;text-transform:uppercase;letter-spacing:0.6px;'
                f'margin-bottom:6px;">Consumes</div>',
                unsafe_allow_html=True,
            )
            for item in stage["consumes"]:
                st.markdown(
                    f'<div style="color:{TEXT_PRIMARY};font-size:0.9rem;'
                    f'line-height:1.6;margin-bottom:2px;">• {item}</div>',
                    unsafe_allow_html=True,
                )

            st.markdown("<br>", unsafe_allow_html=True)

            # Produces
            st.markdown(
                f'<div style="color:{TEXT_SECONDARY};font-size:0.68rem;'
                f'font-weight:600;text-transform:uppercase;letter-spacing:0.6px;'
                f'margin-bottom:6px;">Produces</div>',
                unsafe_allow_html=True,
            )
            for item in stage["produces"]:
                st.markdown(
                    f'<div style="color:{SUCCESS};font-size:0.9rem;'
                    f'line-height:1.6;margin-bottom:2px;">• {item}</div>',
                    unsafe_allow_html=True,
                )

        with c_right:
            # Downstream Consumer
            st.markdown(
                f'<div style="color:{TEXT_SECONDARY};font-size:0.68rem;'
                f'font-weight:600;text-transform:uppercase;letter-spacing:0.6px;'
                f'margin-bottom:6px;">Downstream Consumer</div>',
                unsafe_allow_html=True,
            )
            for item in stage["downstream"]:
                st.markdown(
                    f'<div style="color:{ACCENT};font-size:0.9rem;'
                    f'line-height:1.6;margin-bottom:2px;">• {item}</div>',
                    unsafe_allow_html=True,
                )

            st.markdown("<br>", unsafe_allow_html=True)

            # Representative Output
            st.markdown(
                f'<div style="color:{TEXT_SECONDARY};font-size:0.68rem;'
                f'font-weight:600;text-transform:uppercase;letter-spacing:0.6px;'
                f'margin-bottom:6px;">Representative Output</div>',
                unsafe_allow_html=True,
            )
            for line in stage["output"].split("\n"):
                st.markdown(
                    f'<div style="color:{PRIMARY};font-size:0.95rem;'
                    f'font-weight:600;line-height:1.5;margin-bottom:2px;">{line.strip()}</div>',
                    unsafe_allow_html=True,
                )


# ═══════════════════════════════════════════════════════════════════
#  Section 4 — Execution Lifecycle
# ═══════════════════════════════════════════════════════════════════

def _render_lifecycle():
    """Render a vertical execution lifecycle diagram."""
    section_title("Execution Lifecycle")

    lifecycle_steps = [
        "📥  Inputs",
        "↓",
        "⚙️  Execution Tick",
        "↓",
        "✅  Validated Outputs",
        "↓",
        "🗄️  Snapshot Archived",
        "↓",
        "🔄  Next Tick",
    ]

    for i, step in enumerate(lifecycle_steps):
        if step == "↓":
            st.markdown(
                f'<div style="color:{TEXT_SECONDARY};font-size:1.2rem;'
                f'text-align:center;line-height:1.0;padding:2px 0;">▼</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div style="background-color:{CARD_BACKGROUND};'
                f'border:1px solid {BORDER};'
                f'border-radius:8px;padding:14px 24px;text-align:center;'
                f'color:{PRIMARY if i == 2 else TEXT_PRIMARY};'
                f'font-size:0.95rem;font-weight:600;'
                f'margin:0 auto;max-width:340px;">{step}</div>',
                unsafe_allow_html=True,
            )

    st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)

    st.markdown(
        textwrap.dedent(f"""\
        <p style="color:{TEXT_PRIMARY};font-size:0.95rem;line-height:1.7;margin-bottom:16px;">
        Each execution tick produces a complete, reproducible system snapshot.
        The following tick begins from this archived state.
        This design enables replay, rollback, comparison, and forensic analysis.
        </p>
        """),
        unsafe_allow_html=True,
    )


# ═══════════════════════════════════════════════════════════════════
#  Page
# ═══════════════════════════════════════════════════════════════════

def main():
    # ── Page Header ──────────────────────────────────────────
    page_header(
        "Execution Architecture",
        "How every execution tick transforms validated inputs into auditable outputs",
    )

    st.markdown(
        f'<p style="color:{TEXT_SECONDARY};font-size:0.92rem;'
        f'margin:-12px 0 24px 24px;line-height:1.5;">'
        'The Architecture Explorer illustrates six representative execution stages. '
        'The Production Platform extends the same execution contract across '
        '29 specialised stages.'
        '</p>',
        unsafe_allow_html=True,
    )

    # ── Section 1: Execution Contract ────────────────────────
    section_title("Execution Contract")

    # Prominent callout
    st.markdown(
        textwrap.dedent(f"""\
        <div style="
            background-color:rgba(0,180,216,0.06);
            border-left:4px solid {PRIMARY};
            border-radius:6px;
            padding:18px 22px;
            margin:0 0 20px 0;
            color:{TEXT_PRIMARY};
            font-size:0.95rem;
            line-height:1.7;
        ">
            Every execution tick follows exactly the same execution contract.<br>
            Each stage consumes only validated outputs from the previous stage.<br>
            No stage executes out of order.<br>
            No stage accesses downstream state.<br>
            Every output is deterministic, reproducible, and traceable.
        </div>
        """),
        unsafe_allow_html=True,
    )

    # Four principle badges
    _badge_style = (
        f"background-color:{CARD_BACKGROUND};border:1px solid {BORDER};"
        f"border-radius:20px;padding:8px 20px;color:{SUCCESS};"
        f"font-size:0.82rem;font-weight:600;white-space:nowrap;"
        f"display:inline-block;margin-right:10px;margin-bottom:8px;"
    )
    badges_html = "".join(
        f'<span style="{_badge_style}">✓ {p}</span>'
        for p in ["Ordered Execution", "Deterministic", "Auditable", "Replayable"]
    )
    st.markdown(
        f'<div style="margin:0 0 16px 0;">{badges_html}</div>',
        unsafe_allow_html=True,
    )

    # Annotation
    st.markdown(
        f'<div style="color:{TEXT_SECONDARY};font-size:0.78rem;line-height:1.6;">'
        f'<strong style="color:{PRIMARY};">Production Platform:</strong> '
        f'29 execution stages<br>'
        f'<strong style="color:{PRIMARY};">Architecture Explorer:</strong> '
        f'6 representative stages<br>'
        f'Remaining stages belong to protected production workflows.'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

    # ── Section 2: Execution Flow (Mermaid) ──────────────────
    _render_mermaid_flow()

    # ── Section 3: Execution Stages ──────────────────────────
    section_title("Execution Stages")

    for stage in _STAGE_CATALOG:
        _render_stage_expander(stage)

    st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

    # ── Section 4: Execution Lifecycle ───────────────────────
    _render_lifecycle()

    # ── Section 5: Why This Architecture Matters ─────────────
    section_title("Why This Architecture Matters")

    st.markdown(
        textwrap.dedent(f"""\
        <p style="color:{TEXT_PRIMARY};font-size:1rem;line-height:1.7;margin-bottom:16px;">
        The execution architecture is the foundation of platform trustworthiness.
        Because every stage exposes explicit inputs and outputs, every result can
        be traced back through the complete execution chain.
        </p>
        <p style="color:{TEXT_PRIMARY};font-size:1rem;line-height:1.7;margin-bottom:16px;">
        A frequency anomaly can be traced from aggregated KPIs back through thermal
        assessment, operational decisions, grid state, mobility behaviour, and weather
        conditions. Every intermediate output remains reproducible and independently
        verifiable.
        </p>
        <p style="color:{TEXT_PRIMARY};font-size:1rem;line-height:1.7;margin-bottom:16px;">
        The Production Platform applies exactly the same execution contract across
        29 specialised stages. Every stage is independently testable. Every
        interface is explicit. Every execution path is deterministic.
        </p>
        """),
        unsafe_allow_html=True,
    )

    # ── Section 6: Callouts ──────────────────────────────────
    info_callout(
        "The representative outputs displayed on this page originate from a "
        "pre-computed synthetic execution trace. No simulation engine executes "
        "inside the Architecture Explorer. The page illustrates execution "
        "architecture rather than computational capability.",
        callout_type="info",
    )

    info_callout(
        "The complete 29-stage execution architecture—including "
        "protected workflows, operational validation assets, and execution contracts—is "
        "protected intellectual property. This page illustrates the execution contract "
        "using six representative stages from the synthetic demonstrator.",
        callout_type="info",
    )

    # ── Footer & Watermark ───────────────────────────────────
    render_footer()
    render_watermark()


main()
