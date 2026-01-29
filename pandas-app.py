import pandas as pd
import numpy as np

# Create a sample DataFrame
dfdemo = pd.DataFrame(
    {
        "A": np.random.randint(1, 100, 10),
        "B": np.random.rand(10),
        "C": pd.date_range("20230101", periods=10),
    }
)

print(dfdemo)

# # Print with a header
# print("=" * 50)
# print("Sample DataFrame")
# print("=" * 50)
# print(dfdemo)
# print("=" * 50)