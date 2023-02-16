from joblib import load
import streamlit as st
# st.title('YOUR APP')

st.title("Deploying the model")

LABELS = ['setosa', 'versicolor', 'virginica']

clf = load("DT.joblib")

sp_l = st.slide('sepal length (cm)', min_value=0, max_value=18)

sp_w = st.slide('sepal width (cm)', min_value=0, max_value=18)

pe_l = st.slide('petal length (cm)', min_value=0, max_value=18)

pe_w = st.slide('petal width (cm)', min_value=0, max_value=18)

prediction = clf.predict([[sp_l, sp_w, pe_l, pe_w]])

st.write(LABELS[prediction])
