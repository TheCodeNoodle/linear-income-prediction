import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


dataset = {
    "Months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Income (USD)": [132.17, 158.63, 161.57, 176.02, 214.53, 282.53, 225.43, "N/A", "N/A", "N/A", "N/A", "N/A"]
}

df = pd.DataFrame(dataset)

#--------------Converting month names to numerical order--------------
month_map = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7,
             "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
df["Month_num"] = df["Months"].map(month_map)

#--------------Clean unknown data--------------
train_df = df[df["Income (USD)"] != "N/A"].copy()
train_df["Income (USD)"] = train_df["Income (USD)"].astype(float)

#--------------Training the linear regression model--------------
X = train_df[["Month_num"]]
y = train_df["Income (USD)"]
model = LinearRegression()
model.fit(X, y)

#--------------Predictiooonnn!!--------------
future_months = pd.DataFrame({"Month_num": list(range(8, 13))})
future_predictions = model.predict(future_months)

for i, month in enumerate(df["Months"][7:]):
    print(f"Predicted income for {month}: ${future_predictions[i]:.2f}")

#--------------Data plotting--------------
plt.plot(train_df["Month_num"], train_df["Income (USD)"], label="Known Income", marker='o')
plt.plot(future_months["Month_num"], future_predictions, label="Predicted Income", linestyle='--', marker='x')
plt.xticks(range(1, 13), df["Months"], rotation=45)
plt.xlabel("Month")
plt.ylabel("Income (USD)")
plt.title("Monthly Income Prediction")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
