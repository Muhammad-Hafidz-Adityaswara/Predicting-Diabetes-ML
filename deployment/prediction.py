# import library
import pandas as pd 
import numpy as np
import streamlit as st 

# import pickle
import pickle

# Load Model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to run streamlit prediction models
def run():
    # Set title
    st.title("Diabetes Prediction")
    st.write('---')

    # Display images using CSS to arrange the layout
    st.markdown(
        """
        <style>
        .centered {
            display: flex;
            justify-content: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Displays an image in the middle of the page
    st.markdown(
        """
        <div class="centered">
            <img src='https://cdn.idntimes.com/content-images/community/2020/10/glucometer-syringes-with-diabetes-accessories-262730-207-69d98757acdfef8fad536a57d8bc31bf.jpg' \
                  alt='Diabetes Image' style='width:800px;height:400px;'>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write('---')


    # Display text in two lines and use CSS to layout it
    st.markdown(
        """
        <style>
        .two-columns {
            display: flex;
            justify-content: space-between;
        }
        </style>
        <div class="two-columns">
            <div>"Welcome to the 'Diabetes Prediction' page! <br> 
            Here, you can use our diabetes prediction model to make predictions on your own data. 
            This model has been trained using relevant data and has the ability to predict the likelihood 
            of someone having diabetes based on certain clinical features. 
            You can input your own data into the form provided on this page. 
            Make sure to enter relevant values. After inputting the data, you can press the 'Predict' 
            button to see the prediction results from our model."</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write('---')


    with st.form(key='form parameters'):

        st.subheader("Input Data")
        Age = st.selectbox("Your age:", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], format_func=lambda x: "18-24" if x == 1 else \
                           ("25-29" if x == 2 else ("30-34" if x == 3 else ("35-39" if x == 4 else ("40-44" if x == 5 else \
                           ("45-49" if x == 6 else ("50-54" if x == 7 else ("55-59" if x == 8 else ("60-64" if x == 9 else \
                           ("65-69" if x == 10 else ("70-74" if x == 11 else ("75-79" if x == 12 else ("80 or older" if x == 13 else x)))))))))))))

        Sex = st.selectbox("Gender :", ("male", "female"), format_func=lambda x: "Male" if x == "male" else "Female")

        HighChol = st.selectbox("Have you ever been diagnosed with high cholesterol by a doctor :", \
                                ('high', 'no high'), format_func=lambda x: "Yes" if x == "high" else "No")

        CholCheck = st.selectbox("Have you undergone a cholesterol screening within the last 5 years :", \
                                 ('yes','no'), format_func=lambda x: "Yes" if x == "yes" else "No")

        BMI = st.slider("Please input your Body Mass Index (BMI) : ", 0, 100, 29)

        Smoker = st.selectbox("Have you ever smoked 100 or more cigarettes in your lifetime : (Note: 5 packs = 100 cigarettes)", \
                              ('yes','no'), format_func=lambda x: "Yes" if x == "yes" else "No")

        HeartDiseaseorAttack = st.selectbox("Have you ever been diagnosed with coronary heart disease (CHD) or experienced a heart attack (MI) :", \
                                            ('yes','no'), format_func=lambda x: "Yes" if x == "yes" else "No")

        PhysActivity = st.selectbox("Have you engaged in physical activity within the last 30 days, excluding work-related activities :", \
                                    ('yes','no'), format_func=lambda x: "Yes" if x == "yes" else "No")

        Fruits = st.selectbox("Do you consume fruit at least once a day?", ('yes','no'), format_func=lambda x: "Yes" if x == "yes" else "No")

        Veggies = st.selectbox("Do you consume vegetables at least once a day?", ('yes','no'), format_func=lambda x: "Yes" if x == "yes" else "No")

        HvyAlcoholConsump = st.selectbox("Do you consume alcohol per week? (Adult men: minimum 14; adult women: minimum 7)", \
                                         ('yes','no'), format_func=lambda x: "Yes" if x == "yes" else "No")

        GenHlth = st.selectbox ('How would you rate your overall health :', ('good','excellent','very good','fair','poor'), format_func=lambda x: "Good" \
                                if x == "good" else ("Excellent" if x == 'excellent' else ('Very Good' if x == 'very good' else ('Fair' if x == 'fair' else 'Poor'))))

        MentHlth = st.slider("How many days have you experienced poor mental health within the range of 1-30 days :",0, 30, 4)

        PhysHlth = st.slider("How many days did you have a physical illness or injury in the last 30 days :",0, 30, 6)
                
        DiffWalk = st.selectbox("Do you have serious difficulty walking or climbing stairs :", ('yes','no'), format_func=lambda x: "Yes" if x == "yes" else "No")

        Stroke = st.selectbox("Have you ever had a stroke :", ('yes','no'), format_func=lambda x: "Yes" if x == "yes" else "No")

        HighBP = st.selectbox("Do you have high or low blood pressure :", ('high', 'no high'), format_func=lambda x: "Yes" if x == "high" else "No")

        submit = st.form_submit_button('Predict')

    data_baru = {
    'Age': Age,
    'Sex': Sex,
    'HighChol': HighChol,
    'CholCheck': CholCheck,
    'BMI': BMI,
    'Smoker': Smoker,
    'HeartDiseaseorAttack': HeartDiseaseorAttack,
    'PhysActivity': PhysActivity,
    'Fruits': Fruits,
    'Veggies': Veggies,
    'HvyAlcoholConsump': HvyAlcoholConsump,
    'GenHlth': GenHlth,
    'MentHlth': MentHlth,
    'PhysHlth': PhysHlth,
    'DiffWalk': DiffWalk,
    'Stroke': Stroke,
    'HighBP' : HighBP
    }

    data_inf = pd.DataFrame([data_baru])
    st.dataframe(data_inf)


    if submit:
        score = model.predict(data_inf)
        if score == 0:
            score_txt = 'Non-Diabetes'
        else:
            score_txt = 'Diabetes'

        st.write('## Patient Status :', score_txt)

    st.write('---')
    # Display text using CSS to layout it
    st.markdown(
        """
        <style>
        .right-align {
            text-align: right;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Displays text on the right
    st.markdown(
        "<p class='right-align'>Created by Muhammad Hafidz Adityaswara</p>",
        unsafe_allow_html=True
    )

# Executes the command after the page opens
if __name__ == "__main__":
    run()