import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 
import pickle as pkl 
from utils import yes_no_variable
from pages.graphs import pie_probe

ciudades=pd.read_csv("data/dpts.csv",sep=";") 
ciudades=list(ciudades["Nombre"])

def write():
    info="""
    ### **Test the Models**

    In this section you can calculate the probability of being employed based on 
    the estimate of the selected model. You just have to answer the following questions 
    that relate to the different variables used during the modeling processes.
    
    """
    st.markdown(info)

    
    col1,col2=st.columns(2)
    with col1:
        gender=st.selectbox("Gender:",("Male","Female"))
        age=st.number_input("Age:",min_value=(13))
        schooling=st.number_input("Years of Schooling:",min_value=(0))
        couple=st.selectbox("Couple:",("Yes","No"))
        student=st.selectbox("Are you currently a student?",("Yes","No"))

    with col2:
        stratum=st.number_input("Social Stratum:",min_value=0,max_value=6)
        pc=st.selectbox("Do you have a personal PC?",("Yes","No"))
        fathers=st.selectbox("With whom of your fathers do you live?",("Mother","Dad","Both of them","None"))
        ethnicity=st.selectbox("With what ethnic group do you feel recognized?",("Afro-descendant","Gypsy","Indigenous","Palenquero","Raizal","No ethnic recognition"))    
        country=st.selectbox("Select your town:",ciudades)

    
    gender=yes_no_variable(gender)
    couple=yes_no_variable(couple)
    student=yes_no_variable(student)
    pc=yes_no_variable(pc)

    list_ethnic=["Afro-descendant","Gypsy","Indigenous","Palenquero","No ethnic recognition"]

    list_ctr=['Atlántico', 'Bogotá D.C.','Bolívar', 'Boyacá', 'Caldas', 'Caquetá', 'Cauca', 'Cesar', 'Chocó',\
        'Cundinamarca', 'Córdoba', 'Huila', 'La Guajira', 'Magdalena', 'Meta','Nariño', 'Norte de Santander', 'Quindío',\
        'Risaralda', 'Santander', 'Sucre','Tolima','valle del Cauca']

    if fathers=="Both of them":
        array_fathers=[1,1]
    elif fathers=="Mother":
        array_fathers=[0,1]
    elif fathers=="Dad":
        array_fathers=[1,0]
    else:
        array_fathers=[0,0]
        
    ethnic=[]
    for i in list_ethnic:
        if i ==ethnicity:
            ethnic.append(1)
        else:
            ethnic.append(0)
    
    array_country=[]
    for i in list_ctr:
        if i==country:
            array_country.append(1)
        else:
            array_country.append(0)

    lr_pickle=open("lr_clf.pickle","rb")
    lr=pkl.load(lr_pickle)
    lr_pickle.close()

    variables=[gender,age,schooling,couple,student,stratum,pc]
    variables.extend(array_fathers)
    variables.extend(ethnic)
    variables.extend(array_country)

    
    pred_proba=lr.predict_proba([variables])
    # st.text(list(pred_proba[0]))     

    fig=pie_probe([list(pred_proba[0]*100)[1],list(pred_proba[0]*100)[1]])




    # fig, ax = plt.subplots(figsize=(4, 4))
    # data = [list(pred_proba[0]*100)[1],list(pred_proba[0]*100)[1]]
    # wedgeprops = {'width':0.3, 'edgecolor':'black', 'lw':3}
    # patches, _ = ax.pie(data, wedgeprops=wedgeprops, startangle=90, colors=['#5DADE2', 'white'])
    # patches[1].set_zorder(0) 
    # patches[1].set_edgecolor('black')
    # plt.title('Worldwide Access to Electricity', fontsize=16, loc='left')
    # plt.text(0, 0, "{0:.2f}%".format(data[0]), ha='center', va='center', fontsize=30)
    # plt.text(-1.2, -1.3, "", ha='left', va='top', fontsize=12)
    # plt.show()



    st.pyplot(fig)


    
    st.write(pred_proba)
    


    # # ESPACIO PARA CREAR LA GRAFIca
    # X=np.linspace(0,100)
    # fig, ax = plt.subplots()
    # ax.plot(X,X**2)
    # #####
    # st.pyplot(fig)


    
    
    



    


    


