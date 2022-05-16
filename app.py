from streamlit_dashboard import user_overview_analysis_page, \
    user_engagement_analysis_page, \
    user_experience_analysis_page, \
    user_satisfaction_analysis_page
import streamlit as st
from scripts.multiapp import MultiApp

st.set_page_config(page_title="User Analytics in the Telecommunication Industry", layout="wide")

app = MultiApp()
st.sidebar.markdown("""
### User Analytics in the Telecommunication Industry
""")

# Add all your application here
app.add_app("User Overview Analysis", user_overview_analysis_page.app)
app.add_app("User Engagement Analysis", user_engagement_analysis_page.app)
app.add_app("User Experience Analysis", user_experience_analysis_page.app)
app.add_app("User Satisfaction Analysis", user_satisfaction_analysis_page.app)

# The main app
app.run()