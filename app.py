from flask import Flask, render_template, request
import re
from urllib.parse import urlparse
import joblib
import numpy as np

app = Flask(__name__)

MODEL_FILE = "phishing_model.joblib"

# The included model is a small demonstration model trained on URL-pattern examples.
# For your final project, replace it with your own trained model/dataset if available.
model = joblib.load(MODEL_FILE)

SUSPICIOUS_WORDS = [
    "login", "verify", "verification", "secure", "account", "update",
    "confirm", "password", "bank", "wallet", "signin", "bonus", "free"
]

def extract_features(url):
    """Extract the same type of URL features described in the project PPT."""
    original = url.strip()
    candidate = original if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", original) else "http://" + original
    parsed = urlparse(candidate)
    host = parsed.netloc.split("@")[-1].split(":")[0]
    path = parsed.path

    url_len = len(original)
    has_https = int(parsed.scheme.lower() == "https")
    has_ip = int(bool(re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host)))
    special_chars = sum(original.count(c) for c in ["@", "-", "_", "%", "="])
    dots = host.count(".")
    subdomains = max(0, dots - 1)
    suspicious_word_count = sum(1 for word in SUSPICIOUS_WORDS if word in original.lower())

    return [
        url_len,
        has_https,
        has_ip,
        special_chars,
        dots,
        subdomains,
        suspicious_word_count
    ]

def feature_labels(values):
    labels = [
        ("URL length", values[0]),
        ("HTTPS", "Yes" if values[1] else "No"),
        ("IP address used", "Yes" if values[2] else "No"),
        ("Special characters", values[3]),
        ("Dots in domain", values[4]),
        ("Subdomains", values[5]),
        ("Suspicious words", values[6]),
    ]
    return labels

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    probability = None
    features = None
    url = ""

    if request.method == "POST":
        url = request.form.get("url", "").strip()

        if not url:
            result = ("Invalid", "Please enter a URL.")
        else:
            values = extract_features(url)
            prediction = int(model.predict([values])[0])
            probability = float(model.predict_proba([values])[0][prediction]) * 100
            result = (
                "Phishing" if prediction == 1 else "Legitimate",
                "⚠️ Suspicious URL detected." if prediction == 1
                else "✅ URL appears legitimate based on the trained demo model."
            )
            features = feature_labels(values)
            risk = "High" if probability >= 70 else "Medium" if probability >= 40 else "Low"

        reasons = []

        if values[1] == 0:
            reasons.append("No HTTPS detected")
        if values[2] == 1:
            reasons.append("IP address used in URL")
        if values[3] >= 2:
            reasons.append("Many special characters")
        if values[5] >= 2:
            reasons.append("Multiple subdomains")
        if values[6] >= 1:
            reasons.append("Suspicious words found")

    return render_template(
        "index.html",
        result=result,
        probability=probability,
        features=features,
        url=url
        risk=risk,
reasons=reasons
    )

if __name__ == "__main__":
    app.run(debug=True)
