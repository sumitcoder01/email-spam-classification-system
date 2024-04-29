import streamlit as st
import pickle
import re
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

st.set_page_config(
        page_title="Email/SMS classification system",
)

nltk.download('stopwords')

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
   vectorizer = pickle.load(f)


def stemming(text):
  port_stem = PorterStemmer()
  stem_text=re.sub('[^a-zA-Z0-9 ]',' ',text).lower().split()
  stem_text=[port_stem.stem(word) for word in stem_text if not word in stopwords.words('english')]
  stem_text = ' '.join(stem_text)
  return stem_text

st.title('Email/SMS classification system')

text = st.text_area(label="Enter the text",placeholder="enter text here...")

if st.button('Predict'):
   if len(text):
      stem_text = stemming(text)
      tranform_text = vectorizer.transform([stem_text]).toarray()
      prediction = model.predict(tranform_text)
      if prediction == 1:
         st.subheader("The text is identified as spam")
      else:
         st.subheader("The text is not spam")
   else:
      st.subheader("Type something to check Spam")    
else:
   st.subheader("Type something to check Spam")