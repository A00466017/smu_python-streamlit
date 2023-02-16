from joblib import load
import streamlit as st
# st.title('YOUR APP')

st.title("Deploying the model")

LABELS = ['setosa', 'versicolor', 'virginica']

clf = load("DT.joblib")

sp_l = st.slider('sepal length (cm)', min_value=0, max_value=18)

sp_w = st.slider('sepal width (cm)', min_value=0, max_value=18)

pe_l = st.slider('petal length (cm)', min_value=0, max_value=18)

pe_w = st.slider('petal width (cm)', min_value=0, max_value=18)

prediction = clf.predict([[sp_l, sp_w, pe_l, pe_w]])

st.write(LABELS[prediction])
