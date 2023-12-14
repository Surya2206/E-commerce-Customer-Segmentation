import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title= "E-COMMERCE",
                   layout= "wide"
                   )
st.header("E-COMMERCE CUSTOMER SEGMENTATION", divider='rainbow')

backgroundColor = "#743FD0"
secondaryBackgroundColor = "#2F2F62"

df1=pd.read_csv(r"C:\Users\surya\Desktop\guvi\E_ Commerce\clustered_data.csv")

col1,col2,col3,col4,col5=st.columns(5)
with col1:
 Gender=st.text_input('Gender (Male : 1, Female : 0) ','0')
 Orders=st.text_input('Orders','0')
 Jordan=st.text_input('Jordan','0')
 Gatorade=st.text_input('Gatorade','0')
 Samsung=st.text_input('Samsung','0')
 Asus=st.text_input('Asus','0')
 Udis=st.text_input('Udis','0')

with col2:
 Mondelez_International=st.text_input('Mondelez International','0')
 Wrangler=st.text_input('Wrangler','0')
 Vans=st.text_input('Vans','0')
 Fila=st.text_input('Fila ','0')
 Brooks=st.text_input('Brooks','0')
 Hm=st.text_input('H&M','0')
 Dairy_Queen=st.text_input('Dairy Queen','0')

with col3:
 Fendi=st.text_input('Fendi','0')
 Hewlett_Packard=st.text_input('Hewlett Packard','0')
 Pladis=st.text_input('Pladis','0')
 Asics=st.text_input('Asics','0')
 Siemens=st.text_input('Siemens','0')
 Jm=st.text_input('J.M. Smucker ','0')
 Pop_Chips=st.text_input('Pop Chips','0')


with col4:
 Juniper=st.text_input('Juniper','0')
 Huawei=st.text_input('Huawei','0')
 Compaq=st.text_input('Compaq','0')
 Ibm=st.text_input('IBM','0')
 Burberry=st.text_input('Burberry','0')
 Mi=st.text_input('Mi','0')
 Lg=st.text_input('LG','0')
 Dior=st.text_input('Dior','0')
 
with col5: 
 Scabal=st.text_input('Scabal ','0')
 Tommy_Hilfiger=st.text_input('Tommy Hilfiger','0')
 Hollister=st.text_input('Hollister','0')
 Forever_21=st.text_input('Forever 21','0')
 Colavita=st.text_input('Colavita','0')
 Microsoft=st.text_input('Microsoft','0')
 Jiffy_mix=st.text_input('Jiffy mix','0')
 Kraft=st.text_input('Kraft','0')
aa=st.button("Enter") 
if aa:
    import pickle
    with open(r'C:\Users\surya\Desktop\guvi\E_ Commerce\cmodel.pkl', 'rb') as file:
        plc=pickle.load( file) 

    sample=[[int(Gender),int(Orders),int(Jordan),int(Gatorade),int(Samsung),int(Asus),int(Udis),int(Mondelez_International),int(Wrangler),int(Vans),int(Fila),int(Brooks),int(Hm),int(Dairy_Queen),int(Fendi),int(Hewlett_Packard),int(Pladis),int(Asics),int(Siemens),int(Jm),int(Pop_Chips),int(Juniper),int(Huawei),int(Compaq),int(Ibm),int(Burberry),int(Mi),int(Lg),int(Dior),int(Scabal),int(Tommy_Hilfiger),int(Hollister),int(Forever_21),int(Colavita),int(Microsoft),int(Jiffy_mix),int(Kraft)]]
    array=np.array(sample)
    result=plc.predict(array)
    
    if result==0:
       st.subheader(
    f"This Customer Belongs To Cluster 0")
    else: 
      st.subheader(
    f"This Customer Belongs To Cluster 1")
