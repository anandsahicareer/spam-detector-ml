import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("Loading dataset...")

# Load dataset (TAB separated)
data = pd.read_csv(
    "spam_dataset.csv",
    sep="\t",
    header=None,
    names=["label", "text"],
    encoding="latin-1"
)

print("Dataset loaded successfully")
print("Total messages:", len(data))
print(data.head())

# Convert labels to numbers
data["label"] = data["label"].map({"ham": 0, "spam": 1})

# Features and labels
X = data["text"]
y = data["label"]

# Text vectorization
vectorizer = TfidfVectorizer(
    stop_words="english",
    lowercase=True,
    ngram_range=(1,2)
)

X = vectorizer.fit_transform(X)

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, pred)
print("Model Accuracy:", accuracy)

# Save model
pickle.dump(model, open("spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model saved successfully!")