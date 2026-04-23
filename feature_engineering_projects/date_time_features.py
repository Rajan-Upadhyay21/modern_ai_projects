import pandas as pd

data = pd.DataFrame({
    "date": pd.to_datetime(["2026-01-01", "2026-02-15", "2026-03-20"])
})

data["year"] = data["date"].dt.year
data["month"] = data["date"].dt.month
data["day"] = data["date"].dt.day
data["weekday"] = data["date"].dt.day_name()

print(data)
