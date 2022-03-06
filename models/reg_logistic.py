import pandas as pd 
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, mean_absolute_error
from sklearn.preprocessing import StandardScaler
import pickle as pkl

datos=pd.read_csv("data/data_models2.csv")
datos.columns
X=datos.drop(columns=["empleado"])
y=datos["empleado"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=777)

param_grid={"C":[10, 1.0, 0.1, 0.01],
            "max_iter":[750,1000,1500],
            "class_weight":[{0:0.7,1:0.3},{0:0.8,1:0.2},{0:0.75,1:0.25},]}

#grid_search=GridSearchCV(LogisticRegression(),param_grid,cv=6) # no ejecuto para optimizar 
#grid_search.fit(X_train,y_train)
# class_weight={0:y_train.value_counts()[1]/len(y_train),1:y_train.value_counts()[0]/len(y_train)}

# lr_clf=LogisticRegression(**grid_search.best_params_,solver="saga",)  # no ejecuto por optimizar


# estandarisacion 


scaler = StandardScaler().fit(X_train)
standardized_X = scaler.transform(X_train)
standardized_X_test = scaler.transform(X_test)

def scaler_variable_to_predict(variables):
    return scaler.transform(variables)

lr_clf=LogisticRegression(class_weight={0:0.75,1:0.25},solver="saga",max_iter=750,C=0.1,n_jobs=5,penalty='elasticnet',l1_ratio=0)
lr_clf.fit(standardized_X,y_train)
y_pred= lr_clf.predict(standardized_X_test)
print(mean_absolute_error(y_test,y_pred)*100)


lr_pickle=open("lr_clf.pickle","wb")

pkl.dump(lr_clf,lr_pickle)

lr_pickle.close()



print("Hola")
# y_pred_proba=rf_clf.predict_proba(X_test)




# X_test.tail()
# print("listo")
# X_test.iloc[37565]
# y_test.tail(1)
# (confusion_matrix(y_test,y_pred)/total)*100

# len(y_test)
# confusion_matrix(y_test,y_pred)

# total=10700+6132+33336+54254
# 10700/total

# list(y_pred)

# print("hola")