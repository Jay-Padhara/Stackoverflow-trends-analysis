import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("QueryResults.csv")

# Convert to datetime
df["Month"] = pd.to_datetime(df["Month"])

# Sort
df = df.sort_values("Month")

# Filter 2008–2024
df = df[(df["Month"] >= "2008-01-01") & (df["Month"] <= "2024-12-31")]

# Rolling average (12 months)
df["RollingAvg"] = df["QuestionCount"].rolling(window=12).mean()

# Plot
plt.figure(figsize=(14,7))

plt.plot(df["Month"], df["QuestionCount"], label="Monthly Questions")
plt.plot(df["Month"], df["RollingAvg"], label="12-Month Avg", linewidth=3)

# AI events
ai_events = {
    "2017-06-01": "Transformer",
    "2020-06-01": "GPT-3",
    "2022-11-01": "ChatGPT",
    "2023-03-01": "GPT-4"
}

for date, label in ai_events.items():
    d = pd.to_datetime(date)
    plt.axvline(d, linestyle="--")
    plt.text(d, df["QuestionCount"].max()*0.8, label, rotation=90)

# Labels
plt.title("Stack Overflow Questions (2008–2024)")
plt.xlabel("Year")
plt.ylabel("Number of Questions")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()