import pandas as pd

ratings = pd.DataFrame(
    {
        "User1": [5, 4, 1, 0],
        "User2": [4, 0, 1, 0],
        "User3": [0, 0, 0, 5],
        "User4": [1, 1, 5, 4],
    },
    index=["Movie_A", "Movie_B", "Movie_C", "Movie_D"]
)

print("Collaborative Filtering Matrix:")
print(ratings)
