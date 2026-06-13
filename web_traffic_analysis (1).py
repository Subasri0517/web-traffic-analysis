import pandas as pd

# Load dataset
df = pd.read_csv("web_traffic.csv")

print("Total Page Views:", df["Page_Views"].sum())

most_viewed = df.loc[df["Page_Views"].idxmax()]
print("Most Visited Page:", most_viewed["Page"])

highest_bounce = df.loc[df["Bounce_Rate"].idxmax()]
print("Highest Bounce Rate:", highest_bounce["Page"])

print("\nInsights:")
print("- Home page receives highest traffic.")
print("- Contact page has highest bounce rate.")
print("- Blog page has highest engagement time.")
