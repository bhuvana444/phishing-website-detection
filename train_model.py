import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

# Small demonstration dataset based on URL characteristics.
# 0 = Legitimate, 1 = Phishing
X = np.array([
    # length, https, ip, special, dots, subdomains, suspicious words
    [22, 1, 0, 0, 1, 0, 0],
    [25, 1, 0, 1, 1, 0, 0],
    [28, 1, 0, 0, 2, 1, 0],
    [31, 1, 0, 0, 1, 0, 0],
    [35, 1, 0, 1, 2, 1, 0],
    [20, 1, 0, 0, 1, 0, 0],

    [72, 0, 1, 5, 0, 0, 2],
    [86, 0, 0, 8, 4, 3, 3],
    [94, 0, 0, 7, 3, 2, 4],
    [65, 0, 1, 6, 0, 0, 3],
    [78, 0, 0, 9, 5, 4, 3],
    [105, 0, 0, 10, 4, 3, 5],
    [59, 0, 0, 5, 3, 2, 2],
    [90, 0, 1, 7, 0, 0, 4],
])

y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1])

model = RandomForestClassifier(
    n_estimators=120,
    random_state=42,
    class_weight="balanced"
)
model.fit(X, y)
joblib.dump(model, "phishing_model.joblib")
print("Created phishing_model.joblib")
