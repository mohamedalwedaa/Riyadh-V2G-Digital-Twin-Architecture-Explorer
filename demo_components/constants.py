"""
Design System Constants for Riyadh V2G Digital Twin — Architecture Explorer.

All visual tokens and spacing values used across the application.
These provide a consistent look and feel for all pages and components.
"""

# ── Color Palette ──────────────────────────────────────────────

PRIMARY = "#00B4D8"       # Cyan — primary brand and interactive elements
ACCENT = "#FF6B35"        # Orange — highlights, calls to action
BACKGROUND = "#0D1117"    # Near-black — page background

# Status Colors
SUCCESS = "#2ECC71"       # Green — healthy / operational
WARNING = "#F39C12"       # Amber — degraded / attention needed
CRITICAL = "#E74C3C"      # Red — offline / alert

# Neutral / Text
TEXT_PRIMARY = "#E6EDF3"
TEXT_SECONDARY = "#8B949E"
CARD_BACKGROUND = "#161B22"
BORDER = "#30363D"

# ── Card Spacing ───────────────────────────────────────────────

CARD_SPACING = {
    "padding": "16px",
    "gap": "20px",
    "border_radius": "8px",
}

# ── Watermark ──────────────────────────────────────────────────

WATERMARK_TEXT = (
    "Architecture Explorer — Not the Production Platform | "
    "Demo Scale: 97 transformers / 512 EVs "
    "(Production Platform: 60,000 / 1,000,000)"
)
