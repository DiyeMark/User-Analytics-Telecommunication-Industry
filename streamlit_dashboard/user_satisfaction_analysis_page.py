import streamlit as st
from scripts.pickler import Pickler
import sys
sys.path.insert(0, '../scripts')


def app():

    # Load Saved Results Data
    results = Pickler()
    results.load_data(file_name='./data/satisfaction.pickle')

    st.title("User Satisfaction analysis")

    st.header("Engagement Score")
    st.subheader("Sample Users")
    st.dataframe(results.data['engagement_score'].sample(10))

    st.header("Experience Score")
    st.subheader("Sample Users")
    st.dataframe(results.data['experience_score'].sample(10))

    st.header("Top 10 Satisfied Customers")
    st.subheader(
        "satisfaction score = average of both engagement & experience scores")
    st.dataframe(results.data['top_10_satisfied_customers'])

    st.header("Trained Model")
    st.subheader("Details")
    data = results.data['model_desc']
    for key in data:
        text = f'{key}: {data[key]}'
        st.text(text)

    st.header('Aggregate Metrics of all Users')
    st.dataframe(results.data['statisfaction_agg_cluster'])
