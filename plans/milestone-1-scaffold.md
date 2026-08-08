# Milestone 1 — Project Scaffold Plan

## Architecture Decisions

### 1. Multi-Page Navigation Strategy

**Decision:** Use `st.navigation()` + `st.Page` (Streamlit ≥ 1.36).

This is the current official approach. Each page file in `pages/` exposes a `main()` function. `app.py` imports each module and registers them via `st.Page`. The 9 pages and their metadata:

| # | File | Title | Icon |
|---|------|-------|------|
| 0 | `pages/00_Executive_Overview.py` | Executive Overview | `:material/dashboard:` |
| 1 | `pages/01_System_Architecture.py` | System Architecture | `:material/account_tree:` |
| 2 | `pages/02_Pipeline_Explorer.py` | Pipeline Explorer | `:material/timeline:` |
| 3 | `pages/03_Production_Scale.py` | Production Scale | `:material/ssid_chart:` |
| 4 | `pages/04_Engineering_Decisions.py` | Engineering Decisions | `:material/gavel:` |
| 5 | `pages/05_Production_Evidence.py` | Production Evidence | `:material/verified:` |
| 6 | `pages/06_System_Evolution.py` | System Evolution | `:material/trending_up:` |
| 7 | `pages/07_Credentials.py` | Credentials | `:material/license:` |
| 8 | `pages/08_Contact.py` | Contact | `:material/mail:` |

### 2. Design System (`demo_components/constants.py`)

```
Primary:    #00B4D8 (Cyan)
Accent:     #FF6B35 (Orange)
Background: #0D1117 (Dark)
Success:    #2ECC71 (Green)
Warning:    #F39C12 (Amber)
Critical:   #E74C3C (Red)

Typography:
  Title: 2rem, 700 weight
  Subtitle: 1.25rem, 500 weight
  Body: 1rem, 400 weight

Card Spacing:
  Padding: 16px
  Gap: 20px
  Border Radius: 8px
```

### 3. Synthetic Data Generation

All data is generated ONCE during scaffolding with `np.random.default_rng(42)`:

- **demo_grid.csv**: 97 transformers, 7 columns. Riyadh-centered lat/lon (~24.7°N, ~46.7°E) with noise.
- **demo_fleet.csv**: 512 EVs, 6 columns. V2G capable ~30% of fleet.
- **demo_pipeline.json**: 24 hourly snapshots. Peak load (13-17h), frequency inversely correlated.

### 4. Import Dependency Graph

```
app.py
 ├── pages/00_Executive_Overview.py → demo_components.ui_elements
 ├── pages/01_System_Architecture.py → demo_components.ui_elements
 ├── ...
 └── pages/08_Contact.py → demo_components.ui_elements

demo_components/
 ├── __init__.py (empty)
 ├── ui_elements.py → (standalone, uses st.*)
 ├── charts.py → plotly.graph_objects
 └── constants.py → (standalone, pure Python)
```

### 5. File Creation Order

1. `.streamlit/config.toml`
2. `requirements.txt`
3. `.gitignore`
4. `demo_components/__init__.py`
5. `demo_components/constants.py`
6. `demo_components/ui_elements.py`
7. `demo_components/charts.py`
8. `assets/` directory (empty)
9. Generate `synthetic_data/demo_grid.csv`
10. Generate `synthetic_data/demo_fleet.csv`
11. Generate `synthetic_data/demo_pipeline.json`
12. All 9 page files in `pages/`
13. `app.py`
14. `README.md`
15. `DISCLAIMER.md`

### 6. Verification Checklist

- [ ] `python -c "import demo_components; from demo_components.ui_elements import render_watermark, gated_button, metric_card"` succeeds
- [ ] `python -c "from demo_components.charts import placeholder_chart"` succeeds
- [ ] All 9 pages have `main()` with `st.title()` + description + `render_watermark()`
- [ ] `app.py` imports all 9 page modules and registers them with `st.navigation()`
- [ ] CSV files have exactly 97 and 512 rows
- [ ] JSON file has exactly 24 entries
- [ ] `.gitignore` covers `__pycache__/`, `.venv/`, `*.pyc`, etc.
