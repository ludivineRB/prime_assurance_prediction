import streamlit as st
import pandas as pd
import numpy as np
import math

def bmi_calculation(size, weight):
    return round((weight / size**2),2)


st.write("Prédiction d'une prime d'assurance")

with st.form("my_form"):
    # selection de la région de 'individu
    st.write("What is your genre ?")
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
    age = st.slider("Scroll the cursor")

    # demander le nombre d'enfants
    st.write("How many children do you have ?")
    nb_children = st.slider("Select the number of children", min_value=0,max_value=6)

    # demander la taille 
    st.write("What is your size (m) ?")
    size = st.number_input("Insert your size (m) :")

    # demander le poids
    st.write("What is your weight ?")
    weight = st.number_input("Insert your weight (kg) :")
    

        
    # soumission du formulaire
    submitted = st.form_submit_button("Submit")

st.write("Outside the form")

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



# input_data = pd.DataFrame([
#     [age],
#     [sex],
#     [bmi],
#     [nb_children],
#     [is_smoker],
#     [selection_region]
# ])

# st.write(input_data)

