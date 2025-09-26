from flask import Flask, render_template, request, jsonify
import requests  # <-- use requests for API calls

API_KEY = "82dcae79-fb3a-4081-a36f-00e0107f2e70"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chat.html")


@app.route("/ask", methods=["POST"])
def ask():
    user_msg = request.json.get("message")

    system_prompt = """
    You are a kind and supportive AI companion focused ONLY on queries related to this college:
    "KAILASH INSTITUTE OF PHARMACY AND MANAGEMENT & KIPM COLLEGE OF ENGINEERING AND TECHNOLOGY"
    Website: https://www.kipm.edu.in/

    ❌ Do NOT answer questions about coding, history, politics, math, or other unrelated topics.
    ✅ ONLY answer queries related to this website.

    📌 VERY IMPORTANT:
    - Always format your response in valid HTML.
    - Start with a bold heading (<h3><b>...</b></h3>).
    - Then provide the information in point-wise format using <ul><li>...</li></ul>.
    - Do not add anything outside HTML.
    Example:
    <h3><b>About KIPM College</b></h3>
    <ul>
      <li>Located in Gorakhpur, Uttar Pradesh</li>
      <li>Offers Engineering, Pharmacy, and Management courses</li>
      <li>Affiliated to AKTU, Lucknow</li>
    </ul>

    📌 VERY IMPORTANT:
    Campus Location:
    KIPM-Technical Campus , BL 1 & 2 Sector-9 GIDA,
Gorakhpur, Uttar Pradesh
CONTACT US- +91-8009902933-40, +91-9151005261-70,
+91-9628373559, +918853437366
email: kipm08@gmail.com


City Office:
CHARU CHANDRAPURI, NEAR CANTT THANA
GORAKHPUR-273001
CONTACT US +91-9984804356
    """

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "Meta-Llama-3-8B-Instruct",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_msg}
        ]
    }

    resp = requests.post(
        "https://api.awanllm.com/v1/chat/completions",
        headers=headers,
        json=payload
    )

    # Extract only the assistant's reply (HTML expected)
    reply = resp.json()["choices"][0]["message"]["content"]

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True ,port=501)
