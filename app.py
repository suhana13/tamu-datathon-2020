from pathlib import Path
import streamlit as st
import numpy as np
import pandas as pd
## Side bar line graphs
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
url1 = 'https://drive.google.com/uc?id=1mPK8_AasPMdqy3D9D0kxjjKcIXmhhcQo'
df = pd.read_csv(url1, sep = ',')


import matplotlib.pyplot as plt
majors = df.majors.apply(eval).explode().value_counts()[:10]
df['tech'] = df['technology_experience']
tech = df.tech.apply(eval).explode().value_counts()[:8]
classify = df.classification.value_counts()
st.sidebar.markdown("Diversity of Majors")
st.sidebar.line_chart(majors)
st.sidebar.markdown("The array of tech tool knowledge")
st.sidebar.line_chart(tech) 
st.sidebar.markdown("Classification of participants")
st.sidebar.line_chart(classify)

## Read intro markdown file
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()


intro_markdown = read_markdown_file("introduction.md")
st.markdown(intro_markdown, unsafe_allow_html=True)

## Importing rand_num file and its contents
import rand_num
from rand_num import user
user

## Importing the team building
mid_markdown = read_markdown_file("dream_team.md")
st.markdown(mid_markdown, unsafe_allow_html=True)
import team_building
from team_building import build_result
build_result

nlp_markdown = read_markdown_file("NLP.md")
st.markdown(nlp_markdown, unsafe_allow_html=True)
def icon(icon_name):
   st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

icon("search")

import workshop
##workshop.enter_queries("search")
user_input = st.text_input(" ")
button_clicked = st.button("OK")
output = workshop.enter_queries(user_input)
user_input
output

img_1 = 'datavis.PNG'
st.image(img_1, width=700)

img_2 = 'pie-chart.png'
st.image(img_2, width=700)