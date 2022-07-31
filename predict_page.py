import sys
import subprocess
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'feature_engine'])

import sys
import subprocess
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'catboost'])

import streamlit as st
import pickle
import pandas as pd 
import feature_engine
import catboost
# import shap

# from streamlit_shap import st_shap

def load_model():
    with open(r'model_CatBR_top.pkl','rb') as file:
        files = pickle.load(file)
    return files

files = load_model()
ord_encoder_top=files['ord_encoder_top']
ohe_encoder_top=files['ohe_encoder_top']
final_model=files['final_model_CBR_top']     

def show_predict_page():

    st.write("""### We need some information for prediction """)        
    
    option_State_Factor = ['State_1', 'State_2', 'State_4', 'State_6', 'State_8', 'State_10','State_11']
    option_building_class = ['Commercial', 'Residential']
    option_facility_type = ['Grocery_store_or_food_market',
       'Warehouse_Distribution_or_Shipping_center',
       'Retail_Enclosed_mall', 'Education_Other_classroom',
       'Warehouse_Nonrefrigerated', 'Warehouse_Selfstorage',
       'Office_Uncategorized', 'Data_Center', 'Commercial_Other',
       'Mixed_Use_Predominantly_Commercial',
       'Office_Medical_non_diagnostic', 'Education_College_or_university',
       'Industrial', 'Laboratory',
       'Public_Assembly_Entertainment_culture',
       'Retail_Vehicle_dealership_showroom', 'Retail_Uncategorized',
       'Lodging_Hotel', 'Retail_Strip_shopping_mall',
       'Education_Uncategorized', 'Health_Care_Inpatient',
       'Public_Assembly_Drama_theater', 'Public_Assembly_Social_meeting',
       'Religious_worship', 'Mixed_Use_Commercial_and_Residential',
       'Office_Bank_or_other_financial', 'Parking_Garage',
       'Commercial_Unknown', 'Service_Vehicle_service_repair_shop',
       'Service_Drycleaning_or_Laundry', 'Public_Assembly_Recreation',
       'Service_Uncategorized', 'Warehouse_Refrigerated',
       'Food_Service_Uncategorized', 'Health_Care_Uncategorized',
       'Food_Service_Other', 'Public_Assembly_Movie_Theater',
       'Food_Service_Restaurant_or_cafeteria', 'Food_Sales',
       'Public_Assembly_Uncategorized', 'Nursing_Home',
       'Health_Care_Outpatient_Clinic', 'Education_Preschool_or_daycare',
       '5plus_Unit_Building', 'Multifamily_Uncategorized',
       'Lodging_Dormitory_or_fraternity_sorority',
       'Public_Assembly_Library', 'Public_Safety_Uncategorized',
       'Public_Safety_Fire_or_police_station', 'Office_Mixed_use',
       'Public_Assembly_Other', 'Public_Safety_Penitentiary',
       'Health_Care_Outpatient_Uncategorized', 'Lodging_Other',
       'Mixed_Use_Predominantly_Residential', 'Public_Safety_Courthouse',
       'Public_Assembly_Stadium', 'Lodging_Uncategorized',
       '2to4_Unit_Building', 'Warehouse_Uncategorized']

    State_Factor = st.selectbox('State in which the building is located - State Factor', options=option_State_Factor  )
    building_class = st.selectbox('Building Class', options=option_building_class )
    facility_type = st.selectbox('Building usage type - Facility Type', options=option_facility_type )

    heating_degree_days = st.slider( 'Number of degrees where the daily average temperature falls under 65 degrees Fahrenheit - heating_degree_days', 398, 7929)
    snowdepth_inches = st.slider( 'Annual snowfall in inches at the location of the building - snowdepth_inches', 0, 1292)
    snowfall_inches = st.slider( 'Annual snow depth in inches at the location of the building - snowfall_inches', 0.0, 127.3, 2.5)
    february_avg_temp = st.slider( 'Average temperature in February (in Fahrenheit) at the location of the building - february_avg_temp', -13, 48, 1 )
    ELEVATION = st.slider( 'Elevation of the building location', -6.4, 1924.5, 2.5 )
    floor_area = st.slider( 'Floor area (in square feet) of the building - floor_area', 943, 6385382)
    energy_star_rating = st.slider( 'Energy star rating of the building - energy_star_rating', 0.0, 100.0, 0.1 )    
    days_with_fog = st.slider('Number of days with fog at the location of the building', 12, 311 )
    year_built = st.slider( 'Year in which the building was constructed - year_built', 1600, 2015)

    ok = st.button("Predict")
    
    columns_name = ['heating_degree_days', 'snowdepth_inches', 'snowfall_inches', 'days_with_fog', 'State_Factor', 'february_avg_temp',
               'building_class', 'ELEVATION', 'year_built', 'floor_area', 'energy_star_rating', 'facility_type']

    values = [heating_degree_days, snowdepth_inches, snowfall_inches, days_with_fog, State_Factor, february_avg_temp,
               building_class, ELEVATION, year_built, floor_area, energy_star_rating, facility_type]

    if ok:
        data = pd.DataFrame( data=[values] ,columns=columns_name )

        data = ord_encoder_top.transform( data )
        data = ohe_encoder_top.transform( data )

        predict_value = final_model.predict(data)
        
        st.write("# Site EUI : "+str(predict_value[0]) )


        # # plot the force plot in streamlit in API
        # def st_shap(plot, height=None):
        #     shap_html = f"<head>{shap.getjs()}</head><body>{plot.html()}</body>"
        #     components.html(shap_html, height=height)

        # st.write("""### Explainable AI (using Shap)""")  
        # shap_values = shap.TreeExplainer(final_model).shap_values(data)
        
        # st_shap(shap.summary_plot(shap_values, data, plot_type="bar") )

        # # shap.initjs()
        # st_shap(shap.force_plot(shap.TreeExplainer(final_model).expected_value[0], shap_values[0][:], data))
        
        # # shap.initjs()
        # st_shap(shap.force_plot(shap.TreeExplainer(final_model).expected_value[0], shap_values[1][10], data.iloc[10]))
