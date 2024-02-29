# **Transforming Healthcare: <br>Predicting Diabetes with Machine Learning Classification**
**Project Description:**  
Errors in diabetes prediction, especially false negatives, can have a very serious impact on a person's health if not detected in a timely manner. This can lead to a situation where patients at high risk for diabetes do not receive appropriate medical attention, missing the opportunity for early intervention, treatment, and timely disease management. In this project, I aim to overcome this problem by developing an early diabetes detection system using predictive technology.

Through the use of advanced machine learning algorithms and data analysis, I will build predictive models capable of identifying patients at high risk of developing diabetes. This model will be based on patient medical data such as health history, risk factors, and laboratory test results related to diabetes.

By implementing this model, I hope to reduce the false negative rate in diabetes prediction, thereby enabling early detection and timely intervention. This will allow patients to receive appropriate treatment earlier in the progression of their disease, reducing the risk of serious complications, and improving the overall prognosis.

---

**Project Scope:**
1. Cleaning data to handle missing values, outliers, and inconsistencies in diabetes datasets.
2. Conduct exploratory data analysis to understand the characteristics of variables in the diabetes dataset.
3. Implementing the K-Nearest Neighbors (KNN), Support Vector Classification (SVC), Decision Tree, Random Forest, and Boosting algorithms to create a diabetes prediction model.
4. Carrying out cross validation using the k-fold cross validation technique for each algorithm to objectively validate model performance.
5. Tuning hyperparameters on the best model of each algorithm using techniques such as grid search or random search to improve model performance.
6. Created interactive deployment models using Streamlit and Hugging Face platforms to facilitate easy use and integration of models.

--- 
**Dataset Information:**

The dataset used is `Diabetes, Hypertension and Stroke Prediction` obtained from Kaggle, here is the [Dataset](https://www.kaggle.com/datasets/prosperchuks/health-dataset?select=diabetes_data.csv)

| Column | Description | Contents |
|--------|-------------|----------|
| Age | Age category in 13-levels | 1 = 18-24, 2 = 25-29, 3 = 30-34, 4 = 35-39 <br/>5 = 40-44, 6 = 45-49, 7 = 50-54, 8 = 55-59 <br/>9 = 60-64, 10 = 65-69, 11 = 70-74 <br/>12 = 75-79, 13 = 80 or older |
| Sex | Patient's gender | 0 = female, 1 = male |
| HighChol | High cholesterol | 0 = not high cholesterol, 1 = high cholesterol |
| CholCheck | Cholesterol check | 0 = no cholesterol check in the last 5 years <br/>1 = cholesterol check within the last 5 years |
| BMI | Body Mass Index | - |
| Smoker | Ever smoked at least 100 cigarettes in lifetime? <br/>[Note: 5 packs = 100 cigarettes] | 0 = no, 1 = yes |
| HeartDiseaseorAttack | Coronary heart disease (CHD) or myocardial infarction (MI) | 0 = no, 1 = yes |
| PhysActivity | Physical activity in the last 30 days - excluding work | 0 = no, 1 = yes |
| Fruits | Consuming fruits 1 or more times per day | 0 = no, 1 = yes |
| Veggies | Consuming vegetables 1 or more times per day | 0 = no, 1 = yes |
| HvyAlcoholConsump | Adult male >=14 drinks per week; adult female >=7 drinks per week | 0 = no, 1 = yes |
| GenHlth | Would you say that your general health is | 1 = excellent, 2 = very good, 3 = good, 4 = fair, 5 = poor |
| MentHlth | Poor mental health scale 1-30 days | - |
| PhysHlth | Number of days of physical illness or injury in the last 30 days scale 1-30 | - |
| DiffWalk | Do you have serious difficulty walking or climbing stairs? | 0 = no, 1 = yes |
| Stroke | Have you ever had a stroke? | 0 = no, 1 = yes |
| HighBP | High blood pressure | 0 = not high blood pressure, 1 = high blood pressure |
| Diabetes | Diabetes class | 0 = not diabetes, 1 = diabetes |                                                |

---

**Deployment using HuggingFace:**  
The results of the deployment created using HuggingFace can be seen at the following link:
[Diabetes_Prediction](https://huggingface.co/spaces/Adityaswara/Diabetes_Prediction)

**Contact:**  
Email: muhammadhafidz221101@gmail.com