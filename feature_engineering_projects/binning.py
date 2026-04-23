import pandas as pd

data = pd.DataFrame({
    "age": [18, 25, 32, 45, 60]
})

data["age_group"] = pd.cut(
    data["age"],
    bins=[0, 20, 40, 100],
    labels=["young", "adult", "senior"]
)

print(data)
