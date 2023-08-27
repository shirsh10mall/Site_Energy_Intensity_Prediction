# Site_Energy_Intensity_Prediction

#### Kaggle Notebook:- https://www.kaggle.com/code/shirshmall/site-energy-intensity-prediction-graphs-excluded#Feature-Importance

Model Deployment using Streamlit and Heroku:- https://site-energy-intensity-pred-10.herokuapp.com/

# Site Energy Intensity Prediction

## Description
The Defense Meteorological Satellite Program (DMSP) aims to elevate the precision of particle precipitation modeling across the magnetosphere to the ionosphere using an innovative database and deep learning (DL) methodologies. By harnessing this enriched dataset, we seek to harness cutting-edge DL tools to extract valuable insights. This project underscores the potential to significantly diminish energy consumption in buildings, bridging the gap between easily implementable solutions and state-of-the-art strategies.

## Dataset
The crux of this project revolves around a robust dataset encompassing an array of building attributes, localized weather data, energy consumption metrics, and the Site Energy Usage Intensity (Site EUI) parameter for each building, as quantified in a specific year. Each data entry corresponds to a discrete building observed during a designated year, providing a comprehensive repository for analysis and modeling.

## Problem Statement
Within the context of this project, we are presented with two integral datasets. The first dataset, referred to as `train_dataset`, embodies recorded Site EUI values for each respective entry. On the other hand, the `x_test` dataset omits the Site EUI values, which are instead segregated into the accompanying `y_test` dataset. The core objective is to craft a predictive model for the Site EUI values of each building by leveraging building attributes and pertinent weather data. This endeavor necessitates the utilization of the test datasets for both validation and testing purposes. Furthermore, the efficacy of the models is quantified using the Root Mean Squared Error (RMSE) metric.

## Analysis and Model Creation
1. **Feature Identification:** Through a meticulous examination, we categorize the features into distinct types, encompassing ordinal, categorical, numerical, and unique attributes. We also proactively address missing values within the dataset, employing methodologies such as mean and median imputation for robust data integrity.

2. **Data Visualization:** We harness the visualization prowess of Plotly to unveil intricate patterns and correlations within the dataset. This approach facilitates a deeper comprehension of the underlying dynamics driving energy consumption trends.

3. **Feature Encoding:** A pivotal step involves the encoding of categorical and ordinal attributes, rendering them compatible for subsequent model training endeavors. This ensures that the models can effectively learn from the entire spectrum of data.

4. **Handling Missing Values:** Employing a nuanced approach, we address the presence of missing values using simple imputers. The imputation process, guided by either mean or median values, adheres to a data-driven methodology to preserve the inherent characteristics of the dataset.

5. **Iterative Imputation:** Recognizing the prevalence of missing values in certain features, we adopt an iterative imputation strategy. This method not only augments data completeness but also maintains the intricate relationships within the dataset.

6. **Model Training:** Armed with a diverse array of regression models, including XGBoost, Random Forest, Decision Tree, and CatBoost, we embark on comprehensive model training. Each model's performance is refined through hyperparameter tuning using the Optuna framework.

7. **Model Selection:** The pivotal juncture of model selection culminates with the discerning choice of the "CatBoost" model. This selection is grounded in its remarkable ability to minimize RMSE, thus solidifying its role as the ultimate predictive tool.

8. **Explainability:** The quest for model transparency and interpretability propels us to adopt SHAP (SHapley Additive exPlanations) values. Through this methodology, we unlock the intricate decision-making processes within the model, shedding light on feature importance and predictive outputs.

9. **Feature Importance:** The CatBoost model's innate capability to highlight feature importance proves instrumental. By distilling the top 12 influential attributes, we retrain the model, harnessing the potent synergy between hyperparameter tuning and this refined feature subset.

10. **Model Persistence:** Ensuring the longevity of our efforts, we preserve the trained model and feature encoders using the pickle library. This safeguarding mechanism ensures that the model's prowess remains accessible for future endeavors.

11. **Web App Development:** Navigating toward user-centric accessibility, we embark on the development of a streamlined web application utilizing Streamlit. This empowers users to engage with the model by inputting building attributes and weather data for the precise prediction of Site EUI.

12. **Deployment:** Our commitment to seamless accessibility leads us to deploy the Streamlit web app on the Heroku platform. This strategic move ensures universal access to the predictive prowess of our model, fostering informed decision-making across the board.

