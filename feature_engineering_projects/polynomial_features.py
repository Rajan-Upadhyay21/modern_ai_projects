from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

data = pd.DataFrame({
    "x": [1, 2, 3, 4]
})

poly = PolynomialFeatures(degree=2, include_bias=False)
transformed = poly.fit_transform(data[["x"]])

result = pd.DataFrame(transformed, columns=poly.get_feature_names_out(["x"]))

print(result)
