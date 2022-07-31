import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from plotly import graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import streamlit as st
st.set_page_config(layout="wide")

# Data=pd.read_csv(r'/home/shirsh/Downloads/Road-Traffic-Severity-Classification-main/train.csv')
Data=pd.read_csv('train.csv')

ordinal_feature_names = [ 'Year_Factor' ]
nominal_feature_names = [ 'State_Factor', 'building_class', 'facility_type'  ] 
date_time_feature_names = []
numerical_feature_name = [ 'floor_area', 'year_built' ,'energy_star_rating', 'ELEVATION', 'january_min_temp', 'january_avg_temp', 'january_max_temp',
                           'february_min_temp', 'february_avg_temp', 'february_max_temp', 'march_min_temp', 'march_avg_temp', 'march_max_temp',
                            'april_min_temp', 'april_avg_temp', 'april_max_temp', 'may_min_temp', 'may_avg_temp', 'may_max_temp', 'june_min_temp',
                            'june_avg_temp', 'june_max_temp', 'july_min_temp', 'july_avg_temp', 'july_max_temp', 'august_min_temp', 'august_avg_temp',
                               'august_max_temp', 'september_min_temp', 'september_avg_temp', 'september_max_temp', 'october_min_temp', 'october_avg_temp',
                               'october_max_temp', 'november_min_temp', 'november_avg_temp', 'november_max_temp', 'december_min_temp', 'december_avg_temp',
                               'december_max_temp', 'cooling_degree_days', 'heating_degree_days','precipitation_inches', 'snowfall_inches', 'snowdepth_inches',
                               'avg_temp', 'days_below_30F', 'days_below_20F', 'days_below_10F', 'days_below_0F', 'days_above_80F', 'days_above_90F',
                               'days_above_100F', 'days_above_110F', 'direction_max_wind_speed', 'direction_peak_wind_speed', 'max_wind_speed', 'days_with_fog']

def plot_graphs():


    st.write("""# Exploratory Data Analysis """)  

    st.write("""### Loading...  """)
    st.write("""# \n """)  
    st.write("""# \n """) 

    st.write("""##### Histogram Distribution of Site EUI across Facility Type """)
    df_temp = Data[['facility_type','floor_area','site_eui']].groupby( by='facility_type' ).mean().reset_index()
    fig = px.histogram(df_temp, x="facility_type", y="site_eui").update_xaxes( categoryorder='total ascending' )
    fig.update_layout( height=800 )
    st.plotly_chart(fig)

    st.write("""# \n """)  
    st.write("""# \n """) 
    
    st.write("""##### Histogram Distribution of Site EUI with Floor Area """)
    fig = px.histogram(df_temp, x="facility_type", y="floor_area").update_xaxes( categoryorder='total ascending' )
    fig.update_layout( height=800 )
    st.plotly_chart(fig)

    st.write("""# \n """)  
    st.write("""# \n """) 

    st.write("""##### Variation of Site EUI with Floor Area using Sunburst Chart  """)
    fig = px.sunburst(Data, path=['State_Factor', 'building_class', 'facility_type'], values='site_eui')
    st.plotly_chart(fig)

    def plot_histograms( df ):
        i=0
        fig = make_subplots( rows=1, cols=df.shape[1],subplot_titles=df.columns.values )
        for feature in df.columns.values:
            fig.add_trace( go.Histogram( x=df[feature], name=feature), row=1,col=i+1 )
            i = i+1

        no_of_features = len(df.columns.values)
        fig.update_layout( bargap=0.2, width= no_of_features*800, height=700 )
        st.plotly_chart(fig)
        return

    st.write("""# \n """)  
    st.write("""# \n """) 

    st.write("""##### Histogram of Nominal Features """)
    plot_histograms( Data[nominal_feature_names] )

    st.write("""# \n """)  
    st.write("""# \n """) 

    Data['year_built'].replace( to_replace=[0],  value=Data['year_built'].mode(), inplace=True )

    st.write("""##### Histogram of Numerical Features """)
    plot_histograms( Data[numerical_feature_name] )

    def plot_scatter_trend( df, columns ):
        i=0
        fig = make_subplots( rows=1, cols=len(columns),subplot_titles=columns )
        for feature in columns:
            fig.add_trace( go.Scatter( x=df[feature] , y=df['site_eui'], mode='markers', ), row=1,col=i+1 )
            i = i+1

        no_of_features = len(columns)
        fig.update_layout( bargap=0.2, width= no_of_features*800, height=700 )
        st.plotly_chart(fig)
        return

    st.write("""# \n """)  
    st.write("""# \n """) 

    st.write("""##### Scatter Plot with Linear Trendline of Site EUI with Year_Factor, Year of Built, Energy Star Rating , Average Temperature, Direction Maximum Wind Speed, No. of Days with Fog """)
    plot_scatter_trend( Data, columns=['Year_Factor', 'year_built', 'energy_star_rating', 'avg_temp', 'direction_max_wind_speed', 'days_with_fog' ] )

    st.write("""# \n """)  
    st.write("""# \n """) 

    st.write("""##### Distribution of Average Temperature of each Month """)
    columns_avg_temp=[ 'january_avg_temp', 'february_avg_temp', 'march_avg_temp', 'april_avg_temp', 'may_avg_temp', 'june_avg_temp', 'july_avg_temp', 'august_avg_temp', 
          'september_avg_temp', 'october_avg_temp', 'november_avg_temp', 'december_avg_temp' ]
    # fig = make_subplots( rows=1, cols=Data.shape[1],subplot_titles=columns)
    fig = go.Figure()
    for feature in columns_avg_temp:
        fig.add_trace( go.Histogram( x=Data[feature], name=feature )  )
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)
    st.plotly_chart(fig)

    st.write("""# \n """)  
    st.write("""# \n """) 

    st.write("""##### Comparison of Average Temperature """)
    # columns_avg_temp=[ 'january_avg_temp', 'february_avg_temp', 'march_avg_temp', 'april_avg_temp', 'may_avg_temp', 'june_avg_temp', 'july_avg_temp', 'august_avg_temp', 
    #       'september_avg_temp', 'october_avg_temp', 'november_avg_temp', 'december_avg_temp' ]
    # # fig = make_subplots( rows=1, cols=Data.shape[1],subplot_titles=columns)
    # fig = go.Figure()
    # for feature in columns_avg_temp:
    #     fig.add_trace( go.Box( x=Data[feature], name=feature)  )

    # fig.update_layout( height=1500 )
    # st.plotly_chart(fig)

    st.write("""# \n """)  
    st.write("""# \n """) 

    st.write("""##### Scatterplot of Site EUI with Categorical Variables """)
    df_temp = Data[['year_built','site_eui','energy_star_rating','building_class']]
    df_temp.dropna(axis=0,inplace=True)
    fig = px.scatter(df_temp, x="year_built", y="energy_star_rating",  size="site_eui", color="building_class", size_max=30)
    fig.update_layout( height=1000 )
    st.plotly_chart(fig)

    st.write("""# \n """)  
    st.write("""# \n """) 

    st.write("""##### Pair Plot of Average Temperature """)
    temp_columns = ['building_class','ELEVATION', 'cooling_degree_days', 'heating_degree_days' ,'precipitation_inches', 'snowfall_inches', 'snowdepth_inches', 'avg_temp', 'site_eui' ]
    fig1 = plt.figure( figsize=(15,15) )
    sns.pairplot(Data[temp_columns] , hue='building_class', size=4.5)
    st.pyplot(fig1)

    st.write("""# \n """)  
    st.write("""# \n """) 

    st.write("""##### Correalation Matrix """)
    # #
    fig2 = px.imshow( Data[numerical_feature_name].corr(),color_continuous_scale='RdBu_r', width=1200, height=1000 )
    st.plotly_chart(fig2)

    st.write("""# \n """)  
    st.write("""# \n """) 

    st.write("""##### Distribution of Average Temperature and   """)
    fig3 = sns.jointplot("heating_degree_days", "avg_temp", Data, kind='kde');
    st.pyplot(fig3)

    st.write("""# \n """)  
    st.write("""# \n """) 

    st.write("""##### Distribution of Amount of Snowfall and  Depth of Snow  """)
    fig4 = sns.jointplot("snowfall_inches", "snowdepth_inches", Data, kind='kde');
    st.pyplot(fig4)

    st.write("""# \n """)  
    st.write("""# \n """) 

    st.write("""### Done  """)


