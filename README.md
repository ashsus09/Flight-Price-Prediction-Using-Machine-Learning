# 🛫 Flight Price Prediction using Machine Learning

This project predicts flight ticket prices using Machine Learning techniques based on factors like Airline, Source, Destination, Stops, Duration, and Class.  
The main objective is to build a model that helps travelers estimate flight fares and assists airlines in analyzing pricing patterns.


## 🌐 Live Demo

👉 Try the app here: [https://huggingface.co/spaces/ashsus09/Flight_Price_Prediction](https://huggingface.co/spaces/ashsus09/Flight_Price_Prediction)


## 🚀 Features
- Data preprocessing and feature engineering  
- Handling missing values and encoding categorical variables  
- Exploratory Data Analysis (EDA) with visualizations  
- Model training with multiple regressors (Linear Regression, Random Forest, XGBoost)  
- Model evaluation using R², MAE, and RMSE  
- Streamlit web application for real-time flight price prediction  
- Model saved using Pickle for deployment  

## 📂 Dataset
The dataset contains details of flights with the following features:

| Feature | Description |
|----------|-------------|
| Airline | Name of the airline (e.g., IndiGo, Air India, SpiceJet) |
| Source City | City of departure |
| Destination City | City of arrival |
| Total Stops | Number of stops in the journey (Non-stop, 1 stop, etc.) |
| Departure Time | Time category of flight departure (Morning, Evening, Night) |
| Arrival Time | Time category of flight arrival |
| Duration | Total travel time |
| Class | Travel class (Economy / Business) |
| Price | Ticket price (Target variable) |

## ⚙️ Installation & Setup

Clone the repository:
```bash
git clone https://github.com/ashsus09/Flight-Price-Prediction-Using-Machine-Learning.git
cd flight-price-prediction
```

Install dependencies:
```bash
pip install -r requirements.txt
```

**requirements.txt**
```
pandas
numpy
matplotlib
seaborn
scikit-learn
xgboost
streamlit
```

Run the Streamlit app:
```bash
streamlit run app.py
```

## 📊 Exploratory Data Analysis (EDA)
- Performed data cleaning, visualization, and statistical analysis.  
- Visualized relationships between price and various features such as Airline, Total Stops, and Class.  
- Found that fewer stops and business class flights tend to have higher prices.  

**Example Visualization:**  
📈 Box plots, heatmaps, and bar charts showing feature correlations and price distribution.

## 🤖 Model Training Process
Tried multiple regression algorithms and compared results.

**Example Code:**
```python
from sklearn.ensemble import RandomForestRegressor
import pickle

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
pickle.dump(model, open('flight_model.pkl', 'wb'))
```

Evaluated using:  
- R² Score  
- Mean Absolute Error (MAE)  
- Root Mean Squared Error (RMSE)  

## 🧮 Streamlit Web App
Developed an interactive Streamlit app for users to input flight details and get real-time price predictions.

**Input Parameters:**
- Airline  
- Source City  
- Destination City  
- Departure Time  
- Arrival Time  
- Total Stops  
- Class  
- Duration  
- Day and Month of Journey  

**Output:**  
💰 Predicted Flight Price  

## 📑 Example Input → Output
| Feature | Value |
|----------|--------|
| Airline | IndiGo |
| Source | Delhi |
| Destination | Mumbai |
| Stops | 1 Stop |
| Class | Economy |
| Duration | 2.5 hours |
| Day | 15 |
| Month | 8 |

💸 **Predicted Price → ₹ 6,740**

## 📈 Business Insights
- Airline, Total Stops, and Class are the most influential factors affecting price.  
- Evening and weekend flights generally cost more due to higher demand.  
- Model helps users find the best time and route combinations for affordable travel.  

## 🔮 Future Improvements
- Include additional features like seat type, airline ratings, or demand factors.  
- Apply advanced models (CatBoost, LightGBM, Gradient Boosting).  
- Deploy app using Docker / Render / AWS.  
- Add real-time flight data integration via API.  
- Enhance visualization dashboard with Streamlit or Plotly.  

## 👨‍💻 Author
**Aastha**  
GitHub: @ashsus09 
