<<<<<<< HEAD
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
=======
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
>>>>>>> 18e47dd9f7064d18ce0678c2af4441c8ed45f44f
    print("✅ Not Spam")