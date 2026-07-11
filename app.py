import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

st.set_page_config(
    page_title="Credit Card Customer Segmentation",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Credit Card Customer Segmentation")
st.markdown("---")

uploaded_file = st.file_uploader(
    "Upload Customer Data CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset")

    st.dataframe(df.head())

    st.write("Rows :", df.shape[0])
    st.write("Columns :", df.shape[1])

    st.markdown("---")

    st.subheader("Dataset Information")

    st.write(df.describe())

    st.markdown("---")

    st.subheader("Missing Values")

    st.write(df.isnull().sum())

    df.fillna(df.median(numeric_only=True), inplace=True)

    st.success("Missing values handled successfully.")

    st.markdown("---")

    if "CUST_ID" in df.columns:
        X = df.drop("CUST_ID", axis=1)
    else:
        X = df.copy()

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    st.subheader("Feature Scaling Completed")

    st.success("Data Standardized")

    st.markdown("---")

    st.subheader("Elbow Method")

    wcss = []

    for i in range(1,11):

        model = KMeans(
            n_clusters=i,
            random_state=42,
            n_init=10
        )

        model.fit(X_scaled)

        wcss.append(model.inertia_)

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(range(1,11),wcss,marker="o")

    ax.set_xlabel("Clusters")

    ax.set_ylabel("WCSS")

    ax.set_title("Elbow Method")

    st.pyplot(fig)

    st.markdown("---")

    k = st.slider(
        "Select Number of Clusters",
        2,
        10,
        4
    )

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    clusters = kmeans.fit_predict(X_scaled)

    df["Cluster"] = clusters

    st.success("Clustering Completed")

    st.markdown("---")

    st.subheader("Cluster Counts")

    st.write(df["Cluster"].value_counts())

    fig2, ax2 = plt.subplots(figsize=(7,4))

    sns.countplot(
        x="Cluster",
        data=df,
        ax=ax2
    )

    st.pyplot(fig2)

    st.markdown("---")

    st.subheader("PCA Visualization")

    pca = PCA(n_components=2)

    pca_data = pca.fit_transform(X_scaled)

    df["PCA1"] = pca_data[:,0]

    df["PCA2"] = pca_data[:,1]

    fig3, ax3 = plt.subplots(figsize=(10,6))

    sns.scatterplot(
        x="PCA1",
        y="PCA2",
        hue="Cluster",
        data=df,
        palette="Set1",
        ax=ax3
    )

    st.pyplot(fig3)

    st.markdown("---")

    st.subheader("Cluster Summary")

    cluster_summary = df.groupby("Cluster").mean(numeric_only=True)

    st.dataframe(cluster_summary)

    st.markdown("---")

    st.subheader("Correlation Heatmap")

    fig4, ax4 = plt.subplots(figsize=(12,8))

    sns.heatmap(
        df.corr(numeric_only=True),
        cmap="coolwarm",
        ax=ax4
    )

    st.pyplot(fig4)

    st.markdown("---")

    st.subheader("Download Results")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Customer Segments",
        data=csv,
        file_name="customer_segments.csv",
        mime="text/csv"
    )

    summary = cluster_summary.to_csv().encode("utf-8")

    st.download_button(
        label="Download Cluster Summary",
        data=summary,
        file_name="cluster_summary.csv",
        mime="text/csv"
    )

    st.markdown("---")

    st.success("Project Completed Successfully")

    st.write("Total Customers :", len(df))

    st.write("Total Clusters :", df["Cluster"].nunique())

else:

    st.info("Please upload Customer Data.csv")