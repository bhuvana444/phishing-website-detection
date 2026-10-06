# Phishing Website Detector – Mini Project Demo

This is a small working Flask demonstration for the mini project.

## What it demonstrates

Website URL
→ Feature Extraction
→ Machine Learning Model
→ Prediction
→ Legitimate / Phishing

The features are:
- URL length
- HTTPS
- IP address
- Special characters
- Dots/subdomains
- Suspicious words

## Run in VS Code

1. Install Python 3.
2. Open this folder in VS Code.
3. Open Terminal.
4. Run:

```bash
pip install -r requirements.txt
python train_model.py
python app.py
```

5. Open the address shown by Flask, normally:
http://127.0.0.1:5000

## Safe demo URLs

Try:
- https://www.google.com
- https://www.wikipedia.org

For a suspicious-pattern demonstration, use a made-up URL such as:
- http://192.168.1.10/login/verify-account
- http://secure-login-verify-example.test/account/update

These are demonstration strings. Do not visit suspicious websites.

## Important project note

This is a demonstration model trained on a tiny illustrative dataset so that your presentation can show the complete software flow. It is NOT a production-grade phishing detector.

For a stronger final project, replace the illustrative training data with your actual phishing/legitimate URL dataset, train the model, and evaluate it with accuracy, precision, recall and a confusion matrix.
