import numpy as np
import pandas as pd

data = pd.DataFrame({
    "income": [1000, 5000, 20000, 50000]
})

data["log_income"] = np.log1p(data["income"])

print(data)
