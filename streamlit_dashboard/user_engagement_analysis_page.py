import streamlit as st
from scripts.pickler import Pickler
import sys
sys.path.insert(0, '../scripts')


def app():
    # Load Saved Results Data
    results = Pickler()
    results.load_data(file_name='./data/engagement.pickle')

    st.title("User Engagement analysis")

    st.header("Top 10 Users")
    st.subheader("Based on: Session Count")
    st.dataframe(results.data['top_10_session'])

    st.subheader("Based on: Total Duration (hr)")
    st.dataframe(results.data['top_10_duration'])

    st.subheader("Based on: Total Data Traffic (MegaBytes)")
    st.dataframe(results.data['top_10_total_traffic'])

    st.header("Top 10 Users Engaged Per Each Application")
    st.subheader("Social Media App")
    st.dataframe(results.data['top_10_socialmedia_users'])

    st.subheader("Google")
    st.dataframe(results.data['top_10_google_users'])

    st.subheader("Email")
    st.dataframe(results.data['top_10_email_users'])

    st.subheader("Youtube")
    st.dataframe(results.data['top_10_youtube_users'])

    st.subheader("Netflix")
    st.dataframe(results.data['top_10_netflix_users'])

    st.subheader("Gaming")
    st.dataframe(results.data['top_10_gaming_users'])

    st.subheader("Other Apps")
    st.dataframe(results.data['top_10_other_users'])

    st.header("Top 3 Most Used Applications")
    st.dataframe(results.data['most_used_apps'])
