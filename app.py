import streamlit as st
import pandas as pd
import joblib

model = joblib.load("salary_predictor.pkl")

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


# city = st.selectbox("Kota", ["Jakarta", "Bandung", "Surabaya", "Medan"])
# education = st.selectbox("Pendidikan", ["SMA", "Diploma", "Sarjana", "Magister", "Doktor"])
# experience = st.number_input("Lama pengalaman (tahun)", min_value=0, max_value=40, value=3)
# age = st.number_input("Usia Karyawan (tahun)", min_value=18, max_value=60, value=25)

# data = pd.DataFrame({
#     "City": [city],
#     "Education": [education],
#     "Experience": [experience],
#     "Age": [age]
# })

# if st.button("Prediksi Gaji"):
#     prediction = model.predict(data)
#     st.success(f"Prediksi Gaji: Rp {prediction[0]:,.2f}")