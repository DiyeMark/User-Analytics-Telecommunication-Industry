from streamlit_dashboard import user_overview_analysis_page
# from streamlit_dashboard import user_engagement
# from streamlit_dashboard import user_experience
# from streamlit_dashboard  import user_satisfaction
import streamlit as st
from scripts.multiapp import MultiApp

st.set_page_config(page_title="User Analytics in the Telecommunication Industry", layout="wide")

app = MultiApp()
st.sidebar.markdown("""
# User Analytics in the Telecommunication Industry
### Multi-Page App
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
### Modifications
\t- Page Folder Based Access
\t- Presentation changed to SideBar
""")

# Add all your application here
app.add_app("User Overview Analysis", user_overview_analysis_page.app)
# app.add_app("User Engagement Analysis", user_engagement_analysis_page.app)
# app.add_app("User Experience Analysis", user_experience_analysis_page.app)
# app.add_app("User Satisfaction Analysis", user_satisfaction_analysis_page.app)
# app.add_app("Predict Satisfaction", model_implementation.app)

# The main app
app.run()

