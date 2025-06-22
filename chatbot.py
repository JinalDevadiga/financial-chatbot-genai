from flask import Flask, request, render_template_string

chatbot = Flask(__name__)

# Predefined answers based on 10-K financial data
answers = {
    "What is Microsoft's total revenue in 2024?":
        "Microsoft's total revenue in 2024 was $245,122 million.",
    
    "How much did Tesla's net income change from 2023 to 2024?":
        "Tesla's net income decreased from $14,974 million in 2023 to $7,153 million in 2024, a drop of approximately 52.23%.",
    
    "Which company had the highest operating cash flow in 2024?":
        "Microsoft had the highest operating cash flow in 2024 with $118,548 million.",
    
    "What were Apple's total assets in 2023?":
        "Apple's total assets in 2023 were $352,583 million.",
    
    "Which company had the highest net income in 2024?":
        "Microsoft had the highest net income in 2024 with $88,136 million."
}

# Simple HTML interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>10-K Financial Chatbot</title>
</head>
<body>
    <h2>10-K Financial Chatbot</h2>
    <form method="post">
        <label>Enter your question:</label><br>
        <input type="text" name="query" size="60" required/><br><br>
        <input type="submit" value="Ask"/>
    </form>
    {% if response %}
        <p><strong>Response:</strong> {{ response }}</p>
    {% endif %}
</body>
</html>
"""

@chatbot.route("/", methods=["GET", "POST"])
def chat():
    response = None
    if request.method == "POST":
        user_query = request.form["query"]
        response = answers.get(user_query, "Sorry, I can only respond to predefined questions.")
    return render_template_string(HTML_TEMPLATE, response=response)

if __name__ == "__main__":
    chatbot.run(debug=True)
