import streamlit as st
import seaborn as sns

# Load the tips dataset
tips = sns.load_dataset('tips')

# Sidebar for plot selection
plot_options = ['Histogram', 'Scatterplot', 'Boxplot', 'Pairplot']
selected_plot = st.sidebar.selectbox('Select Plot Type', plot_options)

# Main content area
st.title('Tips Dataset Plotting App')

if selected_plot == 'Histogram':
    # Plot a histogram
    st.subheader('Histogram')
    column = st.selectbox('Select a column', tips.columns)
    sns.histplot(tips[column])
    st.pyplot()

elif selected_plot == 'Scatterplot':
    # Plot a scatterplot
    st.subheader('Scatterplot')
    x_column = st.selectbox('Select X-axis column', tips.columns)
    y_column = st.selectbox('Select Y-axis column', tips.columns)
    sns.scatterplot(data=tips, x=x_column, y=y_column)
    st.pyplot()

elif selected_plot == 'Boxplot':
    # Plot a boxplot
    st.subheader('Boxplot')
    x_column = st.selectbox('Select X-axis column', tips.columns)
    y_column = st.selectbox('Select Y-axis column', tips.columns)
    sns.boxplot(data=tips, x=x_column, y=y_column)
    st.pyplot()

# plot a pair plot
else:
    st.subheader('Pairplot')
    sns.pairplot(tips)
    st.pyplot()
