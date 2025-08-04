# 📈 Monthly Income Predictor

A simple machine learning project that uses **linear regression** to predict missing monthly income data based on historical trends.

Built with **pandas**, **scikit-learn**, and **matplotlib**, this script takes partial yearly income data (Jan-Jul) and forecasts the remaining months (Aug-Dec) using linear regression modeling.

---

## 🚀 Features

- ✅ Handles missing data (N/A values) in income dataset
- ✅ Converts month names to numerical format for model training
- ✅ Trains linear regression model on available income data (Jan-Jul)
- ✅ Predicts missing months (Aug-Dec) based on learned trends
- ✅ Visualizes known vs predicted income with interactive plots

---

## 🧰 Tech Used

- `pandas` – for data manipulation
- `scikit-learn` – for training the regression model
- `matplotlib` – for plotting predictions

---

## 📦 Example Output

```
Monthly Income Predictions:

Known Data (Jan-Jul):
Jan: $132.17
Feb: $158.63
Mar: $161.57
Apr: $176.02
May: $214.53
Jun: $282.53
Jul: $225.43

Predicted Data (Aug-Dec):
Aug: $245.67
Sep: $257.12
Oct: $268.58
Nov: $280.03
Dec: $291.49
```

## 🛠️ How to Use

### 1. Clone the repository
```bash
git clone https://github.com/TheCodeNoodle/linear-income-prediction.git
cd linear-income-prediction
```

### 2. Install dependencies
```bash
pip install pandas scikit-learn matplotlib
```

### 3. Run the prediction script
```bash
python income_predictor.py
```

### 4. View results
- **Console Output**: See predicted income values for Aug-Dec
- **Interactive Plot**: Visual comparison of known vs predicted data
- **Grid Display**: Month-by-month breakdown with trend analysis

---

## 📁 What You Get

- **Data Processing**: Hardcoded dataset with month mapping and N/A handling
- **Trained Model**: Linear regression model trained on Jan-Jul income data
- **Predictions**: Aug-Dec income forecasts printed to console
- **Visualization**: Interactive matplotlib chart with known/predicted data points
- **Trend Analysis**: Linear progression based on historical income patterns

---

## 🔧 Customization

You can easily modify:
- **Income Data**: Update the hardcoded dataset with your own values
- **Prediction Range**: Change which months to predict (currently Aug-Dec)
- **Model Parameters**: Experiment with different regression algorithms
- **Visualization Style**: Customize plot colors, markers, and formatting
- **Data Source**: Replace hardcoded data with CSV/database input

---

## 📊 Requirements

```
pandas>=1.3.0
scikit-learn>=1.0.0
matplotlib>=3.5.0
numpy>=1.21.0
```
