
# 🧠 AI-Powered Financial Chatbot (10-K Analysis Project)

This project is a simplified AI chatbot prototype developed as part of the BCG GenAI simulation on Forage. It focuses on interpreting and responding to predefined queries based on financial data extracted from the 10-K filings of **Apple**, **Microsoft**, and **Tesla** over the last three fiscal years.

---

## 📁 Project Structure

- `10-K_Data.csv` — Cleaned and structured financial data from official company filings (Total Revenue, Net Income, Assets, etc.)
- `Financial_Analysis_Chatbot.ipynb` — Jupyter Notebook used to explore the data, calculate trends (YoY growth, margins), and summarize key insights
- `chatbot.py` — A Flask-based chatbot app that serves predefined financial insights based on user input through a web interface

---

## 🚀 Features

- 🧾 **Financial Analysis**: Trends in revenue, net income, profitability, and efficiency metrics
- 🤖 **Rule-Based Chatbot**: Responds to 5 common financial questions using hardcoded logic
- 🌐 **Simple Web UI**: Built with Flask for local web-based interaction

---

## 💬 Supported Chatbot Questions

The chatbot can answer the following predefined queries:

- What is Microsoft's total revenue in 2024?
- How much did Tesla's net income change from 2023 to 2024?
- Which company had the highest operating cash flow in 2024?
- What were Apple's total assets in 2023?
- Which company had the highest net income in 2024?

---

## 🔧 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/financial-chatbot.git
   cd financial-chatbot
   ```

2. Install required package:
   ```bash
   pip install pandas seaborn flask
   ```

3. Start the chatbot server:
   ```bash
   python chatbot.py
   ```

4. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

---

## 📊 Insights Summary

- **Microsoft** leads in profitability and operating efficiency.
- **Apple** remains the top revenue generator but shows slightly declining net income.
- **Tesla** exhibits high volatility with a sharp drop in profit in 2024 despite stable revenue.

---

## 📚 Skills Practiced

- Python scripting & data analysis
- Jupyter Notebook workflows
- Financial metrics interpretation
- Flask web app development
- Rule-based chatbot design

---

## 🏁 Future Enhancements

- Add fuzzy matching or NLP to understand more natural language questions
- Turn static answers into dynamic data-driven responses using AI

---

## 🙌 Acknowledgments

- Developed as part of the [BCG GenAI Virtual Experience Program on Forage](https://www.theforage.com/simulations/bcg/gen-ai-anlo)
