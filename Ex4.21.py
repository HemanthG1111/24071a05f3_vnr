import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.datasets import fetch_openml

# Load MNIST dataset
mnist = fetch_openml('mnist_784', version=1)
df = mnist.data

# Standardize the features
scaled_df = pd.DataFrame(StandardScaler().fit_transform(df), columns=df.columns)

# Apply KMeans Clustering
kmeans = KMeans(n_clusters=10).fit(scaled_df)

# Apply PCA for 2D projection
reduced_X = pd.DataFrame(PCA(n_components=2).fit_transform(scaled_df), columns=['PCA1', 'PCA2'])

reduced_X.head()