import pickle

print("Spam Message Detector")

# Load trained model
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Get user input
message = input("Enter a message: ")

# Convert text to numeric vector
data = vectorizer.transform([message])

# Predict
prediction = model.predict(data)

# Output result
if prediction[0] == 1:
    print("⚠ Spam Message")
else:
    print("✅ Not Spam")