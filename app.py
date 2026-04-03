import streamlit as st
import pickle

# Load model
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Page config
st.set_page_config(page_title="Spam Detector", page_icon="📩")

# Title
st.markdown("<h1 style='text-align: center; color: blue;'>📩 Spam Detection App</h1>", unsafe_allow_html=True)

st.write("### Enter a message to check if it's Spam or Not")

# Input box
msg = st.text_area("Type your message here...")

# Button
if st.button("Check Message"):
    if msg.strip() == "":
        st.warning("⚠️ Please enter a message")
    else:
        msg_vec = vectorizer.transform([msg])
        pred = model.predict(msg_vec)[0]

        if pred == 1:
            st.error("🚫 This is a Spam Message")
        else:
            st.success("✅ This is Not Spam")