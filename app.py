import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📩 Spam Message Detector")

st.write("Type a message below to check whether it is spam or not.")

# Input box
message = st.text_area("Enter your message")

if st.button("Detect Spam"):
    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        data = vectorizer.transform([message])
        prediction = model.predict(data)

        if prediction[0] == 1:
            st.error("⚠ This message is SPAM")
        else:
            st.success("✅ This message is NOT spam")