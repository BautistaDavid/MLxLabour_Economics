
from numpy import dtype

def estado_civil_dummy():
    dic_estado={"Separado(a) o divorciado(a)":0,
    "Soltero(a)":0,"Casado":1,"En unión libre":1,
    "Viudo(a)":0,1.0:1,2.0:1,3.0:0,4.0:0,5.0:0}
    return dic_estado

    
def dic_etnia():
    import numpy as np 
    dic_etnia={"Mestizo":1,'Ninguno de los  anteriores':0,"Blanco":1,"Indígena":0,"Negro, mulato (afro descendiente)":1,
                "Palenquero":1,np.NaN:0,1.0:1,2.0:1,3.0:1,4.0:1,5.0:1,6.0:1,7.0:1,8.0:0}
    return dic_etnia

def cols_names():
    names_cols={"actividad_ppal":"employment","sexo":"sex","edad":"age","estado_civil":"couple",
                "hijos":"sons","etnia":"ethnicity","Discapacidad":"Disability","educ_años":"educ_years",
                "embarazo_hoy":"w_pregnant","lee_escribe":"read_write","estudia":"student",
                "n_internet":"internet","Urbano":"Urban"}
    return names_cols



def creador_id(data):
    try:
        data.insert(0,"id",data["DIRECTORIO"]+data["SECUENCIA_P"]+data["ORDEN"]+data["HOGAR"])
        data.insert(1,"id_hogar",data["DIRECTORIO"]+data["SECUENCIA_P"])
    except:
        data.insert(0,"id_hogar",data["DIRECTORIO"]+data["SECUENCIA_P"])


def dic_dtypes():
    dtype={"DIRECTORIO":"str",
        "SECUENCIA_P":"str",
        "ORDEN":"str",
        "HOGAR":"str"}
    return dtype

def variables_modelo():
    variables=["id","id_hogar","ocupado","desocupado","P6020","P6040","ESC","P6080","P6070","P6170","P4030S1A1","P5210S16","P6081","P6083","DPTO_x"]
    return variables


def procces_data_month(mes,variables):
    import pandas as pd 
    dtype=dic_dtypes()
    Ac=pd.read_csv(f"sets_model/{mes}/Acaracteristicas.csv",sep=";",dtype=dtype)
    Ao=pd.read_csv(f"sets_model/{mes}/Aocupados.csv",sep=";",dtype=dtype)
    Ad=pd.read_csv(f"sets_model/{mes}/Adesocupados.csv",sep=";",dtype=dtype)
    Av=pd.read_csv(f"sets_model/{mes}/Avivienda.csv",sep=";",dtype=dtype)

    Cc=pd.read_csv(f"sets_model/{mes}/Ccaracteristicas.csv",sep=";",dtype=dtype)
    Co=pd.read_csv(f"sets_model/{mes}/Cocupados.csv",sep=";",dtype=dtype)
    Cd=pd.read_csv(f"sets_model/{mes}/Cdesocupados.csv",sep=";",dtype=dtype)
    Cv=pd.read_csv(f"sets_model/{mes}/Cvivienda.csv",sep=";",dtype=dtype)

    Rc=pd.read_csv(f"sets_model/{mes}/Rcaracteristicas.csv",sep=";",dtype=dtype)
    Ro=pd.read_csv(f"sets_model/{mes}/Rocupados.csv",sep=";",dtype=dtype)
    Rd=pd.read_csv(f"sets_model/{mes}/Rdesocupados.csv",sep=";",dtype=dtype)
    Rv=pd.read_csv(f"sets_model/{mes}/Rvivienda.csv",sep=";",dtype=dtype)

    for k in [Ao,Co,Ro]:
        k.insert(0,"ocupado",1)
    for g in [Ad,Cd,Rd]:
        g.insert(0,"desocupado",1)

    A=[Ac,Ao,Ad,Av]
    C=[Cc,Co,Cd,Cv]
    R=[Rc,Ro,Rd,Rv]

    for j in A:
        creador_id(j)
    for j in C:
        creador_id(j)
    for j in R:
        creador_id(j)

    datos_a=pd.merge(Ac,Ao,on="id",how="outer",suffixes=("","_x"))
    datos_a=pd.merge(datos_a,Ad,on="id",how="outer",suffixes=("","_x"))
    datos_a=pd.merge(datos_a,Av,on="id_hogar",how="outer")

    datos_c=pd.merge(Cc,Co,on="id",how="outer",suffixes=("","_x"))
    datos_c=pd.merge(datos_c,Cd,on="id",how="outer",suffixes=("","_x"))
    datos_c=pd.merge(datos_c,Cv,on="id_hogar",how="outer")

    datos_r=pd.merge(Rc,Ro,on="id",how="outer",suffixes=("","_x"))
    datos_r=pd.merge(datos_r,Rd,on="id",how="outer",suffixes=("","_x"))
    datos_r=pd.merge(datos_r,Rv,on="id_hogar",how="outer")

    datos_a=datos_a[variables]
    datos_c=datos_c[variables]
    datos_r=datos_r[variables]
    
    return pd.concat([datos_a,datos_c,datos_r])

def yes_no_variable(item):
    if item=="Yes" or item=="Male":
        item=1
    else:
        item=0
    return item
