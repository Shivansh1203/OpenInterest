import streamlit as st
import pandas as pd
import requests
# from streamlit_lottie import st_lottie
import smtplib
# import datetime
# import matplotlib.pyplot as plt
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
        st.write("MQH is a comprehensive online platform dedicated to providing data visualization and in-depth analysis of major moves in international markets. With a focus on empowering traders and investors, MQH offers a range of tools and resources to delve into market trends, enabling users to scrutinize charts and identify trading opportunities with precision.")
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
lottie_coding_1 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# lottie_coding_2 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_2cwDXD.json")

st.sidebar.header('MQH')
st.sidebar.header("Select The Parameters:")

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
       
        st_lottie(lottie_coding_1, height=300, key="coding")

def plot_line_chart_with_slider(df, y_column, start_date, end_date, title):
    # Convert start_date and end_date to datetime objects
    start_datetime = pd.Timestamp(start_date)
    end_datetime = pd.Timestamp(end_date)
    
    # Filter dataframe based on selected date range
    mask = (df['Timestamp'] >= start_datetime) & (df['Timestamp'] <= end_datetime)
    filtered_df = df.loc[mask]

    # Sort dataframe by 'Timestamp'
    filtered_df = filtered_df.sort_values(by='Timestamp')

    # Create a Plotly figure
    fig = go.Figure()

    # Add trace for the selected column
    fig.add_trace(go.Scatter(x=filtered_df['Timestamp'], y=filtered_df[y_column], name=y_column, mode='lines'))

    # Update layout with title and slider
    fig.update_layout(
        title=title,
        xaxis=dict(title='Timestamp', rangeslider=dict(visible=True), type='date'),
        yaxis=dict(title=y_column, autorange=True),
        hovermode='x unified'
    )

    # Show the Plotly figure
    st.plotly_chart(fig)

def plot_scatter_chart(df, x_column, y_column, start_date, end_date, title):
    # Convert start_date and end_date to datetime objects
    start_datetime = pd.Timestamp(start_date)
    end_datetime = pd.Timestamp(end_date)
    
    # Filter dataframe based on selected date range
    mask = (df['Timestamp'] >= start_datetime) & (df['Timestamp'] <= end_datetime)
    filtered_df = df.loc[mask]

    # Create a Plotly figure
    fig = go.Figure()

    # Add trace for scatter plot
    fig.add_trace(go.Scatter(x=filtered_df[x_column], y=filtered_df[y_column], mode='markers', name='Data points'))

    # Update layout with title and axis labels
    fig.update_layout(
        title=title,
        xaxis=dict(title=x_column),
        yaxis=dict(title=y_column),
        hovermode='x unified'
    )

    # Show the Plotly figure
    st.plotly_chart(fig)

def plot_heatmap(df):
    # Sort the DataFrame by 'Timestamp' column
    df = df.sort_values(by='Timestamp')
    
    # Convert 'Timestamp' column to datetime format
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    # Extract year and month from 'Timestamp' column
    df['Year'] = df['Timestamp'].dt.year
    df['Month'] = df['Timestamp'].dt.month_name()

    # Define the correct order of months
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Convert 'Month' column to categorical type with the correct order of months
    df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

    # Group by year and month and calculate the mean of 'Market Open Interest'
    heatmap_data = df.groupby(['Year', 'Month'])['Market Open Interest'].mean().reset_index()

    # Pivot the dataframe for plotting heatmap
    heatmap_data_pivot = heatmap_data.pivot(index='Month', columns='Year', values='Market Open Interest')

    # Create a Plotly heatmap
    fig = go.Figure(data=go.Heatmap(
        z=heatmap_data_pivot.values,
        x=heatmap_data_pivot.columns,
        y=heatmap_data_pivot.index,
        colorscale='ylgn'))

    # Update layout with title and axis labels
    fig.update_layout(
        title='Market Open Interest Heatmap (Years vs Months)',
        xaxis=dict(title='Year'),
        yaxis=dict(title='Month'),
        hovermode='x unified'
    )

    # Show the Plotly heatmap
    st.plotly_chart(fig)


# Daily Range Heatmap
def plot_heatmap1(df):
    # Sort the DataFrame by 'Timestamp' column
    df = df.sort_values(by='Timestamp')
    
    # Convert 'Timestamp' column to datetime format
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    # Extract year and month from 'Timestamp' column
    df['Year'] = df['Timestamp'].dt.year
    df['Month'] = df['Timestamp'].dt.month_name()

    # Define the correct order of months
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Convert 'Month' column to categorical type with the correct order of months
    df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

    # Group by year and month and calculate the mean of 'Daily Range'
    heatmap_data1 = df.groupby(['Year', 'Month'])['Daily Range'].mean().reset_index()

    # Pivot the dataframe for plotting heatmap
    heatmap_data_pivot1 = heatmap_data1.pivot(index='Month', columns='Year', values='Daily Range')

    # Create a Plotly heatmap
    fig1 = go.Figure(data=go.Heatmap(
        z=heatmap_data_pivot1.values,
        x=heatmap_data_pivot1.columns,
        y=heatmap_data_pivot1.index,
        colorscale='Viridis'))

    # Update layout with title and axis labels
    fig1.update_layout(
        title='Daily Range Heatmap (Years vs Months)',
        xaxis=dict(title='Year'),
        yaxis=dict(title='Month'),
        hovermode='x unified'
    )

    # Show the Plotly heatmap
    st.plotly_chart(fig1)


#Greater MOI

def plot_heatmap2(df):
    # Sort the DataFrame by 'Timestamp' column
    df = df.sort_values(by='Timestamp')
    
    # Convert 'Timestamp' column to datetime format
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    # Extract year and month from 'Timestamp' column
    df['Year'] = df['Timestamp'].dt.year
    df['Month'] = df['Timestamp'].dt.month_name()

    # Define the correct order of months
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Convert 'Month' column to categorical type with the correct order of months
    df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

   
     # Group by year and month and calculate the count of occurrences of 'Greater MOI' equal to 1
    heatmap_data2 = df[df['Greater MOI'] == 1].groupby(['Year', 'Month']).size().reset_index(name='Count')

    # Pivot the dataframe for plotting heatmap
    heatmap_data_pivot2 = heatmap_data2.pivot(index='Month', columns='Year', values='Count')

    # Create a Plotly heatmap
    fig2 = go.Figure(data=go.Heatmap(
        z=heatmap_data_pivot2.values,
        x=heatmap_data_pivot2.columns,
        y=heatmap_data_pivot2.index,
        colorscale="Viridis"))

    # Update layout with title and axis labels
    fig2.update_layout(
        title='Greater MOI Heatmap (Years vs Months)  (10 Day Moving Average)',
        xaxis=dict(title='Year'),
        yaxis=dict(title='Month'),
        hovermode='x unified'
    )

    # Show the Plotly heatmap
    st.plotly_chart(fig2)

#Greater DR
    
def plot_heatmap3(df):
    # Sort the DataFrame by 'Timestamp' column
    df = df.sort_values(by='Timestamp')
    
    # Convert 'Timestamp' column to datetime format
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    # Extract year and month from 'Timestamp' column
    df['Year'] = df['Timestamp'].dt.year
    df['Month'] = df['Timestamp'].dt.month_name()

    # Define the correct order of months
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Convert 'Month' column to categorical type with the correct order of months
    df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

    # Group by year and month and calculate the count of occurrences of 'Greater DR' equal to 1
    heatmap_data3 = df[df['Greater DR'] == 1].groupby(['Year', 'Month']).size().reset_index(name='Count')

    # Pivot the dataframe for plotting heatmap
    heatmap_data_pivot3 = heatmap_data3.pivot(index='Month', columns='Year', values='Count')

    # Create a Plotly heatmap
    fig3 = go.Figure(data=go.Heatmap(
        z=heatmap_data_pivot3.values,
        x=heatmap_data_pivot3.columns,
        y=heatmap_data_pivot3.index,
        colorscale="Viridis"))

    # Update layout with title and axis labels
    fig3.update_layout(
        title='Greater DR Heatmap (Years vs Months) (10 Day Moving Average)',
        xaxis=dict(title='Year'),
        yaxis=dict(title='Month'),
        hovermode='x unified'
    )

    # Show the Plotly heatmap
    st.plotly_chart(fig3)
# Streamlit UI
st.title('CSV Viewer')

# Fetch all CSV files from the current directory
csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]

# Dropdown menu to select a CSV file
selected_csv = st.sidebar.selectbox("Choose a CSV file", csv_files)

if selected_csv:
    # Read the selected CSV file
    df = pd.read_csv(selected_csv)
    
    # Display the dataframe (optional)
    st.write("Selected CSV data:")
    st.write(df)
    
    # Convert 'Timestamp' column to datetime format
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    # Date range selection for Market Open Interest and Daily Range
    min_date = df['Timestamp'].min().date()
    max_date = df['Timestamp'].max().date()
    start_date = st.sidebar.date_input('Start date', min_value=min_date, max_value=max_date, value=min_date)
    end_date = st.sidebar.date_input('End date', min_value=min_date, max_value=max_date, value=max_date)
    
    # Plot Market Open Interest chart
    st.subheader("Market Open Interest Line Chart")
    plot_line_chart_with_slider(df, 'Market Open Interest', start_date, end_date, "Market Open Interest")

    # Plot Daily Range chart
    st.subheader("Daily Range Line Chart")
    plot_line_chart_with_slider(df, 'Daily Range', start_date, end_date, "Daily Range")

    # Plot scatter chart for Market Open Interest and Daily Range
    st.subheader("Market Open Interest vs. Daily Range Scatter Plot")
    plot_scatter_chart(df, 'Market Open Interest', 'Daily Range', start_date, end_date, "Market Open Interest vs. Daily Range")

    # Date range selection for "Greater MOI"
    st.subheader("Number of Times Market Open Interest is Greater than 10 Day Moving Average")
    moi_start_date = st.date_input('Start date for Greater MOI/DR', min_value=min_date, max_value=max_date, value=min_date)
    moi_end_date = st.date_input('End date for Greater MOI/DR', min_value=min_date, max_value=max_date, value=max_date)
    
    # Filter dataframe based on selected date range for Greater MOI
    mask = (df['Timestamp'] >= pd.Timestamp(moi_start_date)) & (df['Timestamp'] <= pd.Timestamp(moi_end_date))
    filtered_moi_df = df.loc[mask]
    
    # Check if 'Greater MOI' column exists
    if 'Greater MOI' in filtered_moi_df.columns:
        # Count occurrences of Greater MOI equal to 1
        moi_count = filtered_moi_df[filtered_moi_df['Greater MOI'] == 1].shape[0]
        st.write(f"Number of times MOI is Greater than 10 Day Moving Average: {moi_count}")
    else:
        st.write("The 'Greater MOI' column does not exist in the selected data.")



    st.subheader("Number of Times Daily Range is Greater than 10 Day Moving Average")
    
    # Filter dataframe based on selected date range for Greater MOI
    mask = (df['Timestamp'] >= pd.Timestamp(moi_start_date)) & (df['Timestamp'] <= pd.Timestamp(moi_end_date))
    filtered_dr_df = df.loc[mask]
    
    # Check if 'Greater MOI' column exists
    if 'Greater DR' in filtered_dr_df.columns:
        # Count occurrences of Greater MOI equal to 1
        dr_count = filtered_dr_df[filtered_moi_df['Greater DR'] == 1].shape[0]
        st.write(f"Number of times DR is Greater than 10 Day Moving Average: {dr_count}")
    else:
        st.write("The 'Greater DR' column does not exist in the selected data.")

    plot_heatmap(df)
    plot_heatmap1(df)
    plot_heatmap2(df)
    plot_heatmap3(df)


# ---- WHAT I DO ----
# with st.container():
#     st.write("---")
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.header("What we do")
#         st.write("##")
#         st.write(
#             """
#            MQH is a comprehensive online platform dedicated to providing data visualization and in-depth analysis of major moves in international markets. With a focus on empowering traders and investors, MQH offers a range of tools and resources to delve into market trends, enabling users to scrutinize charts and identify trading opportunities with precision. By offering a closer perspective on market dynamics, MQH equips users with valuable insights to make informed decisions and navigate the complexities of global trading effectively
           
#             """
#         )
#         st.write("[Our Repository >]()")
#     with right_column:
       
#         st_lottie(lottie_coding_1, height=300, key="coding")

       


# st.sidebar.header('MQH 2011-2014')
# st.sidebar.header("Select The Parameters:")


st.sidebar.markdown('''
---
Created with ❤️ by [Shivansh](https://github.com/Shivansh1203/MQH).
''')






# ---- PROJECTS ----
# with st.container():
#     st.write("---")
#     st.header("Our Approach")
#     text_column, image_column= st.columns((2))
#     with text_column:
#         st.subheader("")
#         st.write(
#             """
#            MQH is a comprehensive online platform dedicated to providing data visualization and in-depth analysis of major moves in international markets. With a focus on empowering traders and investors, MQH offers a range of tools and resources to delve into market trends, enabling users to scrutinize charts and identify trading opportunities with precision. By offering a closer perspective on market dynamics, MQH equips users with valuable insights to make informed decisions and navigate the complexities of global trading effectively
#             """
#         )

#     with image_column:

#             image = Image.open('images/mqh_logo.jpeg')

#             resized_image = image.resize((300, 300))  

#             st.image(resized_image)

# with st.container():
#         st.subheader("Our Vision")
#         st.write(
#             """
#             MQH is a comprehensive online platform dedicated to providing data visualization and in-depth analysis of major moves in international markets. With a focus on empowering traders and investors, MQH offers a range of tools and resources to delve into market trends, enabling users to scrutinize charts and identify trading opportunities with precision. By offering a closer perspective on market dynamics, MQH equips users with valuable insights to make informed decisions and navigate the complexities of global trading effectively
#             """
#         )
    
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


