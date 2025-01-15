import streamlit as st
import pickle
import pandas as pd
import numpy as np
from functions_model import transform_bmi

with open("model_pipeline.pkl", "rb") as file:
    model = pickle.load(file)

# X = df.drop(columns=["charges"]) 
# y = df["charges"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=X['smoker'])
#age,sex,bmi,children,smoker,region,charges
input_data = pd.DataFrame({
    "age": [20],
    "sex": ["male"],
    "bmi": [40],
    "children": [2],
    "smoker": ["yes"],
    "region": ["northeast"]
})
# Test 
prediction = model.predict(input_data)
print(prediction)

#C'est là ou il va nous manquer la transo en catégorie des bmi... le truc de victor à rajouter dans la pipeline