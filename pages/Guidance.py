import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import altair as alt 
import numpy as np
 

# Import the dataset
image = "CGHPI.png"


# Streamlit application
def app():
    # Main page content
    st.set_page_config(page_title = 'UMMB Dashboard -- Uganda SCORE Survey', page_icon='🇺🇬',layout='wide')

    #st.image(image, width=200, use_column_width=False)
    #st.title('Sustainable Capacity of Local Organizations to Reach and End the HIV/AIDS Pandemic (SCORE)')

    title = 'Guidance for this dashboard'
    col1, col2, col3 = st.columns([4, 1, 5])

    with col1:
        st.write("")

    with col2:
        st.image(image, width=250)

    with col3:
        st.write("")

    # Center the image and title using HTML and CSS in Markdown
    st.markdown(
        f"""
        <style>
        .centered {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 30vh;
            text-align: center;
        }}
        </style>
        <div class="centered">
            <h1 style='text-align: center'>{title}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    ### 1. Institution Comparison

    This tab allows the CDC to compare the performance of different institutions on each question. Select your module, section, and specific question, then choose the visualization type you'd like to see.
    """)

    st.markdown("""
    ### 2. Metric Check

    Use this tab to review the metrics used to score each question. Select the module and section through the selection bar to view the metrics for each module.
    """)

    st.markdown("""
    ### 3. Score Filtering

    This tab is designed for institutions to filter questions based on the scores of interest. Select the institution name and the score(s) you are interested in.
    """)

    st.markdown("""
    ### 4. Section Analysis

    This tab allows for section analysis. Select the institution, module, and section you want to review to easily see the performance of the questions within that section. If you're curious about scores within a certain range, you can also select those scores in the selection bar.
    """)

    
if __name__ == "__main__":
    app()