# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame using the list given above. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()

# Write your code to filter streamlit warnings 
st.set_option('deprecation.showPyplotGlobalUse', False)
# Configure your home page.
# Set the title to the home page contents.
st.title("Census Visualisation App")
# Provide a brief description for the web app.
st.text('''This web app allows user to explore and visualise census data.''')

# View Dataset Configuration
st.header("View Data")
# Add an expander and display the dataset as a static table within the expander.

st.expander("View Dataset")
# Create three beta_columns.
st.subheader("Column's Description")
col1 , col2 , col3= st.columns(3)
# Add a checkbox in the first column. Display the column names of 'census_df' on the click of checkbox.
with col1 :
      if st.checkbox("Show all column names"):
        st.table(list(census_df.columns))
# Add a checkbox in the second column. Display the column data-types of 'census_df' on the click of checkbox.
df = pd.DataFrame({'Column Data-Type': census_df.dtypes})
with col2:
	if st.checkbox("View column data-types"):
		st.dataframe(df)

# Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
with col3:
      if st.checkbox("View column data"):
        columns_data = st.selectbox("Select_columns" , ('age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income'))
        if columns_data == "age":
          st.write(census_df["age"]) 

        elif columns_data == "workclass":
          st.write(census_df["workclass"])

        elif columns_data == "fnlwgt":
          st.write(census_df["fnlwgt"])

        elif columns_data == "education":
          st.write(census_df["education"])

        elif columns_data == "education-years":
          st.write(census_df["education-years"])

        elif columns_data == "marital-status":
          st.write(census_df["marital-status"])

        elif columns_data == "occupation":
          st.write(census_df["occupation"])

        elif columns_data == "relationship":
          st.write(census_df["relationship"])

        elif columns_data == "race":
          st.write(census_df["race"])

        elif columns_data == "gender":
          st.write(census_df["gender"])

        elif columns_data == "capital-gain":
          st.write(census_df["capital-gain"])

        elif columns_data == "capital-loss":
          st.write(census_df["capital-loss"])

        elif columns_data == "hours-per-week":
          st.write(census_df["hours-per-week"]) 

        elif columns_data == "native-country":
          st.write(census_df["native-country"])                   

        else:
          st.write(cars_df['income'])
# Display summary of the dataset on the click of checkbox.
