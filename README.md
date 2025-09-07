# Prediksi Gaji Berdasarkan Karakteristik Pekerja

## 📖 Deskripsi Project
Project ini bertujuan untuk memprediksi gaji seseorang berdasarkan beberapa fitur seperti usia, tingkat pendidikan, dan kota tempat tinggal.  
Project ini meliputi **end-to-end machine learning pipeline** mulai dari eksplorasi data, preprocessing, pemodelan, tuning hyperparameter, interpretasi model (SHAP), hingga deployment menggunakan **Streamlit**.

## 🗂️ Dataset
- Sumber: Synthetic Dataset.
- Jumlah data: 500 baris, 4 fitur.
- Fitur utama:
  - `age` → usia pekerja
  - `education` → tingkat pendidikan (Highschool, Bachelor, Master, PhD)
  - `city` → kota tempat tinggal
- Target: `salary` (nilai gaji)

## ⚙️ Metodologi
1. **EDA (Exploratory Data Analysis)**  
   - Analisis distribusi umur, kota, dan pendidikan.
   - Identifikasi hubungan antar fitur dengan target `salary`.

2. **Preprocessing**
   - Encoding kategori (`OneHotEncoder`, `OrdinalEncoder`).
   - Scaling numerik (`StandardScaler`).
   - Pipeline dengan `ColumnTransformer`.

3. **Modeling**
   - Algoritma yang digunakan:
     - Linear Regression
     - Random Forest Regressor
     - XGBoost Regressor
   - Hyperparameter tuning dengan `GridSearchCV`.

4. **Evaluasi Model**
   - Metrik: R², MAE, RMSE.
   - Perbandingan performa ketiga model.

5. **Model Explainability**
   - Feature importance.
   - SHAP values (SHAP summary plot untuk Random Forest & XGBoost).

6. **Deployment**
   - Aplikasi interaktif menggunakan **Streamlit**.
   - User dapat input data (`age`, `education`, `city`) untuk memprediksi gaji.

## 📊 Hasil
- **Best Model:** XGBoost.
- **Performansi:**
  - R²: 0.988
  - MAE: 421865.44
  - RMSE: 512362.8

> Insight: Pendidikan lebih dominan daripada kota dalam menentukan gaji.

## 🚀 Cara Menjalankan
1. Clone repository ini:
   ```bash
   git clone https://github.com/Jeanpeg1/ML-Salary-Predictor.git
   cd ML-Salary-Predictor
