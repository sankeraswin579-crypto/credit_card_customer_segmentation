# 💳 Credit Card Customer Segmentation

An interactive Streamlit dashboard that applies **Unsupervised Machine Learning** to group credit card customers based on their spending patterns, balances, payment behavior, and purchase activity.

## 🚀 Project Overview

The project uses the K-Means clustering algorithm to identify customer segments without predefined labels. The dashboard presents customer statistics, cluster distributions, PCA visualizations, segment profiles, and downloadable results.

## 🛠️ Technologies Used

- **Python** — programming language
- **Streamlit** — interactive web dashboard
- **Pandas** — data loading and manipulation
- **NumPy** — numerical operations
- **Scikit-learn** — preprocessing, K-Means clustering, and PCA
- **Matplotlib** — data visualization

## 📁 Folder Structure

```text
Streamlit/
├── app.py
├── Customer Data.csv
├── requirements.txt
└── README.md
```

> Ensure the dataset is available locally before running the application. Do not upload sensitive or unauthorized customer financial data to a public repository.

## 📊 Dataset

The application expects a CSV file named `Customer Data.csv`.

The dataset contains 8,950 customer records and 18 columns, including:

- `CUST_ID` — customer identifier
- `BALANCE` — account balance
- `PURCHASES` — total purchases
- `ONEOFF_PURCHASES` — one-time purchases
- `INSTALLMENTS_PURCHASES` — installment purchases
- `CASH_ADVANCE` — cash advances
- `PURCHASES_FREQUENCY` — purchase frequency
- `CREDIT_LIMIT` — credit limit
- `PAYMENTS` — payment amount
- `MINIMUM_PAYMENTS` — minimum payments
- `PRC_FULL_PAYMENT` — proportion of full payments
- `TENURE` — customer tenure

The customer identifier is excluded from clustering features because it is an identifier rather than a behavioral measurement.

## 🧠 Machine Learning Workflow

1. **Load data:** Read the CSV file using Pandas.
2. **Inspect data:** Review customer records, feature counts, and missing values.
3. **Preprocess:** Select numerical features and handle missing or infinite values.
4. **Scale features:** Apply `StandardScaler` so numerical scales do not disproportionately influence K-Means.
5. **Cluster customers:** Use K-Means to group customers into a configurable number of clusters.
6. **Visualize segments:** Display cluster sizes and use PCA to project customer data into two dimensions.
7. **Profile clusters:** Calculate average numerical feature values for each segment.
8. **Export results:** Download the customer dataset with assigned cluster labels as a CSV file.

## ⚙️ Installation

### 1. Navigate to the project folder

Open PowerShell in the `Streamlit` directory:

```powershell
cd C:\Users\ASWIN\OneDrive\credit_card_segmentation_project\Streamlit
```

### 2. Activate the existing virtual environment

```powershell
..\.venv\Scripts\Activate.ps1
```

If the environment is already active, you can skip this command.

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## ▶️ Run the Application

Execute:

```powershell
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

`http://localhost:8501`

Keep the terminal running while using the application.

## 📈 Dashboard Features

- Customer dataset preview
- Total customer and feature counts
- Missing-value overview
- Adjustable number of clusters (K)
- K-Means clustering and inertia
- Customer segment distribution chart
- PCA-based cluster visualization
- Average feature values for each cluster
- Downloadable segmented customer data

## 📌 Important Notes

- **Learning type:** Unsupervised Machine Learning
- **Primary algorithm:** K-Means clustering
- **Preprocessing:** Median imputation and standardization
- **Dimensionality reduction:** Principal Component Analysis (PCA)
- **Deep Learning:** Not used in this implementation

Cluster labels such as `0`, `1`, `2`, and `3` are arbitrary identifiers, not credit scores or intrinsic customer rankings. Interpret clusters by comparing their feature averages.

PCA is used for visualization; it does not replace the original features used by K-Means.

## 🔒 Data Privacy

Before publishing the project, verify that you have permission to share the dataset. Keep confidential customer information, credentials, API keys, and environment files out of public repositories.

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Exploratory data analysis
- Missing-value handling
- Feature scaling
- Unsupervised learning
- K-Means clustering
- PCA visualization
- Interactive dashboard development
- Exporting machine-learning results

## 👨‍💻 Author

**Aswin Sankar P.S.**

AI & Data Science | Machine Learning | Python | Generative AI

---

*This README describes the current Streamlit implementation. Confirm the original project's workflow and results separately before presenting them as previously completed work.*
