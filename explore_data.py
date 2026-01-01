import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Load the dataset
print("Loading dataset")
with open('data/LSWMD.pkl', 'rb') as f:
    data = pickle.load(f)

print(f"Dataset type: {type(data)}")
print(f"Number of samples: {len(data)}")

# Convert to DataFrame for easier handling
df = pd.DataFrame(data)
print("")