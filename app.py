import streamlit as st
import pandas as pd
from prophet.plot import plot_plotly
import plotly.express as px
import requests
from streamlit_lottie import st_lottie
import smtplib
import datetime
import matplotlib.pyplot as plt
import os
from PIL import Image
import plotly.graph_objects as go


st.set_page_config(page_title="MQH", page_icon=":tada:", layout="wide")
# ---- HEADER SECTION ----
with st.container():
    c1, c2 = st.columns(2)
    with c1:
        st.title("MQH")
        st.write(
            "Stay Ahead of the Game with MQH."
        )
        st.write("Hello")
    with c2:
          
            image = Image.open('images/mqh_logo.jpeg')

            resized_image = image.resize((300, 300))

            st.image(resized_image)




def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Description
def info(title, text):
    with st.expander(f"{title}"):
        st.write(text)

local_css("style/style.css")

# ---- LOAD ASSETS ----
# lottie_coding_1 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# lottie_coding_2 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_2cwDXD.json")



# def reshape_csv_table(csv_file):
#     # Read the CSV file
#     df = pd.read_csv(csv_file)
    
#     # Initialize empty lists for Timestamp and Value
#     timestamps = []
#     values = []
    
#     # Iterate through each row in the dataframe
#     for index, row in df.iterrows():
#         # Iterate through each column in the row
#         for column in df.columns:
#             # If the column name starts with "Timestamp"
#             if column.startswith('Timestamp'):
#                 # Get the timestamp value
#                 timestamp = row[column]
#                 # If the timestamp value is not NaN
#                 if pd.notna(timestamp):
#                     # Append the timestamp value to the list
#                     timestamps.append(timestamp)
#                     # Extract the corresponding value from the row
#                     value_col = column.replace('Timestamp', '')
#                     value = row[value_col.strip('. ')]
#                     # Append the corresponding value to the list
#                     values.append(value)
    
#     # Create a new dataframe with Timestamp and Value columns
#     new_df = pd.DataFrame({'Timestamp': timestamps, 'Value': values})
    
#     # Remove rows with NaN values in the "Value" column
#     new_df = new_df.dropna(subset=['Value'])
    
#     # Convert Timestamp column to datetime
#     new_df['Timestamp'] = pd.to_datetime(new_df['Timestamp'], format='%d-%m-%Y', errors='coerce')
    
#     # Sort the dataframe by Timestamp in ascending order
#     new_df = new_df.sort_values(by='Timestamp')
    
#     # Remove rows with NaN values after sorting
#     new_df = new_df.dropna(subset=['Timestamp'])
    
#     return new_df

# def calculate_statistics(df):
#     value_range = df['Value'].max() - df['Value'].min()
#     highest_value = df['Value'].max()
#     lowest_value = df['Value'].min()
#     return value_range, highest_value, lowest_value

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What we do")
        st.write("##")
        st.write(
            """
           MQH is a comprehensive online platform dedicated to providing data visualization and in-depth analysis of major moves in international markets. With a focus on empowering traders and investors, MQH offers a range of tools and resources to delve into market trends, enabling users to scrutinize charts and identify trading opportunities with precision. By offering a closer perspective on market dynamics, MQH equips users with valuable insights to make informed decisions and navigate the complexities of global trading effectively
           
            """
        )
        st.write("[Our Repository >]()")
    with right_column:
       
        # st_lottie(lottie_coding_1, height=300, key="coding")

       st.title('CSV Viewer and Data Visualization')

# Fetch all CSV files from the current directory
# csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]

st.sidebar.header('MQH 2011-2014')
st.sidebar.header("Select The Parameters:")
csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]
# selected_csv = st.sidebar.selectbox("Choose a CSV file", csv_files)
# Fetch all CSV files from the current directory

# Multiselect menu to select multiple CSV files
selected_csvs = st.sidebar.multiselect("Choose CSV files", csv_files)

st.sidebar.markdown('''
---
Created with ❤️ by [Shivansh](https://github.com/Shivansh1203/MQH).
''')


# if selected_csvs:
#     # # Process the selected CSV file
#     # dataframe = reshape_csv_table(selected_csvs)
    
#     # # Display the dataframe (optional)
#     # st.write(dataframe)
    
#     # # Convert minimum and maximum Timestamp values to datetime objects
#     # min_timestamp = pd.to_datetime(dataframe['Timestamp'].min(), format='%d-%m-%Y')
#     # max_timestamp = pd.to_datetime(dataframe['Timestamp'].max(), format='%d-%m-%Y')
#      # Process the selected CSV files
#     dataframes = [reshape_csv_table(csv_file) for csv_file in selected_csvs]
    
#     for idx, dataframe in enumerate(dataframes):
#         st.subheader(f"CSV File {idx + 1}")
#         st.write(dataframe)
    
#     # Convert minimum and maximum Timestamp values to datetime objects
#     min_timestamp = min(df['Timestamp'].min() for df in dataframes)
#     max_timestamp = max(df['Timestamp'].max() for df in dataframes)
    

#     # Set default start and end dates
#     # default_start_date = pd.Timestamp('2011-02-16') 
#     # default_end_date = pd.Timestamp('2014-08-14')



#     start_date = st.sidebar.date_input('Start date', min_value=min_timestamp.date(), max_value=max_timestamp.date(), value=min_timestamp.date())
#     end_date = st.sidebar.date_input('End date', min_value=min_timestamp.date(), max_value=max_timestamp.date(), value=max_timestamp.date())

#      # Filter the dataframes based on the selected date range
#     filtered_dfs = []
#     for dataframe in dataframes:
#         mask = (dataframe['Timestamp'] >= pd.Timestamp(start_date)) & (dataframe['Timestamp'] <= pd.Timestamp(end_date))
#         filtered_df = dataframe.loc[mask]
#         filtered_dfs.append(filtered_df)
    
#     # Plotting with Plotly
#     for idx, filtered_df in enumerate(filtered_dfs):
#         if not filtered_df.empty:
#             st.subheader(f"Plot for CSV File {idx + 1}")
#             st.write("Hover over the plot to see data values.")
#             fig = px.line(filtered_df, x='Timestamp', y='Value', title=f'Value over Time (CSV File {idx + 1})', labels={'Timestamp': 'Timestamp', 'Value': 'Value'})
#             fig.update_xaxes(rangeslider_visible=True)  # Add range slider for zooming
#             st.plotly_chart(fig)

#              # Calculate statistics
#             value_range, highest_value, lowest_value = calculate_statistics(filtered_df)
#             st.write(f'**Range of values:** {value_range}')
#             st.write(f'**Highest value:** {highest_value}')
#             st.write(f'**Lowest value:** {lowest_value}')

#         else:
#             st.write(f"No data available for CSV File {idx + 1}.")
    # dataframe['Timestamp'] = pd.to_datetime(dataframe['Timestamp'], format='%d-%m-%Y')
    
    # # Filter the dataframe based on the selected date range
    # mask = (dataframe['Timestamp'] >= pd.Timestamp(start_date)) & (dataframe['Timestamp'] <= pd.Timestamp(end_date))
    # filtered_df = dataframe.loc[mask]
    
 
    # if not filtered_df.empty:
   
    #     st.subheader("Detailed Plot")
    #     st.write("Hover over the plot to see data values.")
    #     fig = px.line(filtered_df, x='Timestamp', y='Value', title='Value over Time', labels={'Timestamp': 'Timestamp', 'Value': 'Value'})
    #     fig.update_xaxes(rangeslider_visible=True)  # Add range slider for zooming
    #     st.plotly_chart(fig)
    # else:
    #     st.write("No data available for the selected date range.")
    

    # if not filtered_df.empty:
    #     st.subheader("General Trend")
    #     st.line_chart(filtered_df.set_index('Timestamp'))
        
    #     # Calculate range of values
    #     value_range = filtered_df['Value'].max() - filtered_df['Value'].min()
    #     st.write(f'**Range of values:** {value_range}')
        
    #     # Calculate highest and lowest values
    #     highest_value = filtered_df['Value'].max()
    #     lowest_value = filtered_df['Value'].min()
    #     st.write(f'**Highest value:** {highest_value}')
    #     st.write(f'**Lowest value:** {lowest_value}')
    # else:
    #     st.write("No data available for the selected date range.")




# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Our Approach")
    text_column, image_column= st.columns((2))
    with text_column:
        st.subheader("")
        st.write(
            """
           MQH is a comprehensive online platform dedicated to providing data visualization and in-depth analysis of major moves in international markets. With a focus on empowering traders and investors, MQH offers a range of tools and resources to delve into market trends, enabling users to scrutinize charts and identify trading opportunities with precision. By offering a closer perspective on market dynamics, MQH equips users with valuable insights to make informed decisions and navigate the complexities of global trading effectively
            """
        )

    with image_column:

            image = Image.open('images/mqh_logo.jpeg')

            resized_image = image.resize((300, 300))  

            st.image(resized_image)

with st.container():
        st.subheader("Our Vision")
        st.write(
            """
            MQH is a comprehensive online platform dedicated to providing data visualization and in-depth analysis of major moves in international markets. With a focus on empowering traders and investors, MQH offers a range of tools and resources to delve into market trends, enabling users to scrutinize charts and identify trading opportunities with precision. By offering a closer perspective on market dynamics, MQH equips users with valuable insights to make informed decisions and navigate the complexities of global trading effectively
            """
        )
    
# ---- CONTACT ----

with st.container():
    st.write("---")
    st.header("Get In Touch With Us")
    st.write("##")

 
    def send_email(name, email, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("epicstruchain@gmail.com", "imttyfmbkriojftd")
        msg = f"Subject: New message from {name}\n\n{name} ({email}) sent the following message:\n\n{message}"
        server.sendmail("epicstruchain@gmail.com", "epicstruchain@gmail.com", msg)
        st.success("Thank you for contacting us.")
        
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    if st.button("Send"):
        send_email(name, email, message)

    
    st.markdown(
    """
    <style>
       
         /* Adjust the width of the form elements */
        .stTextInput {
            width: 50%;
        }
        
        .stTextArea {
            width: 20%;
        }
        /* Style the submit button */
        .stButton button {
            background-color: #45a049;
            color: #FFFFFF;
            font-weight: bold;
            padding: 10px;
            border-radius: 5px;
            width: 10%;
        }
        /* Style the success message */
        .stSuccess {
            color: #0072C6;
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


