# Credit Card Customer Segmentation

**Machine Learning | Unsupervised Learning | K-Means Clustering | Streamlit | Power BI**

## Project Overview

This project analyzes credit card customer behavior and groups customers into meaningful segments using unsupervised machine learning. It helps identify patterns in spending, purchase frequency, cash advances, payments, and credit utilization.

The project combines Python-based data analysis, K-Means clustering, an interactive Streamlit dashboard, and Power BI visualization.

## Objectives

- Analyze customer transaction and payment behavior.
- Identify customer groups using K-Means clustering.
- Explore spending habits, purchase frequency, and cash advance behavior.
- Visualize customer segments through charts and dashboards.
- Export segmentation results for further analysis.

## Technologies Used

- **Programming:** Python
- **Data Analysis:** Pandas, NumPy
- **Machine Learning:** Scikit-learn, K-Means clustering
- **Dimensionality Reduction:** Principal Component Analysis (PCA)
- **Data Preprocessing:** StandardScaler
- **Visualization:** Matplotlib, Seaborn
- **Dashboard:** Streamlit, Power BI
- **Development Tools:** Jupyter Notebook, Git, GitHub

## Project Structure

```text
credit_card_segmentation_project/
│
├── data/
│   ├── README.md
│   └── notebooks/
│       ├── credit_card_segmentation.ipynb
│       ├── cluster_summary.csv
│       ├── customer_segments.csv
│       └── requirements.txt
│
├── Streamlit/
│   ├── app.py
│   ├── README.md
│   └── requirements.txt
│
├── powerbi_dashboard/
│   └── capstune_project.program.pbix
│
├── project_output_details/
│   └── Credit_Card_Segmentation_output.docx
│
├── project_presentation_final_reports/
│   └── final_report_presentation.odp
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

*Note: Actual files may vary as the project evolves.*

## Dataset

The dataset contains customer-level credit card behavior features, including:

- Balance and balance frequency
- Total purchases and one-off purchases
- Installment purchases
- Cash advances
- Purchase frequency
- Number of transactions
- Credit limit and payments
- Minimum payments
- Full-payment percentage
- Customer tenure

**Privacy:** Do not publish raw customer data or sensitive financial information. Use appropriately authorized, anonymized data.

## Machine Learning Workflow

1. **Data loading:** Import the dataset using Pandas.
2. **Data cleaning:** Inspect missing values, duplicates, and data types.
3. **Feature selection:** Select relevant numerical customer behavior features.
4. **Preprocessing:** Handle missing values and scale features using `StandardScaler`.
5. **Clustering:** Apply K-Means to group similar customers.
6. **Dimensionality reduction:** Use PCA to project high-dimensional features into two dimensions for visualization.
7. **Segment profiling:** Compare average feature values across clusters.
8. **Visualization:** Display cluster distributions and customer behavior patterns.
9. **Dashboarding:** Explore the analysis through Streamlit and Power BI.

## Run the Streamlit Dashboard

### 1. Clone the repository

```bash
git clone https://github.com/sankeraswin579-crypto/credit_card_customer_segmentation.git
cd credit_card_customer_segmentation
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Prepare the dataset

Place your authorized dataset at the location expected by the application. If the app reads `Customer Data.csv` relative to its current working directory, run it from the directory containing that file.

### 5. Launch the dashboard

From the project root, if the dataset and app dependencies are correctly configured:

```powershell
python -m streamlit run Streamlit/app.py
```

Streamlit will provide a local URL in the terminal, usually `http://localhost:8501`.

## Outputs

Depending on the data and application configuration, the project can produce:

- Customer cluster assignments
- Cluster summary statistics
- PCA-based cluster visualizations
- Segment profiles
- Downloadable segmentation results
- Interactive dashboard charts
- Power BI reports

## Business Applications

Customer segmentation can help organizations:

- Understand different spending patterns.
- Identify customers with frequent purchases.
- Analyze cash advance behavior.
- Compare payment and balance patterns across segments.
- Develop data-driven customer engagement strategies.

Clusters represent statistical patterns, not verified customer categories. Business decisions should be validated with domain expertise and appropriate privacy safeguards.

## Limitations

- Results depend on data quality and feature selection.
- K-Means requires choosing the number of clusters.
- Feature scaling and outliers can influence the results.
- PCA visualizations may not capture all cluster differences.
- The model identifies patterns and does not establish causation or guarantee future customer behavior.

## Future Improvements

- Evaluate cluster quality using silhouette scores and other appropriate metrics.
- Compare K-Means with alternative clustering algorithms.
- Add more robust missing-value and outlier handling.
- Improve dashboard filtering and segment comparisons.
- Add model evaluation, reproducibility, and automated testing.

## Author

**Aswin Sankar P.S.**

GitHub: [sankeraswin579-crypto](https://github.com/sankeraswin579-crypto)

## Disclaimer

This project is intended for educational and analytical purposes. It does not provide financial advice, credit approval decisions, or a production-ready credit risk assessment system.
