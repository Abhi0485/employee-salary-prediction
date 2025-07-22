import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Sidebar
with st.sidebar:
    st.title("Employee Salary Prediction")
    st.markdown("**Internship Project**")
    st.markdown("Created by: Abhinav Mathur")
    st.markdown("---")
    st.markdown("🔹 Fill form or upload CSV")
    st.markdown("🔹 Click Predict")
    st.markdown("🔹 [Download Sample CSV](sample_input_data.csv)", unsafe_allow_html=True)

st.title("Salary Prediction App")

# Upload or form input
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.dataframe(df)

    # Predict for uploaded data
    job_map = {'Analyst': 0, 'Data Scientist': 1, 'HR Manager': 2, 'Project Manager': 3, 'Software Engineer': 4}
    edu_map = {'Bachelors': 0, 'Masters': 1, 'PhD': 2}
    gender_map = {'Male': 1, 'Female': 0}
    loc_map = {'Bangalore': 0, 'Chennai': 1, 'Delhi': 2, 'Hyderabad': 3, 'Mumbai': 4}

    df_encoded = df.copy()
    df_encoded['Job Title'] = df['Job Title'].map(job_map)
    df_encoded['Education Level'] = df['Education Level'].map(edu_map)
    df_encoded['Gender'] = df['Gender'].map(gender_map)
    df_encoded['Location'] = df['Location'].map(loc_map)

    input_data = df_encoded[['Job Title', 'Education Level', 'Experience', 'Gender', 'Location', 'Age']]
    df['Predicted Salary'] = model.predict(input_data)

    st.write("Predictions:")
    st.dataframe(df)
    st.download_button("Download Predictions", df.to_csv(index=False), "predicted_salaries.csv", "text/csv")

else:
    st.subheader("Enter Employee Details")

    job = st.selectbox("Job Role", ["Data Scientist", "HR Manager", "Software Engineer", "Analyst", "Project Manager"], index=0)
    education = st.selectbox("Education Level", ["Bachelors", "Masters", "PhD"], index=1)
    experience = st.slider("Years of Experience", 0, 20, 3)
    hours = st.slider("Hours per Week", 20, 60, 40)
    age = st.number_input("Age", min_value=18, max_value=65, value=30, step=1)

    # Dummy mapping
    job_map = {'Analyst': 0, 'Data Scientist': 1, 'HR Manager': 2, 'Project Manager': 3, 'Software Engineer': 4}
    edu_map = {'Bachelors': 0, 'Masters': 1, 'PhD': 2}

    input_data = np.array([[job_map[job], edu_map[education], experience, 1, 2, age]])  # gender/location placeholder

    if st.button("Predict Salary"):
        prediction = model.predict(input_data)[0]
        st.success(f"Estimated Salary: ₹ {int(prediction):,}")
