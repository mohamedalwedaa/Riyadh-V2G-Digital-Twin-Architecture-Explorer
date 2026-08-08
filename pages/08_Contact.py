"""Contact — Private demonstrations and technical discussions."""

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
#  Page
# ═══════════════════════════════════════════════════════════════════

def main():
    # ── Page Header ──────────────────────────────────────────
    page_header(
        "Contact",
        "Private demonstrations and technical discussions",
    )

    st.markdown(
        f'<p style="color:{TEXT_SECONDARY};font-size:0.92rem;'
        f'margin:-12px 0 24px 24px;line-height:1.5;">'
        'Thank you for exploring the Riyadh V2G Digital Twin — Architecture Explorer. If you would '
        'like to discuss the platform in greater depth, private technical '
        'demonstrations are available.'
        '</p>',
        unsafe_allow_html=True,
    )

    # ── Section 1: Private Demonstration ─────────────────────
    section_title("Private Demonstration")

    info_callout(
        "The complete production platform — including live execution, "
        "architectural deep dives, interactive component exploration, and "
        "engineering discussions — is available through private technical "
        "demonstrations under NDA.",
        callout_type="protected",
    )

    # ── Section 2: Collaboration ─────────────────────────────
    section_title("Collaboration")

    st.markdown(
        textwrap.dedent(f"""\
        <p style="color:{TEXT_PRIMARY};font-size:1rem;line-height:1.7;margin-bottom:16px;">
        Demonstrations are tailored to the audience. Executive sessions focus on
        architecture, scalability, and strategic value. Engineering sessions explore
        execution models, software architecture, validation methodology, and system
        design while respecting the protected nature of the production platform.
        </p>
        """),
        unsafe_allow_html=True,
    )

    # ── Section 3: Relevant For ──────────────────────────────
    section_title("Relevant For")

    relevant_items = [
        "Engineering leaders evaluating large-scale infrastructure platforms",
        "Energy companies exploring grid flexibility and V2G integration",
        "Research institutions collaborating on digital twin methodologies",
        "Infrastructure planners seeking simulation-driven decision support",
    ]

    for item in relevant_items:
        st.markdown(
            f'<div style="'
            f'color:{TEXT_PRIMARY};'
            f'font-size:0.95rem;'
            f'line-height:2.0;'
            f'padding-left:12px;'
            f'">• {item}</div>',
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Section 4: Contact Channels ──────────────────────────
    section_title("Contact Channels")

    channels = [
        {
            "icon": "📧",
            "label": "Email",
            "detail": "Available upon request through professional channels.",
        },
        {
            "icon": "💼",
            "label": "LinkedIn",
            "detail": "Mohamed Alwedaa",
            "url": "linkedin.com/in/mohamed-alwedaa",
            "href": "https://www.linkedin.com/in/mohammedalwedaa/",
        },
        {
            "icon": "💻",
            "label": "GitHub",
            "detail": "mohamedalwedaa",
            "url": "github.com/mohamedalwedaa",
            "href": "https://github.com/mohamedalwedaa",
        },
    ]

    cols = st.columns(3)
    for col, channel in zip(cols, channels):
        with col:
            with st.container(border=True):
                st.markdown(
                    textwrap.dedent(f"""\
                    <div style="text-align:center;">
                        <div style="font-size:1.6rem;margin-bottom:10px;">{channel['icon']}</div>
                        <div style="
                            color:{TEXT_PRIMARY};
                            font-size:1rem;
                            font-weight:600;
                            margin-bottom:6px;
                        ">{channel['label']}</div>
                        <div style="
                            color:{TEXT_SECONDARY};
                            font-size:0.82rem;
                            line-height:1.5;
                            margin-bottom:4px;
                        ">{channel['detail']}</div>
                    """) +
                    (
                        f"""<a href="{channel['href']}" target="_blank" rel="noopener noreferrer" style="
                            color:{PRIMARY};
                            text-decoration:none;
                            font-size:0.8rem;
                            line-height:1.5;
                        ">{channel['url']}</a>"""
                        if "href" in channel
                        else (
                            f"""<div style="
                                color:{PRIMARY};
                                font-size:0.8rem;
                                line-height:1.5;
                            ">{channel['url']}</div>"""
                            if "url" in channel
                            else ""
                        )
                    ) +
                    "</div>",
                    unsafe_allow_html=True,
                )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Section 5: Thank You ─────────────────────────────────
    section_title("Thank You")

    with st.container(border=True):
        st.markdown(
            textwrap.dedent(f"""\
            <div style="text-align:center;padding:12px 0;">
                <div style="
                    color:{TEXT_PRIMARY};
                    font-size:1.2rem;
                    font-weight:700;
                    margin-bottom:12px;
                ">Thank you for your time.</div>
                <div style="
                    color:{TEXT_SECONDARY};
                    font-size:0.95rem;
                    line-height:1.7;
                    max-width:600px;
                    margin:0 auto;
                ">I welcome thoughtful technical discussions, research collaborations,
                and professional conversations around digital twins, infrastructure
                modelling, and large-scale software architecture.</div>
            </div>
            """),
            unsafe_allow_html=True,
        )

    # ── Footer & Watermark ───────────────────────────────────
    render_footer()
    render_watermark()


main()
