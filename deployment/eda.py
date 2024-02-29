# import library
import pandas as pd 
import numpy as np
import streamlit as st 

# library for visualization
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px

# Function to run streamlit prediction models
def run():
    # Title
    st.title('Exploring Diabetes Data')
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
            <img src='https://static.vecteezy.com/system/resources/previews/002/869/590/original/diabetes-word-concepts-banner-dangerous-diseases-treatment-infographics-with-linear-icons-on-coral-background-isolated-creative-typography-outline-color-illustration-with-text-vector.jpg'  alt='Diabetes Image' style='width:800px;height:400px;'>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write('---')


    # Displays text in two lines and uses CSS to layout it
    st.markdown(
        """
        <style>
        .two-columns {
            display: flex;
            justify-content: space-between;
        }
        </style>
        <div class="two-columns">
            <div> Welcome to the EDA page! <br>
                Here, we present exploratory data analysis aimed at understanding the factors contributing 
                to the risk of diabetes. Through the use of statistical techniques and relevant data visualization, 
                we strive to identify patterns and relationships among various variables related to diabetes. 
                Our main objective is to provide valuable insights for the public and healthcare professionals in 
                efforts toward prevention and management of this serious disease. With an emphasis on a deep understanding 
                of risk factors, we hope this page can serve as a useful source of information and motivate proactive 
                actions to improve public health and well-being. Thank you for joining us on this journey!
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write('---')


    # Subtitle
    st.write('## Dataframe')

    # loading dataset
    df = pd.read_csv('C:/Users/Muhammad Hafidz Adit.DESKTOP-6IPGJGG/Documents/Hacktiv8/P1/Milestone2/p1-ftds012-hck-m2-Muhammad-Hafidz-Adityaswara/diabetes_data_cleaning.csv')

    # dataframe
    st.dataframe(df)
    st.write('---')

    # Visualization Chapter
    st.write('## Exploratory Data Analysis (EDA)')

    # Title visualization
    st.write('### Diabetes Distribution Chart')
    
    # option
    opsi = st.selectbox('Select column : ', ('Age', 'HighBP', 'GenHlth', 'HighChol','HeartDiseaseorAttack','Fruits','Veggies','HvyAlcoholConsump') \
                        , format_func=lambda x: "Age" if x == "Age" else ('High Blood Pressure' if x == 'HighBP' else ('General Health' if x == 'GenHlth' else \
                        ('Heart Diseaseor Attack' if x == 'HeartDiseaseorAttack' else ('Fruits' if x == 'Fruits' else ('Veggies' if x == 'Veggies' else \
                        ('Heavy Alcohol Consumption' if x == 'HvyAlcoholConsump' else ('High Cholesterol' if x == 'HighChol' else x))))))))
    # visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x=opsi, hue='Diabetes', data=df, palette={0: 'blue', 1: 'red'}, linewidth=2.5, ax=ax)
    ax.bar_label(ax.containers[0])
    ax.bar_label(ax.containers[1])
    ax.set_xlabel(opsi)
    ax.set_ylabel(' ')
    ax.legend(title='Description', labels=['Non-Diabetes', 'Diabetes'])
    st.pyplot(fig)

    # Insight
    st.write('Insight :')
    if opsi == 'Age':
        st.write('1. The prevalence of diabetes increases with age.')
        st.write('2. The 65-69 year age group has the highest number of diabetes sufferers, followed by the 60-64 year and 70-74 year age groups.')
        st.write('3. The 18-24 year age group has the lowest number of diabetes sufferers.')
    elif opsi == 'HighBP':
        st.write('1. People with high blood pressure are more at risk of developing diabetes.')
        st.write('2. The number of people with diabetes who have high blood pressure is greater than those who do not have high blood pressure.')
        st.write('3. High blood pressure is a significant risk factor for diabetes.')
    elif opsi == 'GenHlth':
        st.write('1. The Excelent group had the lowest proportion of diabetes sufferers, but also had the lowest number of all health pattern groups.')
        st.write('2. The Good group has the highest number of diabetes sufferers among all health pattern groups, but also includes a significant number of diabetes sufferers.')
        st.write('3. The Poor group has the highest proportion of diabetes sufferers compared to other health pattern groups.')
        st.write('4. The Fair group has a relatively high proportion of diabetes sufferers, but the number is smaller than the Good group.')
    elif opsi == 'HighChol':
        st.write('1. Patients with high cholesterol constitute the majority of the diabetes and non-diabetes groups.')
        st.write('2. The proportion of diabetes sufferers is higher in people with high cholesterol than in people with low cholesterol.')
        st.write('3. Although the number of diabetics was higher in the high cholesterol group, there were still a large number of patients without diabetes.') 
    elif opsi == 'HeartDiseaseorAttack':
        st.write('1. Patients who have never had a heart attack account for a significant number of both groups, both diabetics and non-diabetics.')
        st.write('2. The proportion of patients with diabetes is higher among those who have had a heart attack compared to those who have never had a heart attack.')
        st.write('3. Although the number of patients with diabetes was higher in the group who had experienced a heart attack, there was still a sizable number of those who did not have diabetes in this group.') 
    elif opsi == 'Fruits':
        st.write('1. Patients who ate fruit were a significant number of both groups, both diabetes and non-diabetes.')
        st.write('2. The proportion of patients with diabetes was higher among those who ate fruit compared to those who did not eat fruit.')
        st.write('3. Although the number of patients with diabetes was higher in the group that ate fruit, there was still a sizable number of those without diabetes in this group.')   
    elif opsi == 'Veggies':
        st.write('1. Patients who ate vegetables were a significant number of both groups, both diabetes and non-diabetes.')
        st.write('2. The proportion of patients with diabetes was higher among those who ate vegetables compared to those who did not eat vegetables.')
        st.write('3. Although the number of patients with diabetes was higher in the group that ate vegetables, there was still a sizable number of those without diabetes in this group.')    
    elif opsi == 'HvyAlcoholConsump':
        st.write('1. Patients who did not consume alcohol accounted for a significant number of both groups, both diabetes and non-diabetes.')
        st.write('2. The proportion of patients with diabetes was higher among those who did not consume alcohol compared with those who did.')
        st.write('3. Although the number of patients with diabetes was higher in the group that did not consume alcohol, there was still a sizable number of those who consumed alcohol in this group.')

    st.write('---')


    # Create by Hafidz
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
    st.markdown(
        "<p class='right-align'>Created by Muhammad Hafidz Adityaswara</p>",
        unsafe_allow_html=True
    )


# Executes the command after the page opens
if __name__ == "__main__":
    run()
