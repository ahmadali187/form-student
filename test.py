import streamlit as st
import pandas as pd
import os

# Set title
st.title("🎓 College Student Information Form")

# Input fields
name = st.text_input("Enter your Name *")
roll_number = st.text_input("Enter your Roll Number *")
course = st.text_input("Enter your Course *")
year = st.selectbox("Select your Year *", ["1st", "2nd", "3rd", "4th"])
semester = st.selectbox("Select your Semester *", ["1", "2"])
department = st.text_input("Enter your Department *")
email = st.text_input("Enter your Email *")
phone = st.text_input("Enter your Phone Number")
address = st.text_area("Enter your Address")

# Submit button
if st.button("Submit"):
    # Validate required fields
    if not name or not roll_number or not course or not department or not email:
        st.error("⚠️ Please fill in all required fields marked with *")
    else:
        # Prepare data
        student_data = pd.DataFrame([{
            "Name": name,
            "Roll Number": roll_number,
            "Course": course,
            "Year": year,
            "Semester": semester,
            "Department": department,
            "Email": email,
            "Phone": phone,
            "Address": address.replace("\n", " ")
        }])

        file_path = "students.csv"

        # Save to CSV
        if os.path.exists(file_path):
            student_data.to_csv(file_path, mode='a', header=False, index=False, quoting=1)
        else:
            student_data.to_csv(file_path, index=False, quoting=1)

        st.success("✅ Student information submitted and saved successfully!")
