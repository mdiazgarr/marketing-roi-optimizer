# Marketing Spend ROI Optimiser

A machine learning project to predict campaign ROI and optimise marketing spend allocation.  
Using real-world ad performance datasets, this tool helps analysts identify high-performing campaigns early and reallocate budgets to maximise returns.

---

## Objective
Help optimise marketing spend by:
- Predicting Return on Investment (ROI) of campaigns.
- Simulating budget reallocation to maximise profitability.
- Providing actionable insights for growth and performance marketing teams.

---

## Project Workflow

1. **Data Acquisition**  
   Public ad campaign datasets (Facebook Ads, Google Ads).  

2. **Cleaning & Feature Engineering**  
   - Standardise campaign identifiers.  
   - Calculate derived metrics:
     - CTR = Clicks / Impressions  
     - CPC = Cost / Clicks  
     - CPA = Cost / Conversions  
     - ROI = Sale_Amount / Cost  

3. **Exploratory Data Analysis (EDA)**  
   - Distribution plots of spend and ROI.  
   - Campaign performance by channel, geo, device, and keyword.  

4. **Modelling**  
   - Gradient Boosting Regressor to predict ROI.  
   - Evaluation metrics: R², RMSE.  

5. **Simulation Tool**  
   - Predict ROI for each campaign.  
   - Recommend budget reallocation (e.g., top 25% campaigns).  

---

## Repository Structure

```plaintext
marketing-roi-optimizer/
│
├── data/
│   ├── raw/              # Original datasets
│   └── processed/        # Cleaned & feature-engineered data
│
├── notebooks/
│   └── eda.ipynb         # Exploratory Data Analysis
│
├── reports/
│   └── figures/          # Generated plots & figures
│
├── src/
│   ├── data/
│   │   └── load_data.py
│   │   └── feature_engineering.py
│   ├── models/
│   │   └── train_model.py
│   ├── visuals/
│   │   └── plot_metrics.py
│   └── utils/
│       └── helpers.py
│
├── scripts/
│   └── simulate_budget_allocation.py
│
├── models/
│   └── roi_predictor.pkl # Saved model
│
├── README.md
└── requirements.txt
```

---

## Setup (Quickstart)

### Prerequisites
- Python ≥ 3.10  
- Git  
- (Optional) Conda or venv for isolated environments  

### Installation

```bash
# Clone repo
git clone https://github.com/<your-username>/marketing-roi-optimizer.git
cd marketing-roi-optimizer

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

### 1. Run Feature Engineering
```bash
python src/data/feature_engineering.py
```

### 2. Train Model
```bash
python src/models/train_model.py
```

### 3. Run Simulation
```bash
python scripts/simulate_budget_allocation.py
```

---

## Example Output

- **Model Performance**  
  - R² Score: `0.82`  
  - RMSE: `0.15`

- **Budget Reallocation Simulation**
```text
Original budget: $120,000
Total predicted return if allocated to top 25%: $180,000
```

---

## Data Sources 
- [Google Ads Performance Dataset](https://www.kaggle.com/datasets)  

---

## License
This project is licensed under the MIT License.  
Feel free to use, modify, and share with attribution.
