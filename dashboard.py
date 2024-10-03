import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your cleaned data (replace with your actual file path)
file_path_csv = 'Cleaned_Changping_Air_Quality.csv'
data_csv_filled_combined = pd.read_csv(file_path_csv)

# Define pollutants and meteorological variab   les
pollutants_except_CO = ['PM2.5', 'PM10', 'SO2', 'NO2', 'O3']
meteorological_vars = ['TEMP', 'PRES', 'DEWP', 'WSPM', 'RAIN']

# Ensure the 'season' column is correctly mapped based on the month
data_csv_filled_combined['season'] = data_csv_filled_combined['month'].map({
    12: 1, 1: 1, 2: 1,  # Winter
    3: 2, 4: 2, 5: 2,   # Spring
    6: 3, 7: 3, 8: 3,   # Summer
    9: 4, 10: 4, 11: 4  # Fall
})

# Grouped data for yearly, monthly, and seasonal trends
yearly_pollution = data_csv_filled_combined.groupby('year')[pollutants_except_CO + ['CO']].mean()
monthly_pollution = data_csv_filled_combined.groupby('month')[pollutants_except_CO + ['CO']].mean()
seasonal_pollution = data_csv_filled_combined.groupby('season')[pollutants_except_CO + ['CO']].mean()

# Streamlit dashboard layout
st.title('Air Quality Data Dashboard')

# Section 1: Yearly Trends
st.header("Yearly Trends in Air Pollution")
st.write("Visualizing the yearly average levels of pollutants (excluding CO and for CO separately).")

# 1. Yearly trends for pollutants excluding CO
fig, ax = plt.subplots(figsize=(10, 6))
for pollutant in pollutants_except_CO:
    ax.plot(yearly_pollution.index, yearly_pollution[pollutant], label=pollutant)
ax.set_title('Yearly Average Levels of Pollutants (Excluding CO)')
ax.set_xlabel('Year')
ax.set_ylabel('Concentration')
ax.legend()
ax.grid(True)
st.pyplot(fig)

# 2. Yearly trends for CO
fig_co, ax_co = plt.subplots(figsize=(8, 5))
ax_co.plot(yearly_pollution.index, yearly_pollution['CO'], color='red', label='CO')
ax_co.set_title('Yearly Average Levels of CO')
ax_co.set_xlabel('Year')
ax_co.set_ylabel('CO Concentration')
ax_co.legend()
ax_co.grid(True)
st.pyplot(fig_co)

# Section 2: Monthly Trends
st.header("Monthly Trends in Air Pollution")
st.write("Visualizing the monthly average levels of pollutants (excluding CO and for CO separately).")

# 1. Monthly trends for pollutants excluding CO
fig_month, ax_month = plt.subplots(figsize=(10, 6))
for pollutant in pollutants_except_CO:
    ax_month.plot(monthly_pollution.index, monthly_pollution[pollutant], label=pollutant)
ax_month.set_title('Monthly Average Levels of Pollutants (Excluding CO)')
ax_month.set_xlabel('Month')
ax_month.set_ylabel('Concentration')
ax_month.legend()
ax_month.grid(True)
st.pyplot(fig_month)

# 2. Monthly trends for CO
fig_month_co, ax_month_co = plt.subplots(figsize=(8, 5))
ax_month_co.plot(monthly_pollution.index, monthly_pollution['CO'], color='red', label='CO')
ax_month_co.set_title('Monthly Average Levels of CO')
ax_month_co.set_xlabel('Month')
ax_month_co.set_ylabel('CO Concentration')
ax_month_co.legend()
ax_month_co.grid(True)
st.pyplot(fig_month_co)

# Section 3: Seasonal Trends
st.header("Seasonal Trends in Air Pollution")
st.write("Visualizing the seasonal average levels of pollutants (excluding CO and for CO separately).")

# 1. Seasonal trends for pollutants excluding CO
fig_season, ax_season = plt.subplots(figsize=(10, 6))
for pollutant in pollutants_except_CO:
    ax_season.plot(seasonal_pollution.index, seasonal_pollution[pollutant], label=pollutant)
ax_season.set_title('Seasonal Average Levels of Pollutants (Excluding CO)')
ax_season.set_xlabel('Season (1: Winter, 2: Spring, 3: Summer, 4: Fall)')
ax_season.set_ylabel('Concentration')
ax_season.legend()
ax_season.grid(True)
st.pyplot(fig_season)

# 2. Seasonal trends for CO
fig_season_co, ax_season_co = plt.subplots(figsize=(8, 5))
ax_season_co.plot(seasonal_pollution.index, seasonal_pollution['CO'], color='red', label='CO')
ax_season_co.set_title('Seasonal Average Levels of CO')
ax_season_co.set_xlabel('Season (1: Winter, 2: Spring, 3: Summer, 4: Fall)')
ax_season_co.set_ylabel('CO Concentration')
ax_season_co.legend()
ax_season_co.grid(True)
st.pyplot(fig_season_co)

# Section 4: Correlation Matrix
st.header("Correlation Between Pollutants and Meteorological Variables")
st.write("This correlation matrix visualizes the relationships between air pollutants and meteorological factors.")

# Correlation matrix
correlation_matrix_all = data_csv_filled_combined[pollutants_except_CO + ['CO'] + meteorological_vars].corr()

fig_corr, ax_corr = plt.subplots(figsize=(12, 8))
sns.heatmap(correlation_matrix_all, annot=True, cmap='coolwarm', ax=ax_corr, linewidths=0.5)
ax_corr.set_title('Correlation Matrix for Pollutants and Meteorological Variables')
st.pyplot(fig_corr)

st.write("Positive correlations indicate that as one variable increases, so does the other. Negative correlations indicate an inverse relationship.")
