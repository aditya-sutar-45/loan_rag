from flask import Flask, request, jsonify
from dotenv import load_dotenv
from rag.llm import init_rag, invoke_llm

app = Flask(__name__)

# Initialize RAG system at startup
load_dotenv()
init_rag(db_path="./data/db")


@app.route("/ask", methods=["POST"])
def ask_question():
    try:
        data = request.get_json()
        if not data or "question" not in data:
            return jsonify({"error": "Please provide a 'question' field"}), 400

        question = data["question"]

        raw_response, safe_response = invoke_llm(question)

        return jsonify(safe_response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
