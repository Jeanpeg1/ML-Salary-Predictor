import streamlit as st
import pandas as pd
import joblib

#Panggil dataset hasil train
model = joblib.load("salary_predictor.pkl")

#Tentukan judul dan pesan
st.title("Salary Prediction App")
st.write("Masukkan data kandidat untuk memprediksi gaji menggunakan model XGBoost.")

# Ambil input user dari Streamlit
age = st.number_input("Usia", min_value=18, max_value=65, value=25)
city = st.selectbox("Kota", ["Yogyakarta", "Jakarta", "Surabaya", "Medan", "Bandung"])
education = st.selectbox("Pendidikan", ["Highschool", "Bachelor", "Master", "PhD"])



# Buat DataFrame sesuai kolom asli
input_df = pd.DataFrame([{
    "age": age,
    "city": city,
    "education": education
}])

# Prediksi
if st.button("Prediksi Gaji"): 
    prediction = model.predict(input_df)[0]
    st.success(f"Prediksi Gaji: Rp {prediction:,.0f}")

