import streamlit as st

st.title("🏥 Health & BMI Calculator")

st.markdown("---")
nn  
name = st.text_input("Enter your name")

age = st.number_input("Enter your age", 10, 100)

sex = st.radio("Select Gender", ["Male", "Female"], horizontal=True)

weight = st.slider("Weight (kg)", 30.0, 150.0, 60.0, 0.5)

height = st.slider("Height (cm)", 100, 220, 170)

st.write(f"Name: {name}, Age: {age}, Gender: {sex}, Weight: {weight} kg, Height: {height} cm")

st.header("BMI Calculator")

height_m = height / 100

bmi = weight / (height_m * height_m)

bmi = round(bmi, 1)

st.metric("BMI", bmi)

if bmi < 18.5:
    st.warning("Underweight | Health Risk: Moderate")
elif bmi < 25:
    st.success("Normal Weight | Health Risk: Low")
elif bmi < 30:
    st.warning("Overweight | Health Risk: Elevated")
else:
    st.error("Obese | Health Risk: High")

st.header("Daily Calorie Need")

activity = st.selectbox(
    "Select Activity Level",
    [
        "Sedentary (desk job)",
        "Lightly active (1–3 days/wk)",
        "Moderately active (3–5 days)",
        "Very active (6–7 days)",
        "Extra active (2x training)"
    ]
)

if sex == "Male":
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
else:
    bmr = 10 * weight + 6.25 * height - 5 * age - 161

if activity == "Sedentary (desk job)":
    calories = bmr * 1.2
elif activity == "Lightly active (1–3 days/wk)":
    calories = bmr * 1.375
elif activity == "Moderately active (3–5 days)":
    calories = bmr * 1.55
elif activity == "Very active (6–7 days)":
    calories = bmr * 1.725
else:
    calories = bmr * 1.9

st.metric("Daily Calories Needed", round(calories))

st.header("Ideal Weight Range")

if sex == "Male":
    ideal_weight = 52 + 1.9 * ((height / 2.54) - 60)
else:
    ideal_weight = 49 + 1.7 * ((height / 2.54) - 60)

low = round(ideal_weight * 0.9, 1)
high = round(ideal_weight * 1.1, 1)

col1, col2 = st.columns(2)

with col1:
    st.metric("Minimum Ideal Weight", f"{low} kg")

with col2:
    st.metric("Maximum Ideal Weight", f"{high} kg")

st.header("Full Summary")

if st.button("Show my summary"):
    st.write(f"Name : {name}")
    st.write(f"Age : {age}")
    st.write(f"Gender : {sex}")
    st.write(f"BMI : {bmi}")
    st.write(f"Daily Calories Needed : {round(calories)}")
    st.write(f"Ideal Weight Range : {low} kg - {high} kg")

    if bmi < 18.5:
        st.write("BMI Category : Underweight")
    elif bmi < 25:
        st.write("BMI Category : Normal Weight")
    elif bmi < 30:
        st.write("BMI Category : Overweight")
    else:
        st.write("BMI Category : Obese")