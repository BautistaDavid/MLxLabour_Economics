import streamlit as st
from pages import Test_the_Models, Variable_Anylisis, About_Sample


st.title("**Calculating the Probability of Being Employed**")

st.sidebar.markdown("""# **About This Proyect**""")

with st.sidebar.expander("What is it about?",expanded=True):
     st.write("""
         This web app was created to present clasfication machine learning models
         relate to the fact of calculate the probability of being emmployed in the 
         colombian context
         """)

with st.sidebar.expander("Abouts Me",expanded=True):
     st.write("""
        ¡Hi1! my name is David Bautista, im a coll
         """)



st.markdown("""<hr style="height:4px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.markdown(
    '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">',
    unsafe_allow_html=True,
)
query_params = st.experimental_get_query_params()
tabs = ["Test the Models", "Variable Anylisis", "About the Sample"]
if "tab" in query_params:
    active_tab = query_params["tab"][0]
else:
    active_tab = "Home"

if active_tab not in tabs:
    st.experimental_set_query_params(tab="Test the Models")
    active_tab = "Test the Models"

li_items = "".join(
    f"""
    <li class="nav-item">
        <a class="nav-link{' active' if t==active_tab else ''}" href="/?tab={t}">{t}</a>
    </li>
    """
    for t in tabs
)
tabs_html = f"""
    <ul class="nav nav-tabs">
    {li_items}
    </ul>
"""

st.markdown(tabs_html, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

if active_tab == "Test the Models":
    Test_the_Models.write()
elif active_tab == "Variable Anylisis":
    Variable_Anylisis.write()
elif active_tab == "About the Sample":
    About_Sample.write()
else:
    st.error("Something has gone terribly wrong.")