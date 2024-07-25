import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import altair as alt 
import plotly.express as px


# Import the dataset
image = "CGHPI.png"
df = pd.read_csv('final_uganda.csv', encoding='ISO-8859-1')
df['Institution'] = df['Program']
df['question'] = df['Qn']
df['Module'] = df['Module'].replace('One','One: Leadership and Governance').replace('Two','Two: Program Management').replace('Three','Three: Technical Assistance').\
replace('Four','Four: Data Use').replace("Five","Five: Sustainability")
# Define conditions and choices for the text labels
conditions = [
    df['Score'] == 1,
    df['Score'] == 2,
    df['Score'] == 3,
    df['Score'] == 4,
    df['Score'] == 5
]
choices = ['Nonexistent', 'Basic', 'Adequate', 'Comprehensive', 'Exceptional']

# Apply conditions and choices
df['Level'] = np.select(conditions, choices, default='Not Applicable')

# Streamlit application
def app():
    # Main page content
    st.set_page_config(page_title = 'UMMB Dashboard -- Uganda SCORE Survey', page_icon='🇺🇬',layout='wide')

    title = 'Comparison of Scores of Questions Within One Section Within UMMB'
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
            <h2 style='text-align: center'>{title}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.sidebar.title('Enter your selections here!')

    # Ensure the Score column is sorted
    #program_selected = st.sidebar.selectbox('Select Institution', df['Program'].unique())
    module_selected = st.sidebar.selectbox('Select Module', df['Module'].unique())
    part_selected = st.sidebar.selectbox('Select Section', df[df['Module'] == module_selected]['Part'].unique())
    st.sidebar.markdown(f"#### You selected: {part_selected}")
    
    # Available scores based on selections
    available_scores = df[(df['Program'] == 'AIC') & (df['Module'] == module_selected) & (df['Part'] == part_selected)]['Score'].unique()
    sorted_unique_scores = sorted(available_scores)

    # Button to select all scores
    if st.sidebar.button('Select All Scores'):
        st.session_state.scores_selected = list(sorted_unique_scores)
    elif 'scores_selected' not in st.session_state or module_selected != st.session_state.last_module \
        or part_selected != st.session_state.last_part:
        # Reset to the first available score by default if not 'Select All' and if part or module has changed
        st.session_state.scores_selected = sorted_unique_scores

    scores_selected = st.sidebar.multiselect(
        'Select Score(s)',
        sorted_unique_scores,
        default=st.session_state.scores_selected
    )

    st.session_state.scores_selected = scores_selected

    # Displaying the selected options in the sidebar
    scores_selected1 = [str(score) for score in scores_selected]
    if scores_selected:  # Checks if any score is selected
        st.sidebar.markdown(f"#### You selected: {', '.join(scores_selected1)}")
    else:
        st.sidebar.markdown("#### No score selected")
    
    # Update last viewed module and part
    st.session_state.last_module = module_selected
    st.session_state.last_part = part_selected
    
    plot_selected = st.sidebar.selectbox('Select Visualization Type',['Bar Plot','Pie Plot','Radar Plot','Table'],index=0)


        
    # Filter data based on selections
    filtered_data = df[(df['Module'] == module_selected) & 
                        (df['Part'] == part_selected) & 
                        (df['Program'] == 'UMMB') &
                        (df['Score'].isin(scores_selected))]
    if not filtered_data.empty:
        module_selected1 = module_selected.split(':')[1]
        if plot_selected == 'Bar Plot':
            st.write("")
            chart = alt.Chart(filtered_data).mark_bar().encode(
                y=alt.Y('Question:N', sort=alt.EncodingSortField(field='Qn', order='ascending')),
                x=alt.X('Score:Q', scale=alt.Scale(domain=[0, 6]),
                        axis=alt.Axis(values=[0, 1, 2, 3, 4, 5])),
                color=alt.Color('Question:N', sort=alt.EncodingSortField(field='Qn', order='ascending')),
                tooltip=['Question', 'Score', 'Level', 'Description']
            ).properties(
                width=600,
                height=600,
                title=f'UMMB -- Bar Plot of Scores by Question within {module_selected1}: {part_selected}'
            )

            text = chart.mark_text(
                align='left',
                baseline='middle',
                color='black'
            ).encode(
                text='Level:N',
            )

            final_chart = alt.layer(chart, text).configure_axis(
                labelFontSize=12,
                titleFontSize=14
            )

            st.altair_chart(final_chart, use_container_width=True)

        elif plot_selected == 'Pie Plot':
            st.write("")
            base = alt.Chart(filtered_data).mark_arc().encode(
                theta=alt.Theta('Score:Q').stack(True),  
                color=alt.Color('Question:N',sort=alt.EncodingSortField(field='Qn', order='ascending')),
                tooltip=['Question', 'Score', 'Level', 'Description'] 
            )

            pie = base.mark_arc(outerRadius = 120)
            text1 = base.mark_text(radius=150, size=12).encode(text="Level:N")

            final_chart1 = alt.layer(pie, text1).properties(
                width=600,
                height=400,
                title=f'UMMB -- Pie Plot of Scores by Question within {module_selected1}: {part_selected}'
            ).configure_axis(
                labelFontSize=12,
                titleFontSize=14
            ).interactive()

            st.altair_chart(final_chart1, use_container_width=True)

        elif plot_selected == 'Radar Plot':
            filtered_data['Question1'] = 'Q' + filtered_data['Qn'].astype(str)
            fig = px.line_polar(filtered_data, r='Score', theta='Question1', line_close=True,
                                text='Level',
                                template="plotly_dark",
                                title=f'UMMB -- Radar Plot of Scores by Question within {module_selected1}: {part_selected}',
                                hover_data={
                                    'Question': True,
                                    'Score': True,  
                                    'Level': True,  
                                    'Description': True 
                                })
            
            fig.update_traces(textposition='bottom center')
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(showticklabels=True, tickangle=0),
                    angularaxis=dict(rotation=90, direction='clockwise', tickfont_size=15)
                ),
                font=dict(size=8)
            )

            st.plotly_chart(fig, use_container_width=True)
        
        else:
            filtered_data['Section'] = filtered_data['Part']
            records = filtered_data[['Institution', 'Module','Section','Question','Score','Level','Description']].reset_index().drop(columns='index')
            st.markdown(f"#### Comparison of Score by Questions in UMMB are shown below:")
            st.dataframe(records)

    else:
        st.markdown("### No data available for the selected criteria.")

if __name__ == "__main__":
    app()