    from os import path
    from numpy import dtype, float32
    from utils import *
    import pandas as pd 

    datos=pd.DataFrame()
    contador=0
    for i in ["Enero.csv","Febrero.csv","Marzo.csv","Abril.csv","Mayo.csv","Junio.csv","Julio.csv","Agosto.csv"]:
        datos=pd.concat([datos,procces_data_month(i,variables=variables_modelo())])
        contador+=1
        print(f"Cargando {contador}/8...")
    datos=datos.iloc[:,~datos.columns.duplicated()]
    datos=datos[(datos["ocupado"]==1.0) | (datos["desocupado"]==1.0)]


    datos.to_csv("data/raw_data.csv")


variables_modelo()
# datos.to_csv("datos.csv")
