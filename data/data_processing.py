import pandas as pd 
import numpy as np 
datos=pd.read_csv("data/raw_data.csv",index_col="Unnamed: 0")

datos["ocupado"].replace({1.0:1,np.NaN:0},inplace=True)
datos["ocupado"]=[int(i) for i in datos["ocupado"]]

datos["ESC"].replace({np.NaN:0.0," ":0.0},inplace=True)
datos["ESC"]=[int(i) for i in datos["ESC"]]

datos["P4030S1A1"].replace({"9":3,"0":1," ":2},inplace=True)
datos["P4030S1A1"]=datos["P4030S1A1"].astype("int64")

#modificar variables
datos["P6070"].replace({1:1,2:1,3:1,4:0,5:0,6:0},inplace=True)

#etnia
datos["P6080"].replace({6:"sin_rec_etnico",5:"afro",4:"palenquero",3:"Raizal",2:"gitano",1:"indigena"},inplace=True)
datos=pd.concat([datos,pd.get_dummies(datos["P6080"])],axis=1)

#sexo
datos["P6020"].replace({2:0},inplace=True)

#estudiante activo 
datos["P6170"].replace({2:0},inplace=True)

#pc

datos["P5210S16"].replace({2:0},inplace=True)

# reside con padre 
datos["P6081"].replace({2:0,3:0},inplace=True)

# reside con madre 
datos["P6083"].replace({2:0,3:0},inplace=True)
#departamento 

dpto=pd.read_csv("data/dpts.csv",sep=";",index_col="Nombre")
dpto=dpto.to_dict()["Código"]
dpto={cod:dp for cod,dp in zip(dpto.values(),dpto.keys())}

datos["DPTO_x"].replace(dpto,inplace=True)
datos=pd.concat([datos,pd.get_dummies(datos["DPTO_x"])],axis=1)

datos=datos.drop(columns=["id","id_hogar","desocupado","P6080","DPTO_x"])

#cols_names
#cols=["employed","sex","age","years_scho","civil_s","Student","social_level"] version ingles
cols=["empleado","sexo","edad","años_edc","pareja","estudiante_act","estrato","pc","reside_padre","reside_madre",\
    "raizal","afro","gitano","indigena","palenquero","sin_rec_etnico","antioquia","atlantico",\
    "bogota","bolivar","boyaca","caldas","Caqueta","cauca","cesar","choco","cundinamarca","cordoba",\
    "huila","guajira","magdalena","meta","nariño","norte_s","quindio","risaralda","santander","sucre",\
    "tolima","valle_c"]
 

datos=datos.rename(columns={old:new for old,new in zip(list(datos.columns),cols)})

datos.drop(columns=["raizal","antioquia"],inplace=True) #trampa dummy 

datos.to_csv("data/data_models.csv",index=False)

