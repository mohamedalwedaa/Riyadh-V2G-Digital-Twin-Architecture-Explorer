"""Engineering Decisions — Key architectural choices and rationale."""

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
    CARD_SPACING,
)


def main():
    # ── Page Header ──────────────────────────────────────────
    page_header(
        "Engineering Decisions",
        "Architectural reasoning behind the platform design.",
    )

    # ── Section 1: Design Philosophy ─────────────────────────
    section_title("Design Philosophy")

    st.markdown(
        textwrap.dedent(f"""\
        <p style="color: {TEXT_PRIMARY}; font-size: 1rem; line-height: 1.7; margin-bottom: 12px;">
        The platform is designed to evolve as regulations, markets, infrastructure,
        and operational requirements evolve. Rather than building a monolithic system
        that hard-codes today's assumptions, each engineering concern is intentionally
        isolated so it can adapt independently without destabilising the whole.
        </p>
        <p style="color: {TEXT_PRIMARY}; font-size: 1rem; line-height: 1.7; margin-bottom: 16px;">
        This principle — <strong style="color: {PRIMARY};">separate what changes for different
        reasons</strong> — is the foundation of every architectural decision documented below.
        When one subsystem must adapt to a new regulation, a new data source, or a new
        operational constraint, the rest of the platform remains stable and unchanged.
        </p>
        """),
        unsafe_allow_html=True,
    )

    # ── Section 2: Designed for Adaptation ────────────────────
    section_title("Designed for Adaptation")

    st.markdown(
        textwrap.dedent(f"""\
        <p style="color: {TEXT_PRIMARY}; font-size: 1rem; line-height: 1.7; margin-bottom: 16px;">
        The Riyadh implementation provides the initial operating context, not a
        permanent architectural constraint. Regional and domain-specific assumptions
        — including market structure, regulatory requirements, infrastructure
        characteristics, weather conditions, and mobility behaviour — are
        deliberately separated from the core execution architecture.
        </p>
        <p style="color: {TEXT_PRIMARY}; font-size: 1rem; line-height: 1.7; margin-bottom: 16px;">
        This allows the architectural framework to be adapted to a different
        operating environment by replacing or extending the relevant domain
        assumptions and interfaces, while preserving the underlying architectural
        structure.
        </p>
        <p style="color: {TEXT_PRIMARY}; font-size: 1rem; line-height: 1.7; margin-bottom: 16px;">
        A new geography would still require domain-specific data, validation,
        calibration, and regulatory modelling. The architectural objective is not
        to make those differences disappear, but to prevent them from being embedded
        throughout the entire system.
        </p>
        <p style="color: {TEXT_PRIMARY}; font-size: 1rem; line-height: 1.7; margin-bottom: 16px;">
        This separation is a deliberate architectural property: the platform is
        designed around stable interfaces and replaceable domain assumptions rather
        than embedding one geography's operating conditions throughout the system.
        </p>
        """),
        unsafe_allow_html=True,
    )

    # ── Section 3: Key Engineering Decisions ─────────────────
    section_title("Key Engineering Decisions")

    decisions = [
        {
            "title": "Modular Architecture",
            "context": (
                "A platform serving multiple stakeholders — operators, planners, "
                "regulators, and analysts — with overlapping but distinct requirements "
                "creates natural tension between feature velocity and system stability."
            ),
            "decision": (
                "Decompose the system into independently deployable functional units, "
                "each owning a well-defined domain responsibility. Units communicate "
                "through explicit contracts, not shared state or implicit coupling."
            ),
            "why": (
                "When a regulatory change affects only one domain — say, reporting "
                "formats — the change stays confined to that unit. Other domains "
                "continue operating without modification, regression testing, or risk."
            ),
            "benefit": (
                "Independent deployability, isolated failure domains, parallel team "
                "development, and the ability to evolve each unit's internal design "
                "without coordinating across the entire platform."
            ),
        },
        {
            "title": "Deterministic Reproducibility",
            "context": (
                "Infrastructure decisions carry financial, operational, and regulatory "
                "consequences. Stakeholders require the ability to trace any result "
                "back to its exact inputs, parameters, and execution path."
            ),
            "decision": (
                "Design every computational pathway to produce identical outputs given "
                "identical inputs, regardless of when or where execution occurs. "
                "Eliminate all sources of non-determinism: random seeds are fixed, "
                "ordering dependencies are explicit, and external state is versioned."
            ),
            "why": (
                "Non-reproducible results erode trust. If two analysts run the same "
                "scenario and get different answers, the platform loses all credibility. "
                "Determinism transforms computation from a black box into an auditable "
                "engineering artifact."
            ),
            "benefit": (
                "Full audit trail, regulatory compliance readiness, scientific "
                "rigour, and the ability to re-run historical analyses with updated "
                "assumptions while proving exactly what changed and why."
            ),
        },
        {
            "title": "Static vs Dynamic Data Separation",
            "context": (
                "Grid infrastructure data changes on fundamentally different timescales: "
                "network topology evolves over years, while operational telemetry streams "
                "in sub-second intervals. Treating them uniformly creates unnecessary "
                "complexity and performance bottlenecks."
            ),
            "decision": (
                "Strictly partition data into two categories: static reference data "
                "(topology, equipment specifications, geographic boundaries) that is "
                "versioned and loaded once per analysis, and dynamic operational data "
                "(load, frequency, state) that streams continuously."
            ),
            "why": (
                "Mixing static and dynamic data forces the entire system to operate "
                "at the speed of the fastest-changing input. Separation allows each "
                "data category to be stored, cached, and processed using the "
                "strategy most appropriate for its velocity."
            ),
            "benefit": (
                "Reduced memory pressure through lifecycle-aligned storage strategies, simplified caching strategies, "
                "clear version boundaries for audit purposes, and the ability to swap "
                "reference datasets without touching operational data pipelines."
            ),
        },
        {
            "title": "Interface-Based Design",
            "context": (
                "As the platform grows, new data sources, new analytical methods, "
                "and new visualization requirements emerge continuously. Hard-coding "
                "dependencies between components creates a brittle system that resists "
                "extension."
            ),
            "decision": (
                "Define stable, versioned interfaces between all major subsystems. "
                "Any component that satisfies the interface contract can participate "
                "in the system — whether it existed at initial design time or was "
                "added years later."
            ),
            "why": (
                "Interfaces decouple <em>what</em> a component does from <em>how</em> "
                "it does it. A new analytical method can be integrated by implementing "
                "the same interface, validated independently, and deployed without "
                "modifying any consuming component."
            ),
            "benefit": (
                "Plug-and-play extensibility, simplified testing through interface "
                "mocking, the ability to benchmark alternative implementations against "
                "identical inputs, and long-term protection against vendor or "
                "technology lock-in."
            ),
        },
        {
            "title": "Layered Architecture",
            "context": (
                "A digital twin spans concerns from raw computation through to "
                "user-facing visualisation. Collapsing these concerns into a single "
                "layer creates tight coupling between operational logic and "
                "presentation — a change to one forces changes to the other."
            ),
            "decision": (
                "Organise the platform into distinct functional layers — Computational "
                "Core, Orchestration Layer, Integration & API Layer, Analytics & Audit "
                "Layer, and Visualization & Control Layer — with each layer depending "
                "only on the layer directly below it."
            ),
            "why": (
                "Layering enforces directionality in dependencies. The visualisation "
                "layer never directly accesses raw computational internals; it consumes "
                "structured outputs from the analytics layer. When the computational "
                "core evolves, only the immediate consumer needs awareness of the change."
            ),
            "benefit": (
                "Clear separation of concerns, ability to replace or upgrade an entire "
                "layer independently, simplified onboarding for new contributors "
                "(they only need to understand their layer's interface), and natural "
                "alignment with team boundaries."
            ),
        },
        {
            "title": "Vectorized Processing",
            "context": (
                "Operating at scale — hundreds of thousands of nodes, millions of "
                "agents — makes iterative, element-by-element processing infeasible. "
                "The platform must handle entire populations simultaneously without "
                "linear degradation in performance."
            ),
            "decision": (
                "Design all computational pathways to operate on entire data arrays "
                "simultaneously rather than iterating over individual elements. "
                "Leverage the mathematical property that many infrastructure models "
                "can be expressed as operations on vectors and matrices."
            ),
            "why": (
                "An architecture designed around element-by-element loops cannot be "
                "retrofitted for scale — the performance ceiling is structural, not "
                "incidental. Vectorized design allows the architecture to express "
                "population-level operations as array-based computations rather than "
                "relying exclusively on element-by-element processing."
            ),
            "benefit": (
                "Consistent performance at production scale, efficient utilisation "
                "of modern hardware, reduced code complexity (one vector operation "
                "replaces thousands of loop iterations), and the ability to reason "
                "about entire system behaviour through aggregate properties."
            ),
        },
    ]

    # Shared style strings — collapsed to single line so the Markdown
    # parser recognises each <div style="..."> as a complete HTML tag
    # and does NOT interpret subsequent indented lines as code blocks.
    _card_style = (
        f"background-color:{CARD_BACKGROUND};border:1px solid {BORDER};"
        f"border-radius:{CARD_SPACING['border_radius']};padding:24px 28px;"
        f"margin-bottom:20px;"
    )
    _title_style = (
        f"color:{PRIMARY};font-size:1.15rem;font-weight:700;"
        f"margin-bottom:18px;padding-bottom:12px;border-bottom:1px solid {BORDER};"
    )
    _label_style = (
        "color:{color};font-size:0.72rem;font-weight:600;"
        "text-transform:uppercase;letter-spacing:0.8px;margin-bottom:4px;"
    )
    _body_style = (
        f"color:{TEXT_PRIMARY};font-size:0.95rem;line-height:1.6;"
        f"margin-bottom:18px;"
    )
    _body_style_last = (
        f"color:{TEXT_PRIMARY};font-size:0.95rem;line-height:1.6;"
    )

    for d in decisions:
        st.markdown(
            textwrap.dedent(f"""\
            <div style="{_card_style}">
                <div style="{_title_style}">{d['title']}</div>
                <div style="{_label_style.format(color=TEXT_SECONDARY)}">Context</div>
                <div style="{_body_style}">{d['context']}</div>
                <div style="{_label_style.format(color=ACCENT)}">Decision</div>
                <div style="{_body_style}">{d['decision']}</div>
                <div style="{_label_style.format(color=SUCCESS)}">Why It Matters</div>
                <div style="{_body_style}">{d['why']}</div>
                <div style="{_label_style.format(color=PRIMARY)}">Engineering Benefit</div>
                <div style="{_body_style_last}">{d['benefit']}</div>
            </div>
            """),
            unsafe_allow_html=True,
        )

    # ── Section 3: Why These Decisions Matter ────────────────
    section_title("Why These Decisions Matter")

    benefits = [
        ("🔧", "Maintainability", "Isolated concerns mean changes stay local. A team can upgrade one subsystem without understanding the internals of another."),
        ("📈", "Scalability", "Interface boundaries and vectorized design ensure the architecture scales horizontally — more nodes, more data, more users — without structural redesign."),
        ("🧪", "Testability", "Deterministic execution and interface contracts make automated validation practical. Every pathway can be tested in isolation with known inputs and expected outputs."),
        ("📋", "Auditability", "Versioned static data, deterministic pathways, and explicit interfaces create a complete provenance chain. Any result can be traced to its exact inputs."),
        ("⚡", "Performance", "Vectorized processing and static/dynamic separation ensure the platform operates efficiently at production scale, not just at demonstrator size."),
        ("🌱", "Long-Term Evolution", "The architecture anticipates change. New regulations, new data sources, and new analytical methods can be integrated without destabilising existing functionality."),
    ]

    benefits_html = "".join(
        f"""
        <div class="benefit-row">
            <span class="benefit-icon">{icon}</span>
            <span class="benefit-label">{label}</span>
            <span class="benefit-desc">{desc}</span>
        </div>"""
        for icon, label, desc in benefits
    )

    st.markdown(
        textwrap.dedent(f"""\
        <style>
        .benefit-row {{
            display: flex;
            align-items: flex-start;
            gap: 12px;
            padding: 10px 0;
            border-bottom: 1px solid {BORDER};
        }}
        .benefit-icon {{
            font-size: 1.1rem;
            flex-shrink: 0;
            width: 28px;
            text-align: center;
        }}
        .benefit-label {{
            color: {TEXT_PRIMARY};
            font-weight: 600;
            font-size: 0.92rem;
            flex-shrink: 0;
            width: 130px;
        }}
        .benefit-desc {{
            color: {TEXT_SECONDARY};
            font-size: 0.88rem;
            line-height: 1.55;
        }}
        </style>
        {benefits_html}
        """),
        unsafe_allow_html=True,
    )

    # ── Section 4: Architecture vs Implementation ────────────
    section_title("Architecture vs Implementation")

    st.markdown(
        textwrap.dedent(f"""\
        <p style="color: {TEXT_PRIMARY}; font-size: 1rem; line-height: 1.7; margin-bottom: 16px;">
        It is important to distinguish between three distinct concepts:
        </p>
        <p style="color: {TEXT_PRIMARY}; font-size: 1rem; line-height: 1.7; margin-bottom: 8px;">
        <strong style="color: {PRIMARY};">Architecture</strong> — the system's structural
        organisation: how components are decomposed, how they communicate, what contracts
        govern their interactions, and what principles guide their evolution. Architecture
        is about <em>what</em> the system is, not <em>how</em> it was built.
        </p>
        <p style="color: {TEXT_PRIMARY}; font-size: 1rem; line-height: 1.7; margin-bottom: 8px;">
        <strong style="color: {ACCENT};">Engineering Methodology</strong> — the practices,
        patterns, and processes used to design, validate, and evolve the system. This
        includes interface design, testing strategy, versioning policy, and the approach
        to managing technical debt.
        </p>
        <p style="color: {TEXT_PRIMARY}; font-size: 1rem; line-height: 1.7; margin-bottom: 16px;">
        <strong style="color: {TEXT_SECONDARY};">Protected Implementation</strong> — the
        concrete algorithms, data structures, models, and code that realise the architecture.
        This layer is protected intellectual property and is not included in this portfolio.
        </p>
        <p style="color: {TEXT_PRIMARY}; font-size: 1rem; line-height: 1.7; margin-bottom: 16px;">
        This portfolio intentionally exposes <strong>architecture and methodology</strong>
        while protecting <strong>implementation</strong>. The reasoning is that architecture
        demonstrates engineering competence; implementation details are commercially sensitive
        and legally protected.
        </p>
        """),
        unsafe_allow_html=True,
    )

    # ── Section 5: Protected Components ──────────────────────
    info_callout(
        "Detailed implementation discussions — including specific computational "
        "pathways, optimisation strategies, validation frameworks, and platform "
        "deployment architecture — are protected intellectual property. The "
        "architectural reasoning shown above remains valid regardless of the "
        "specific implementation approach.",
        callout_type="info",
    )

    # ── Footer & Watermark ───────────────────────────────────
    render_footer()
    render_watermark()


main()
