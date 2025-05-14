from flask import Flask, request, render_template, jsonify
from langchain_agent import run_agent

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json['message']
    try:
        response = run_agent(user_input)
    except Exception as e:
        response = f"Error: {str(e)}"
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
