import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Comment Sentiment Checker", page_icon="💬", layout="centered")

st.title("💬 Comment Sentiment Checker")
st.write("Type a comment below and let AI analyze the sentiment!")

# Input
comment = st.text_area("Enter a comment:")

if st.button("Check Sentiment"):
    if comment.strip() == "":
        st.warning("⚠️ Please enter a comment.")
    else:
        analysis = TextBlob(comment)
        polarity = analysis.sentiment.polarity

        if polarity > 0:
            st.success("😊 Positive Sentiment")
        elif polarity < 0:
            st.error("😞 Negative Sentiment")
        else:
            st.info("😐 Neutral Sentiment")
