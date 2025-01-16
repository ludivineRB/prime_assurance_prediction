import streamlit as st
import pandas as pd
import numpy as np
import math
from functions_model import transform_bmi
import pickle

def bmi_calculation(size, weight):
    convert_cm = weight / 100
    return round((convert_cm / size**2),2)

@st.dialog("Your result")
def display_result(charges):
    with st.container():
        st.write(f"After our calculation, the cost of your life's insurance is estimated at:")
        st.write(f":red[{charges} $ PER YEAR]")



st.write("## Evaluation of your insurance's charges")

with st.form("my_form"):
    # selection de la région de 'individu
    st.write("What is your gender ?")
    options_sex = ["male", "female"]
    sex = st.segmented_control(
    "Select your genre :", options_sex, selection_mode="single")

    # selection de la région de 'individu
    st.write("Are you a smoker ?")
    options_smoker = ["yes", "no"]
    is_smoker = st.segmented_control(
    "Your answer :",options_smoker, selection_mode="single")

    # selection de la région de 'individu
    st.write("Which region do you live ?")
    options_region = ["southwest", "southeast", "northwest", "northeast"]
    selection_region = st.segmented_control(
    "Select your region :", options_region, selection_mode="single")

    # ajout de l'âge de l'individu
    st.write("How old are you ?")
    age = st.slider("Select your age :")

    # demander le nombre d'enfants
    st.write("How many children do you have ?")
    nb_children = st.slider("Select the number of children :", min_value=0,max_value=6)

    # demander la taille 
    st.write("What is your size (cm) ?")
    size = st.number_input("Insert your size (cm) :")

    # demander le poids
    st.write("What is your weight ?")
    weight = st.number_input("Insert your weight (kg) :")
    
    # condition de soumission du formulaire 
    form_valid = True
        
    # soumission du formulaire
    submitted = st.form_submit_button(label="Submit")


if submitted:

    bmi = bmi_calculation(size, weight)
    st.write(
    "sex:", sex,
    ", smoker:", is_smoker,
    ", age:", age, 
    ", region:",selection_region, 
    ", number of children:", nb_children,
    ", bmi:", bmi,
    )

    input_data = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [nb_children],
        "smoker": [is_smoker],
        "region": [selection_region]
    })

    with open("model_pipeline.pkl", "rb") as file:
        model = pickle.load(file)

    # Test 
    prediction = model.predict(input_data)
    #print(prediction)

    prediction_float = round(prediction[0],2)

    display_result(prediction_float)
