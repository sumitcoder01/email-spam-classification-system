# Email/SMS Spam Classification System

This project implements an email/SMS spam classification system that effectively distinguishes between spam and non-spam messages. It utilizes stemming and TF-IDF vectorization for data preprocessing, followed by classification using the Bernoulli Naive Bayes algorithm.

## Components:

1. **Stemming:** Normalizes variations of words by reducing them to their root or base form.
2. **TF-IDF Vectorization:** Transforms text data into numerical vectors using TF-IDF representation, capturing term frequencies weighted by inverse document frequencies.
3. **Bernoulli Naive Bayes Algorithm:** A probabilistic classifier based on Bayes' theorem, suitable for binary feature classification tasks like spam detection.

## Frontend:

The frontend interface is developed using Streamlit, providing an intuitive user experience for interacting with the classification system.

## Deployment:

The project is deployed on Render and can be accessed through the following link: [Email/SMS Spam Classification System on Render](https://email-spam-classification-system.onrender.com)

## Google Colab:

For detailed implementation and execution, refer to the Google Colab notebook: [Email/SMS Spam Classification System on Google Colab](https://colab.research.google.com/drive/1RQNPDXyWfnAwxXC_7eo2EvZz_Aoc5MWC?usp=sharing)

## Usage:

1. Open the Streamlit interface provided by the Render link.
2. Input the text message you want to classify as spam or non-spam.
3. Click on the classify button to get the prediction.

## Requirements:

- Python 3.x
- Streamlit
- Scikit-learn
- NLTK
- pickle
- regex

## How to Run Locally:

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run `streamlit run app.py` to launch the Streamlit app locally.

## Contributors:

- sumitcoder01(Sumit)