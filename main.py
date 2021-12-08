import streamlit as st
from multipage import MultiPage
import world, country, form, rivers, correlation

# Page style
st.set_page_config(page_title="Plastic Pollution", layout="wide")

st.sidebar.markdown("""<font color = "gray"><b>05839: Interactive Data Science</b></font>""", unsafe_allow_html=True)

st.sidebar.markdown("""<font color = "gray"><br>(mmalani)<br>Monalisa Malani<br>M.Sc. Sustainable Design<br>
Carnegie Mellon University<br><br></font>""", unsafe_allow_html=True)

# Contents
st.sidebar.title("Contents")
app = MultiPage()
app.add_page('Global Statistics\t\n', world.app)
app.add_page('Country\t\n', country.app)
app.add_page('Rivers and Oceans\t\n', rivers.app)
app.add_page('Correlation\t\n', correlation.app)
app.add_page('Survey\t\n', form.app)
app.run()