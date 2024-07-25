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

    title = 'Sustainable Capacity of Local Organizations to Reach and End the HIV/AIDS Pandemic (SCORE) -- UMMB'
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
    ### ACKNOWLEDGEMENT

    The “Sustainable Capacity of Local Organizations to Reach and End the HIV/AIDS Pandemic (SCORE)” Project is funded by the US Centers for Disease Control and Prevention (CDC)/PEPFAR through the global award NU2GGH002503. (September 2023 – September 2028).

    Implemented by Georgetown University (Center for Global Health Practice and Impact, O’Neill Institute for National and Global Health Law, Center for Global Health Science and Security, Department of Global Health, McCourt School of Public Policy, McDonough Business School), and partners Sustainability Solutions and Aspen Institute, the SCORE Project is designed to provide governments, faith-based organizations and community-based organizations with support to sustain HIV and related disease outcome gains and strengthen local capacity for resilient and equitable country health systems. 

    The SCORE Project is designed to provide governments, faith-based organizations, and community-based organizations with support to sustain HIV and related disease outcome gains and strengthen local capacity for resilient and equitable country health systems.

    The SCORE HIV/AIDS Pandemic Organizational and Technical Needs Assessment Tool (SCORE-POT) is designed to assess existing organizational capacity to manage and deliver sustainable HIV programs. The tool reviews six modules:

    1. **Module 1: Governance and Leadership**
    2. **Module 2: Program Management**
    3. **Module 3: Technical Assistance**
    4. **Module 4: Data Use**
    5. **Module 5: Sustainability**
    6. **Module 6: Finance and Administration**

    The SCORE-POT has been developed by the SCORE Project with additions, adaptations and modifications from the USAID Non-U.S. Organization Pre-Award Survey (NUPAS) tool, the PEPFAR Strategic Direction (September 2022), and the Americorps Organizational Assessment Tool, Washington DC (2017), and the PEPFAR Rapid Site-level Health Workforce Assessment Tool.
    """)

    st.markdown("""
    ### INTRODUCTION

    In Uganda, the SCORE Project is providing technical assistance to selected faith-based and community-based organizations to strengthen their organizational, leadership, and management capacities to manage and deliver sustainable HIV programs. The capacity and needs assessment is the first step towards building capacity and is conducted through the use of a standardized process or formal instrument to assess facets of organizational capacity and identify areas of relative strength and weakness.

    Through applying the SCORE Pandemic Organizational and Technical Needs Assessment Tool (SCORE-POT), the Project will collaborate with your organization to assess institutional capacity to implement locally driven innovations to sustain HIV epidemic control, support long-term planning, address emerging challenges, and implement adaptive programming.

    The SCORE-POT will be administered in collaboration with the CDC and the following partners:
    - **AIDS Information Centre (AIC)**
    - **Reach Out Mbuya (ROM)**
    - **Uganda Episcopal Conference (UEC)**
    - **Uganda Protestant Medical Bureau (UPMB)**
    - **Uganda Muslim Medical Bureau (UMMB)**
    """)
                            
    st.markdown("""
    ### USAGE
    This dashboard is designed to allow audiences to explore and analyze scoring data across different dimensions. Here are the details of the three sub-tabs:

    1. **Tab 1: Institution Comparison** - Compare how different institutions score on a specific question.
    2. **Tab 2: Score Filtering** - Filter and view questions that meet certain score criteria.
    3. **Tab 3: Section Analysis** - Examine the scores of various questions within a selected section for a specific institution.

    Feel free to explore any tab to interact with the data!
    """)





if __name__ == "__main__":
    app()
