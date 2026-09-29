import os

from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json()

    message = data.get("message", "").strip()

    if not message:
        return jsonify({
            "error": "Please enter a question."
        }), 400

    try:

        response = client.responses.create(
            model="gpt-5-mini",
            instructions="""
            You are a helpful university student assistant.

            Explain technical concepts clearly and simply.
            Help students understand programming, databases,
            algorithms, software engineering and artificial intelligence.

            Do not complete academic assessments dishonestly.
            Instead, guide the student through the concepts.
            """,

            input=message
        )

        answer = response.output_text

        return jsonify({
            "response": answer
        })

    except Exception as error:

        print(error)

        return jsonify({
            "error": "The AI service could not be reached."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)