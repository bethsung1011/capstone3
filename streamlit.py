import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
from statsmodels.nonparametric.smoothers_lowess import lowess
from matplotlib.backends.backend_agg import RendererAgg
from matplotlib.figure import Figure
import matplotlib
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import seaborn as sns
import statsmodels
import requests
import time
import random


# matplotlib.use("Agg")

_lock = RendererAgg.lock
plt.style.use('default')

# SETUP ------------------------------------------------------------------------

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url1 = "https://assets5.lottiefiles.com/private_files/lf30_6jzgknvg.json"
lottie_json = load_lottieurl(lottie_url1)
st_lottie(lottie_json)

st.title('Okcupid Match Making Recommender')
st.write('')
st.write('')
st.write('')


# ROW 0 ------------------------------------------------------------------------
row0_spacer1, row0_1_1, row0_spacer2, row0_1_2, row0_spacer3 = st.beta_columns(
    (.1, 1.6, .1, 3.5, .1)
    )

with row0_1_1:
    lottie_url2 = "https://assets6.lottiefiles.com/packages/lf20_sen1ai7d.json"
    lottie_json = load_lottieurl(lottie_url2)
    st_lottie(lottie_json)

with row0_1_2:
    row0_1_2.write("""“Love doesn’t make the world go round. Love is what makes the ride worthwhile” – Franklin P. Jones  """)

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

# ROW 0 ------------------------------------------------------------------------
row0_spacer1, row0_5_1, row0_spacer2, row0_5_2, row0_spacer3 = st.beta_columns(
    (.1, 1.6, .1, 3.5, .1)
    )

with row0_5_1:
    lottie_url3 = "https://assets4.lottiefiles.com/packages/lf20_utsfwa3k.json"
    lottie_json = load_lottieurl(lottie_url3)
    st_lottie(lottie_json)

with row0_5_2:
    row0_5_2.write("""
    “’Tis better to have loved and lost, than never to have loved at all”  – Alfred, Lord Tennyson 
    """)

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

# ROW 0 ------------------------------------------------------------------------
row0_spacer1, row0_5_1, row0_spacer2, row0_5_2, row0_spacer3 = st.beta_columns(
    (.1, 1.6, .1, 3.5, .1)
    )

with row0_5_1:

    lottie_url4 = "https://assets1.lottiefiles.com/packages/lf20_gghk4m0m.json"
    lottie_json = load_lottieurl(lottie_url4)
    st_lottie(lottie_json)


with row0_5_2:
    row0_5_2.write("""“We come to love not by finding a perfect person, but by learning to see an imperfect person perfectly.” """)
    row0_5_2.write('')
    row0_5_2.write('')

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')


# ROW 1 ------------------------------------------------------------------------

row1_spacer1, row1_1, row1_spacer2, row1_2, row1_spacer3 = st.beta_columns(
    (.1, 2, 1.5, 1, .1)
    )

@st.cache(allow_output_mutation=True)
def get_pd():
    #plyer data
    col_list2 = ['id_','nickname','age', 'status', 'sex', 'orientation', 'body_type', 'diet', 'drinks',
       'drugs', 'education', 'height', 'job', 'offspring', 'pets', 'religion',
       'sign', 'smokes','headshot_url']

    player_data_ = pd.read_csv('https://github.com/bethsung1011/capstone_3/blob/main/profile1.csv?raw=True',
                                low_memory=False, usecols=col_list2)

    return player_data_

player_data_ = get_pd()


# ROW 2 ------------------------------------------------------------------------

row2_spacer1, row2_1, row2_spacer2, row2_2, row2_spacer3,  row2_3, row2_spacer4= st.beta_columns(
    (.1,1.6,.1,1.6,.1,1.6,.1)
    )

with row2_1:
    records=player_data_['nickname'].to_list()
        # 'Miranda', 'Ken', 'Beebeep Bajeep', 'puppy', 'Samu', 'Wayne', 'Tom', 'George Timberman', 'Fox Creek', 'doge', 'Roonie', 'Toby', 'Somebody', 'j']
    selected_data = st.selectbox('Select Who You Are', options=records)


with row2_2:

    url = {'Miranda': 'https://comicvine1.cbsistatic.com/uploads/original/11/114183/5209176-035clefairy.png',
 'Ken': 'https://comicvine1.cbsistatic.com/uploads/original/6/63099/1998241-ep067.png',
 'Beebeep Bajeep': 'https://comicvine1.cbsistatic.com/uploads/original/11/114183/5198759-068machamp.png',
 'puppy': 'https://comicvine1.cbsistatic.com/uploads/original/11/114183/5198898-003venusaur-mega.png',
 'Samu': 'https://comicvine1.cbsistatic.com/uploads/original/11/114183/5213189-042golbat.png',
 'Wayne': 'https://comicvine1.cbsistatic.com/uploads/original/11/114183/5198880-007squirtle.png',
 'Tom': 'https://comicvine1.cbsistatic.com/uploads/original/11/114183/4357615-250px-094gengar.png',
 'George Timberman': 'https://comicvine1.cbsistatic.com/uploads/original/11/114183/5215180-175togepi.png',
 'Fox Creek': 'https://comicvine1.cbsistatic.com/uploads/original/11/114183/5198871-143snorlax.png',
 'doge': 'https://comicvine1.cbsistatic.com/uploads/original/11/114183/5198763-052meowth.png',
 'Roonie': 'https://comicvine1.cbsistatic.com/uploads/original/11/114183/5212960-107hitmonchan.png',
 'Toby': 'https://comicvine1.cbsistatic.com/uploads/original/11/114183/5198641-006charizard-mega_y.png',
 'Somebody': 'https://comicvine1.cbsistatic.com/uploads/original/11/114183/5198809-057primeape.png',
 'j': 'https://comicvine1.cbsistatic.com/uploads/original/11/114183/5212919-095onix.png'}


    st.subheader('About Me')
    st.image(url.get(selected_data), width=200)


with row2_3:


    player_filter = player_data_.loc[player_data_['nickname'] == selected_data]
  
    st.subheader('     ')
    st.text(        f"Name: {player_filter['nickname'].to_string(index=False).lstrip()}"        )
    st.text(        f"Age: {player_filter['age'].to_string(index=False).lstrip()}"        )
    st.text(        f"Status: {player_filter['status'].to_string(index=False).lstrip()}"        )
    st.text(        f"Orientation: {player_filter['orientation'].to_string(index=False).lstrip()}"        )
    st.text(        f"Diet: {player_filter['diet'].to_string(index=False).lstrip()}"        )
    st.text(        f"Job: {player_filter['job'].to_string(index=False).lstrip()}"        )    
    # st.text(        f"Job: {player_filter['job'].astype(int).to_string(index=False).lstrip()}"        )
    st.text(' ')

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')


# Roading  ------------------------------------------------------------------------



# @st.cache(suppress_st_warning=True) 
@st.cache(allow_output_mutation=True)
def get_pd():
    lookup={'Miranda':'https://github.com/bethsung1011/capstone_3/blob/main/id_59946.csv?raw=True', 
    'Ken':'https://github.com/bethsung1011/capstone_3/blob/main/id_59947.csv?raw=True', 
    'Beebeep Bajeep':'https://github.com/bethsung1011/capstone_3/blob/main/id_59948.csv?raw=True', 
    'puppy':'https://github.com/bethsung1011/capstone_3/blob/main/id_59949.csv?raw=True', 
    'Samu':'https://github.com/bethsung1011/capstone_3/blob/main/id_59950.csv?raw=True',
    'Wayne':'https://github.com/bethsung1011/capstone_3/blob/main/id_59951.csv?raw=True', 
    'Tom':'https://github.com/bethsung1011/capstone_3/blob/main/id_59952.csv?raw=True', 
    'George Timberman':'https://github.com/bethsung1011/capstone_3/blob/main/id_59953.csv?raw=True', 
    'Fox Creek':'https://github.com/bethsung1011/capstone_3/blob/main/id_59954.csv?raw=True', 
    'doge':'https://github.com/bethsung1011/capstone_3/blob/main/id_59955.csv?raw=True', 
    'Roonie':'https://github.com/bethsung1011/capstone_3/blob/main/id_59956.csv?raw=True', 
    'Toby':'https://github.com/bethsung1011/capstone_3/blob/main/id_59957.csv?raw=True',   
    'Somebody':'https://github.com/bethsung1011/capstone_3/blob/main/id_59958.csv?raw=True', 
    'j':'https://github.com/bethsung1011/capstone_3/blob/main/id_59959.csv?raw=True'}

    #plyer match info
    col_list2 = ['id', 'age', 'status', 'sex', 'orientation', 'body_type', 'diet',
    'drinks', 'drugs', 'education', 'height', 'job', 'offspring', 'pets',
    'religion', 'sign', 'smokes', 'match percentage']
    
    url=lookup.get(selected_data)   
    player_match_ = pd.read_csv(url,low_memory=False, usecols=col_list2)
    return player_match_

player_match_ = get_pd()


st.header('Find My Match with SVD Attributes')

def click():
    if st.button('Hit me') : 

        st.text('Starting a long computation...')
        # Add a placeholder
        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
            # Update the progress bar with each iteration.
            latest_iteration.text(f'Iteration {i+1}')
            bar.progress(i + 1)
            time.sleep(0.1)

        st.text('...and now we\'re done!')

        st.write("## Top 20 Match Mates")
        player_match_.iloc[:20]


click()

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
 

# Roading  ------------------------------------------------------------------------

@st.cache(allow_output_mutation=True)
def get_pd():
    lookup_c={'Miranda':'https://github.com/bethsung1011/capstone_3/blob/main/c_59946.csv?raw=True', 
    'Ken':'https://github.com/bethsung1011/capstone_3/blob/main/c_59947.csv?raw=True', 
    'Beebeep Bajeep':'https://github.com/bethsung1011/capstone_3/blob/main/c_59948.csv?raw=True', 
    'puppy':'https://github.com/bethsung1011/capstone_3/blob/main/c_59949.csv?raw=True', 
    'Samu':'https://github.com/bethsung1011/capstone_3/blob/main/c_59950.csv?raw=True',
    'Wayne':'https://github.com/bethsung1011/capstone_3/blob/main/c_59951.csv?raw=True', 
    'Tom':'https://github.com/bethsung1011/capstone_3/blob/main/c_59952.csv?raw=True', 
    'George Timberman':'https://github.com/bethsung1011/capstone_3/blob/main/c_59953.csv?raw=True', 
    'Fox Creek':'https://github.com/bethsung1011/capstone_3/blob/main/c_59954.csv?raw=True', 
    'doge':'https://github.com/bethsung1011/capstone_3/blob/main/c_59955.csv?raw=True', 
    'Roonie':'https://github.com/bethsung1011/capstone_3/blob/main/c_59956.csv?raw=True', 
    'Toby':'https://github.com/bethsung1011/capstone_3/blob/main/c_59957.csv?raw=True',   
    'Somebody':'https://github.com/bethsung1011/capstone_3/blob/main/c_59958.csv?raw=True', 
    'j':'https://github.com/bethsung1011/capstone_3/blob/main/c_59959.csv?raw=True'}

    #plyer match info
    col_list2 = ['level_0', 'index', 'age', 'status', 'sex', 'orientation', 'body_type',
       'diet', 'drinks', 'drugs', 'education', 'ethnicity', 'height', 'income',
       'job', 'last_online', 'location', 'offspring', 'pets', 'religion',
       'sign', 'smokes', 'speaks', 'profile_text', 'Total Words', 'id_']
    
    url_c=lookup_c.get(selected_data) 
    # url_c=lookup_c.get(selected_data)   
    player_c_match_ = pd.read_csv(url_c,low_memory=False, usecols=col_list2)
    return player_c_match_.iloc[:,2:]

player_c_match_ = get_pd()



st.header('Find Another Match with CountVectorizer')

def click():
    if st.button('Press me') : 

        st.text('Starting a long computation...')
        # Add a placeholder
        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
            # Update the progress bar with each iteration.
            latest_iteration.text(f'Iteration {i+1}')
            bar.progress(i + 1)
            time.sleep(0.1)

        st.text('...and now we\'re done!')

        st.write("## Top 20 Match Mates")
        player_c_match_


click()

st.write('')
st.write('')
st.write('')

# ROW 4 ------------------------------------------------------------------------

lottie_url = "https://assets9.lottiefiles.com/packages/lf20_xldshlit.json"
lottie_json = load_lottieurl(lottie_url)
st_lottie(lottie_json)


st.write('')
st.write('')
st.write('')


# # Roading  ------------------------------------------------------------------------

@st.cache(allow_output_mutation=True)
def get_pd():

    col_list2 = ['id_', 'age', 'status', 'sex', 'orientation', 'body_type', 'diet',
       'drinks', 'drugs', 'education', 'ethnicity', 'height', 'income', 'job',
       'last_online', 'location', 'offspring', 'pets', 'religion', 'sign',
       'smokes', 'speaks', 'profile_text', 'Total Words', 'lda_recommend']
     
    df = pd.read_csv('https://github.com/bethsung1011/capstone_3/blob/main/concat_with_lda.csv?raw=True', usecols=col_list2, error_bad_lines=False)
    return df


df = get_pd()


st.sidebar.title('User Database')



sex = df['sex'].unique()
sex_choice = st.sidebar.selectbox('Select sex:',sex)
msk1 = df["sex"] == sex_choice if sex_choice in sex else True
filtered_sex = df[df['sex'] == sex_choice].iloc[:20,0:9]



orientation = df['orientation'].unique()
orientation_choice= st.sidebar.selectbox('Select orientation:', orientation)
msk2 = df["orientation"] == orientation_choice if orientation_choice in orientation else True
filtered_orientation = df[df['orientation'] == orientation_choice].iloc[:20,0:9]



age = np.arange(18,100,1)
age_choice = st.sidebar.slider('choose age', 18, 100, 30)
msk3 = df["age"] == age_choice if age_choice in age else True
filtered_age = df[df['age'] == age_choice].iloc[:20,0:9]



st.title('Database')
st.dataframe(filtered_age)





# ROW 5 ------------------------------------------------------------------------
row5_spacer1, row5_1, row5_spacer2 = st.beta_columns((.1, 3.2, .1))

with row5_1:
    st.markdown('___')
    about = st.beta_expander('About/Additional Info')
    with about:
        '''
        Thanks for checking out my app! It was built entirely using [okcupid]
        (https://www.kaggle.com/andrewmvd/okcupid-profiles/) data. Special thanks to [Larxel]
        (https://www.kaggle.com/andrewmvd) and [Anna Durbanova](https://www.kaggle.com/annadurbanova) who do a great job providing this kaggle
        data, helping okcupid EDA on initial stage! This is the first time I have ever built something like this, 
        so any comments or feedback is greatly appreciated. I hope you enjoy!

        This app is a dashboard that runs an recommender on specific users provided in Galvanize 2021 Spring Full Time Online Cohort.
        It has logged 14 total anonymous and randomly suffled people.
        
        **Select Who You Are** 
            - Display information of participants along with picture.
        
        **SVD Attributes** 
            - Using non-verval attributes, SVD model was made and recommender provides cosine similarity of best match. 
        
        **CountVectorizer** 
            - Using Natural Language Process, CountVectorizer model provides similarity recommending.
        
                
        ### Beth Sung, April 2021
        '''
st.write('')
st.write('')
st.write('')
st.write('')
st.write('Thanks!')
st.write('made by [Beth Sung](https://www.linkedin.com/in/beth-sung/)')

