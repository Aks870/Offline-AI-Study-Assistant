from flask import Flask, render_template, request, jsonify
import requests


app = Flask(__name__)


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3:1.7b"


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/solve", methods=["POST"])
def solve():

    data = request.get_json()

    question = data.get("question", "").strip()

    mode = data.get("mode", "simple")


    if not question:

        return jsonify({
            "error": "Please enter a question."
        }), 400


    # ---------------------------------
    # SIMPLE ANSWER
    # ---------------------------------

    if mode == "simple":

        mode_instruction = """
Give a simple and clear answer.

Start with the direct answer.
Then explain the concept briefly.
Use one simple example when useful.

Keep the answer concise and easy for a student to understand.
"""


    # ---------------------------------
    # DETAILED EXPLANATION
    # ---------------------------------
    
    elif mode == "detailed":
       mode_instruction = """
Give a detailed and complete educational explanation of the topic.

The answer must be substantially more detailed than a simple answer.

Explain the topic as if you are teaching it to a student who wants
to understand the concept properly.

For a typical topic, include the relevant sections such as:

### Definition
Clearly explain what the topic means.

### Key Concepts
Explain the main ideas and important concepts related to the topic.

### How It Works
Explain the working or process step by step whenever applicable.

### Types
Explain the important types or categories when they exist.

### Examples
Give clear and easy-to-understand examples.

### Real-World Applications
Explain where the concept is used in the real world.

### Advantages and Limitations
Include these when they are relevant to the topic.

### Conclusion
End with a short summary of the topic.

Do not include sections that are not relevant to the question.

Each important point should be explained, not merely listed.

The answer should normally be around 400-600 words for a broad
conceptual question, but use your judgment for shorter questions.

Do not give a short two-paragraph answer.

Do not stop after giving only the definition and one example.

Complete the explanation properly.
"""
    # ---------------------------------
    # EXAM ANSWER
    # ---------------------------------

    elif mode == "exam":

        mode_instruction = """
Give an exam-oriented answer.

Start with a clear definition.

Then explain the important points in an organized way.

Use headings and bullet points where useful.

Include an example when relevant.

Focus on information useful for writing an exam answer.

Keep the answer clear, structured and reasonably concise.
"""


    # ---------------------------------
    # DEFAULT
    # ---------------------------------

    else:

        mode_instruction = """
Give a simple and clear explanation.

Start with the direct answer.
Explain the concept briefly.
Use a simple example when useful.
"""


    # ---------------------------------
    # AI PROMPT
    # ---------------------------------

    prompt = f"""
You are an Offline AI Study Assistant.

Your job is to help a student understand academic topics.

{mode_instruction}

Important rules:

- Answer the student's actual question.
- Do not assume that every question is about Python.
- Do not use a fixed answer from a question-answer database.
- Generate the answer specifically for the question.
- Do not mention Ollama, Qwen, or the local AI model.
- Do not unnecessarily repeat the question.
- Use simple and student-friendly language.
- If you are unsure about a fact, say so instead of inventing information.

Student Question:

{question}
"""


    # ---------------------------------
    # SEND REQUEST TO OLLAMA
    # ---------------------------------

    try:

        response = requests.post(

            OLLAMA_URL,

            json={

                "model": MODEL_NAME,

                "prompt": prompt,

                "stream": False,
                "think": False,

                "options": {
                    "temperature": 0.4,
                    "num_predict": 1450
                },
                "keep_alive": -1

            },

            timeout=240

        )


        response.raise_for_status()


        result = response.json()


        answer = result.get(
            "response",
            ""
        ).strip()


        if not answer:

            return jsonify({

                "error":
                "The AI did not return an answer."

            }), 500


        return jsonify({

            "question": question,

            "answer": answer

        })


    # ---------------------------------
    # OLLAMA CONNECTION ERROR
    # ---------------------------------

    except requests.exceptions.ConnectionError:

        return jsonify({

            "error":
            "Ollama is not running. Please start Ollama and try again."

        }), 503


    # ---------------------------------
    # TIMEOUT ERROR
    # ---------------------------------

    except requests.exceptions.Timeout:

        return jsonify({

            "error":
            "The AI took too long to respond. Please try again."

        }), 504


    # ---------------------------------
    # OTHER REQUEST ERROR
    # ---------------------------------

    except requests.exceptions.RequestException as e:

        return jsonify({

            "error":
            f"Ollama error: {str(e)}"

        }), 500


# ---------------------------------
# START FLASK SERVER
# ---------------------------------

if __name__ == "__main__":

    app.run(debug=True)