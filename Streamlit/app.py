
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

st.set_page_config(
    page_title="Credit Card Customer Segmentation",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Credit Card Customer Segmentation")
st.caption("Customer analytics using Unsupervised Machine Learning | K-Means")

@st.cache_data
def load_data():
    return pd.read_csv("Customer Data.csv")

try:
    df = load_data()
except Exception as e:
    st.error(f"Could not load Customer Data.csv: {e}")
    st.stop()

st.sidebar.header("Segmentation Settings")
k = st.sidebar.slider(
    "Number of customer segments (K)",
    min_value=2,
    max_value=10,
    value=4
)

st.subheader("1. Customer Dataset")

c1, c2, c3 = st.columns(3)
c1.metric("Total Customers", f"{len(df):,}")
c2.metric("Total Features", len(df.columns))
c3.metric("Missing Values", f"{int(df.isna().sum().sum()):,}")

with st.expander("View dataset"):
    st.dataframe(df, use_container_width=True)

st.subheader("2. Prepare Customer Data")

# Customer ID is an identifier, not a clustering feature.
features = df.drop(columns=["CUST_ID"], errors="ignore")
features = features.select_dtypes(include=np.number)
features = features.replace([np.inf, -np.inf], np.nan)

# Fill missing numerical values using column medians.
features = features.fillna(features.median())
features = features.fillna(0)

# Standardize features before K-Means.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

st.success(
    f"Prepared {len(features):,} customers and "
    f"{features.shape[1]} numerical features."
)

st.subheader("3. K-Means Customer Segmentation")

with st.spinner("Training K-Means model..."):
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )
    labels = model.fit_predict(X_scaled)

results = df.copy()
results["Cluster"] = labels

a, b = st.columns(2)
a.metric("Number of Clusters", k)
b.metric("Inertia", f"{model.inertia_:,.2f}")

st.subheader("4. Customer Segment Distribution")

cluster_counts = (
    results["Cluster"]
    .value_counts()
    .sort_index()
)

fig, ax = plt.subplots()
cluster_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Cluster")
ax.set_ylabel("Number of Customers")
ax.set_title("Customers in Each Segment")
ax.tick_params(axis="x", rotation=0)
st.pyplot(fig)
plt.close(fig)

st.subheader("5. PCA Cluster Visualization")

# PCA reduces the scaled features to two dimensions for plotting.
pca = PCA(n_components=2)
coordinates = pca.fit_transform(X_scaled)

plot_df = pd.DataFrame({
    "PC1": coordinates[:, 0],
    "PC2": coordinates[:, 1],
    "Cluster": labels.astype(str)
})

fig, ax = plt.subplots()
for cluster in sorted(plot_df["Cluster"].unique(), key=int):
    subset = plot_df[plot_df["Cluster"] == cluster]
    ax.scatter(
        subset["PC1"],
        subset["PC2"],
        label=f"Cluster {cluster}",
        alpha=0.6,
        s=16
    )

ax.set_xlabel("Principal Component 1")
ax.set_ylabel("Principal Component 2")
ax.set_title("Customer Segments (PCA)")
ax.legend()
st.pyplot(fig)
plt.close(fig)

explained = pca.explained_variance_ratio_.sum() * 100
st.caption(
    f"The two PCA components explain {explained:.2f}% "
    "of the variance in the scaled features."
)

st.subheader("6. Segment Profile")

st.subheader("6. Segment Profile")

# Build the segment profile from the cleaned numerical features.
profile_data = features.copy()
profile_data["Cluster"] = labels

profile = (
    profile_data
    .groupby("Cluster")
    .mean(numeric_only=True)
    .round(2)
)

st.dataframe(profile, use_container_width=True)

st.subheader("7. Download Segmented Customer Data")

csv_data = results.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download customer segments as CSV",
    data=csv_data,
    file_name="credit_card_customer_segments.csv",
    mime="text/csv"
)

st.info(
    "Cluster numbers are machine-generated groups, not credit scores. "
    "Interpret segments by comparing their customer feature averages."
)
