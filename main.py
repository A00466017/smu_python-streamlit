from joblib import load
import streamlit
streamlit.title('YOUR APP')

streamlit.title("Deploying the model")

clf = load("DT.joblib")
