import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix

n_grupos = 4
df = pd.read_csv('4clasesBalanceado.csv')

X_adr = np.array(df[["Rh F (mm)","Rv F (mm)","Astig F (D)","Asph. Q F","Rh B (mm)","Rv B (mm)","K2 B (D)","Astig B (D)","Asph. Q B","Pachy Apex","Pachy Min","ISV","IVA","IHA","IHD","K1 (D)","K2 (D)","Astig","RPI Max","K max","I-S","AC Depth","Ecc Sup","Ecc Inf","Cor.Vol.","KPD","Ecc (Front)","Ecc (Back)","Sag. Height Mean [µm]","ACD Apex"]])
y_adr = np.array(df['cluster_label'])

X_train, X_test, y_train, y_test = train_test_split(X_adr, y_adr, test_size=0.1,random_state=1)

maximo= 0
#print("Total antes de balancear ")
for i in range(n_grupos):
  #print('clase ',i, ' : ', y_adr.tolist().count(i))
  if(y_adr.tolist().count(i)>maximo):
    maximo=y_adr.tolist().count(i)

#print("Cantidad maxima en un grupo: ",maximo)

total_general = len(y_adr)

for i in range(n_grupos):  
  x_lista_temp = []
  y_lista_temp = []
  total_grupo = y_adr.tolist().count(i)
  cociente, resto, restantes = 0,0,0

  cociente = maximo //total_grupo
  resto = maximo % total_grupo
  restantes = total_grupo*(cociente-1)+resto
  if(restantes>0):
    for j in range(cociente-1):
      for k in range(total_general):
        if(y_adr[k]==i):
          #print(y_train[k],i)
          y_adr = np.concatenate((y_adr,y_adr[k:k+1]))
          X_adr = np.concatenate((X_adr,X_adr[k:k+1]))
 
    if(resto>0):
      restantes = resto
      indice = total_grupo // restantes
      n=0
      for l  in range(total_general):
        if(y_adr[l]==i):
          n+=1
          y_adr = np.concatenate((y_adr,y_adr[l:l+1]))
          X_adr = np.concatenate((X_adr,X_adr[l:l+1]))

        l+=indice
        if(n==restantes):
          break

#for i in range(4):
#  print('clase ',i, ' : ', y_train.tolist().count(i))
#
#print('Total validación')
#for i in range(4):
#  print('clase ',i, ' : ', y_test.tolist().count(i))

#produndidad del arbol
adr = RandomForestClassifier(n_estimators=400)
#entrenamiento
adr.fit(X_train, y_train) 
#Y_pred = adr.predict(X_test)
#print("Accuracy:",metrics.accuracy_score(y_test, Y_pred))

pickle.dump(adr,open('model.pkl','wb'))


