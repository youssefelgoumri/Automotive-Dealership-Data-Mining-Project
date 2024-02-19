import pickle
import pandas as pd
import streamlit as st

model_pkl_file = "category_model.pkl"  

with open(model_pkl_file, 'rb') as file:  
    model = pickle.load(file)

# Function to predict the category based on user input
def predict_category(features):
    input_data = pd.DataFrame([features])
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit UI
st.title("Car Category Prediction")

# User Input Form
st.sidebar.header("User Input")
age = st.sidebar.slider("Age", 18, 84, 30)

sexe = st.sidebar.selectbox("Sexe", ['M', 'F'])
sexe_mapping = {'M': 0, 'F': 1}
sexe_mapped = sexe_mapping[sexe]

taux = st.sidebar.slider("Taux (Capacité d'endettement)", 100, 500, 2000)

situation_familiale = st.sidebar.selectbox("Situation Familiale", ['Célibataire', 'Divorcée', 'En Couple', 'Marié(e)'])
situation_familiale_mapping = {'En Couple': 0, 'Célibataire': 1, 'marié(e)':2,'Divorcée':3,'Marié(e)':4}
situation_familiale_mapped = situation_familiale_mapping[situation_familiale]

nb_enfants_a_charge = st.sidebar.slider("Nombre d’enfants à charge", 0, 4, 0)

deuxieme_voiture = st.sidebar.checkbox("Le client possède déjà un véhicule principal?")
deuxieme_voiture_mapping = {False: 0, True: 1}
deuxieme_voiture_mapped = deuxieme_voiture_mapping[deuxieme_voiture]


# Make Prediction Button
if st.sidebar.button("Predict"):
    features = {'age': age, 'sexe': sexe_mapped, 'taux': taux, 'situationFamiliale': situation_familiale_mapped, 'nbEnfantsAcharge': nb_enfants_a_charge, '2eme voiture': deuxieme_voiture_mapped}
    predicted_category = predict_category(features)
    category_names = {
        0: 'Family Cars',
        1: 'Luxury Cars',
        2: 'City Cars'
    }
        # Map the predicted category to category name
    category_name = category_names.get(predicted_category, f'Unknown Category ({predicted_category})')
    
    st.success(f"The predicted category is: {category_name}")