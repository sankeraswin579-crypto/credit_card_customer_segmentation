# Credit Card Customer Segmentation Using K-Means Clustering

## Project Overview

This project performs customer segmentation on credit card users using **K-Means Clustering**. The objective is to identify groups of customers with similar spending habits, credit usage patterns, and payment behaviors. These insights can help financial institutions design targeted marketing campaigns, improve customer retention, and offer personalized financial products.

---

## Dataset

The dataset contains customer credit card information, including:

* Balance
* Purchase Amounts
* Cash Advances
* Credit Limits
* Payment Information
* Purchase Frequency
* Installment Purchases
* Tenure

### Data Preprocessing

1. Removed the `CUST_ID` column.
2. Handled missing values using median imputation.
3. Standardized numerical features using `StandardScaler`.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn

---

## Methodology

### 1. Data Cleaning

* Checked dataset structure and statistics.
* Handled missing values.
* Prepared features for clustering.

### 2. Feature Scaling

Since clustering algorithms are distance-based, all numerical features were standardized using:

```python
from sklearn.preprocessing import StandardScaler
```

### 3. Optimal Cluster Selection

The **Elbow Method** was used to determine the optimal number of clusters.

### 4. K-Means Clustering

The model was trained with:

```python
KMeans(n_clusters=4, random_state=42)
```

### 5. Cluster Analysis

Customer segments were analyzed by comparing average feature values across clusters.

---

## Results

The analysis identified **4 distinct customer segments**:

### Cluster 0 – Premium High-Value Customers

* Highest account balances
* High credit limits
* Large spending activity
* Valuable customers with strong purchasing power

### Cluster 1 – Low Activity Customers

* Very low balances
* Minimal purchases
* Limited card usage
* Potential re-engagement opportunities

### Cluster 2 – Active Regular Customers

* Moderate balances and spending
* Consistent usage patterns
* Reliable customer segment

### Cluster 3 – Credit-Oriented Customers

* Moderate spending
* Higher dependence on credit facilities
* Frequent card utilization

---

## Project Structure

```text
├── Customer Data.csv
├── credit_card_segmentation.ipynb
├── cluster_summary.csv
├── README.md
```

---

## How to Run

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

3. Run the Jupyter Notebook:

```bash
jupyter notebook credit_card_segmentation.ipynb
```

---

## Future Improvements

* Try Hierarchical Clustering and DBSCAN.
* Perform feature selection and engineering.
* Build an interactive dashboard using Streamlit or Power BI.
* Deploy the model for real-time customer segmentation.

---

## Author
Aswin sankar p s

## License

This project is licensed under the MIT License.
