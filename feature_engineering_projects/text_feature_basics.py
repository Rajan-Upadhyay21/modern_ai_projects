import pandas as pd

data = pd.DataFrame({
    "text": [
        "machine learning is useful",
        "feature engineering improves models",
        "text data needs preprocessing"
    ]
})

data["text_length"] = data["text"].apply(len)
data["word_count"] = data["text"].apply(lambda x: len(x.split()))

print(data)
