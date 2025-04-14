import streamlit as st

# Configure the page
st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="centered")

st.title("💪 BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) easily and get health insights! 😃")

height = st.number_input("Enter your height (in meters):", min_value=0.1, format="%.2f")
weight = st.number_input("Enter your weight (in kilograms):", min_value=1.0, format="%.2f")

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.subheader(f"Your BMI: {bmi:.2f}")

        if bmi < 18.5:
            st.warning("You're underweight. 🏃‍♂️🍽️ Consider a nutrition-rich diet.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight. 🎯💪 Great job!")
            st.balloons()  # Celebrate with balloons!
        elif 25 <= bmi < 29.9:
            st.info("You're overweight. ⚡🏋️‍♂️ A bit of exercise might help!")
        else:
            st.error("You're obese. ⚠️ Please consult a health expert for advice.")
    else:
        st.error("Please provide valid height and weight.")