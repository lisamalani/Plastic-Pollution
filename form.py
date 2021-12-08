import streamlit as st
import pygsheets
import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

banner = "images/banner.png"
def _google_creds_as_file():
    t_file = 'credentials_temp.json'
    temp = open(t_file, "w")
    temp.write(json.dumps({
        "type": st.secrets["gcp_service_account"]["type"],
        "project_id": st.secrets["gcp_service_account"]["project_id"],
        "private_key_id": st.secrets["gcp_service_account"]["private_key_id"],
        "private_key": st.secrets["gcp_service_account"]["private_key"],
        "client_email": st.secrets["gcp_service_account"]["client_email"],
        "client_id": st.secrets["gcp_service_account"]["client_id"],
        "auth_uri": st.secrets["gcp_service_account"]["auth_uri"],
        "token_uri": st.secrets["gcp_service_account"]["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["gcp_service_account"]["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["gcp_service_account"]["client_x509_cert_url"]
    }))
    temp.flush()
    temp.close()
    return t_file

def read_gsheet():
    creds_file = _google_creds_as_file()
    gc = pygsheets.authorize(service_file=creds_file) #'client_secret_359875570109-s185gd60vf2esfiq27v9jd8keb7sts89.apps.googleusercontent.com.json')
    sh = gc.open_by_key(st.secrets["private_gsheets_key"])
    wk1 = sh[0]
    data_df = pd.DataFrame(wk1.get_all_records())
    return wk1, data_df

def write_gsheet(response):
    wk1, data_df = read_gsheet()
    rows = len(data_df)
    wk1.update_row(rows + 2, response)


def data_viz():
    st.image(banner)
    st.markdown("<br><br><br>",unsafe_allow_html=True)  
    st.markdown("<h5>Results:</h5>",unsafe_allow_html=True)  
    _, data_df = read_gsheet()

    # AGE
    age_groups = ['10-18', '19-27', '28-36', '37-45', '46-54', '54+']

    age_10_df = data_df[data_df["Age Group"] == "10-18"]
    age_19_df = data_df[data_df["Age Group"] == "19-27"]
    age_28_df = data_df[data_df["Age Group"] == "28-36"]
    age_37_df = data_df[data_df["Age Group"] == "37-45"]
    age_46_df = data_df[data_df["Age Group"] == "46-54"]
    age_54_df = data_df[data_df["Age Group"] == "54+"]
    age_len = [len(age_10_df),
            len(age_19_df),
            len(age_28_df),
            len(age_37_df),
            len(age_46_df),
            len(age_54_df)]
    # Age
    data_age = pd.DataFrame(age_len, age_groups)


    # REGION    
    regions = ['Asia', 'Africa', 'Australia', 'Europe', 'North America', 'South America']
    
    asia_df = data_df[data_df["Region"] == "Asia"]
    africa_df = data_df[data_df["Region"] == "Africa"]
    au_df = data_df[data_df["Region"] == "Australia"]
    europe_df = data_df[data_df["Region"] == "Europe"]
    na_df = data_df[data_df["Region"] == "North America"]
    sa_df = data_df[data_df["Region"] == "South America"]
    regions_len = [len(asia_df),
            len(africa_df),
            len(au_df),
            len(europe_df),
            len(na_df),
            len(sa_df)]
    # Region
    data_region = pd.DataFrame(regions_len, regions)


    # Recycle
    names = ['Everyday', 'About once a week', 'Few times a week', 
                        'About once a month', 'A few times a month', 'Never']
    n0_df = data_df[data_df["Recycle03"] == names[0]]
    n1_df = data_df[data_df["Recycle03"] == names[1]]
    n2_df = data_df[data_df["Recycle03"] == names[2]]
    n3_df = data_df[data_df["Recycle03"] == names[3]]
    n4_df = data_df[data_df["Recycle03"] == names[4]]
    n5_df = data_df[data_df["Recycle03"] == names[5]]
    val = [len(n0_df),
            len(n1_df),
            len(n2_df),
            len(n3_df),
            len(n4_df),
            len(n5_df)]

    # Recycle_data
    data_recycle = pd.DataFrame(val, names)

    # Plot data
    st.markdown('''<h5><b>Age Groups:</b></h5>''',unsafe_allow_html=True)
    st.bar_chart(data_age)

    st.markdown('''<h5><b>Region:</b></h5>''',unsafe_allow_html=True)
    st.bar_chart(data_region)

    st.markdown('''<h5><b>Purchase of plastic drinks bottles</b></h5>''',unsafe_allow_html=True)
    st.bar_chart(data_recycle)


def submit_data(age_group, region, recycle01, recycle02, recycle03, recycle04):
    write_gsheet([age_group, region, recycle01, recycle02, recycle03, recycle04])


def app():
    # Survey
    st.markdown('''The first synthetic plastic — Bakelite  — was produced in 1907, 
    marking the beginning of the global plastics industry. However, rapid growth 
    in global plastic production was not realized until the 1950s. Over the next 
    65 years, annual production of plastics increased nearly 200-fold to 381 
    million tonnes in 2015. For context, this is roughly equivalent to the mass 
    of two-thirds of the world population.<br>
    Let's understand how does a single consumer (that's you) uses plastics:''', 
                        unsafe_allow_html=True)


    st.markdown('''<br>''', unsafe_allow_html=True)
    age_group = st.radio("How old are you?",
                         ('10-18', '19-27', '28-36',
                          '37-45', '46-54', '54+'))
    st.markdown('''<br>''', unsafe_allow_html=True)
    region = st.selectbox('Which region do you belong to?',
                          ('Africa', 'Asia', 'Europe',
                           'North America', 'South America',
                           'Australia'))
    st.markdown('''<br>''', unsafe_allow_html=True)
    recycle01 = st.radio("Do you make an active effort to recycle used plastic?",
                        ('Yes', 'No'))
    st.markdown('''<br>''', unsafe_allow_html=True)
    recycle02 = st.radio("Do you re-use any form of plastic packaging?",
                        ('Yes', 'No', 'Occasionally'))
    st.markdown('''<br>''', unsafe_allow_html=True)
    recycle03 = st.radio("How often do you purchase plastic drinks bottles? I.e. Coca-cola, water, etc.",
                        ('Everyday', 'About once a week', 'Few times a week', 
                        'About once a month', 'A few times a month', 'Never'))
    st.markdown('''<br>''', unsafe_allow_html=True)
    recycle04 = st.radio("Before answering this survey, were you aware that up to 8 million tonnes of plastic 'leak' into our oceans every year?",
                        ('Yes', 'No'))
    st.markdown('''<br>''', unsafe_allow_html=True)
    if st.button('Submit'):
        submit_data(age_group, region, recycle01, recycle02, recycle03, recycle04)

    if st.button('View the result anyway!'):
        data_viz()

if __name__ == "__main__":
    app()
