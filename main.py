import pandas as pd
from taipy.gui import Gui

# Load and process data
df = pd.read_csv("data/missile_attacks_daily.csv")
df["time_start"] = pd.to_datetime(df["time_start"], errors="coerce")
df = df.sort_values("time_start")
df["launched"] = df["launched"].fillna(0)

# Format data for Taipy chart
chart_data = {
    "x": df["time_start"].dt.strftime("%Y-%m-%d"),
    "y": df["launched"]
}

# Define the page
page = """
# 🇺🇦 Missile Attacks on Ukraine

<|{chart_data}|chart|x=x|y=y|type=line|title=Missiles Launched at Ukraine Over Time|>
"""

Gui(page=page).run()