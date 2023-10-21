import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt


header = st.container()
dataset = st.container()

with header:
    st.title("Welcome to my project!...")

with dataset:
    st.header("Welcome to Titanic dataset")
    st.text("Click here to show dataset")
    data = pd.read_csv('Data/Titanic-Dataset.csv')

    
    if st.button('Show Dataset'):
        df = pd.DataFrame(data)
        st.dataframe(df.head(10))
        
        df = pd.DataFrame(data)
        embarked_count = df['Embarked'].value_counts()
        plt.figure(figsize=(4,4))
        plt.pie(embarked_count.values, labels = embarked_count.index, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.title("Embarked Distribution")
        st.pyplot(plt)
        
        plt.figure(figsize=(4,4))
        sex_counts = df['Sex'].value_counts()
        plt.bar(sex_counts.index, sex_counts.values, color=['green', 'yellow'])
        plt.xlabel('Sex')
        plt.ylabel('Count')
        plt.title('Sex Distribution')
        st.pyplot(plt)