import pandas as pd1
import pd_sim as pd2

nombre_archivo = 'FSM_dosUnosSeguidos.csv'

data_frame1 = pd1.read_csv(nombre_archivo)
data_frame2 = pd2.read_csv(nombre_archivo)

print(data_frame1)
print(data_frame2)

print()

print(data_frame1.head())
# error print(data_frame2.head())

print()

print(data_frame1.tail())
#error print(data_frame2.tail())

print()

print(data_frame1.index)
#error print(data_frame2.index)

print()

print(data_frame1.describe())
#error print(data_frame2.describe())

print()

#print(data_frame1.T)
print(data_frame2.T)
#error print(data_frame2.T())

print()

#print(data_frame1.sort_index(axis=1, ascending=False))
#error print(data_frame2.sort_index(axis=1, ascending=False))

print()

print(data_frame1['Est_act'])
print(data_frame2['Est_act'])

print()

print(data_frame1[0:3])
# print(data_frame2[0:3])

print("Manuel Gamboa Funcion Loc")
print(data_frame1[0:3])
print(data_frame2[0:3])

# print()

print(data_frame1.loc[0])
# #error print(data_frame2.loc[0])
# #error print(data_frame2.loc(0))

print(data_frame1)
print('data_frame1')
print(data_frame1.at[1,2])
print(data_frame2.at[1,2])
print("Juan Esteban Parada, loc")

print()

print(data_frame1.at[1, "Est_act"])
#error print(data_frame2.at[1, "Est_act")])
#error print(data_frame2.at(1, "Est_act"))

# print()

print(data_frame1 > 0)
# #error print(data_frame2 > 0)

# print()

print(data_frame1.iloc[3])
# #error print(data_frame2.iloc[3])
# #error print(data_frame2.iloc(3))

# print()

# #data_frame1_a=data_frame1.copy()
# print(data_frame1_a)
# #error data_frame2_a=data_frame2.copy()
# #error print(data_frame2_a)

# print()

# #data_frame1_a['Est_act'] = 0
# print(data_frame1_a)
# #data_frame2['Est_act'] = 0
print(data_frame2)

# print('Función negar -, Gerardo Muñoz')

print(-data_frame1)
# print(-data_frame2)

# print()


#Oscar David Poblador Parra - 20211005116
#Función de selección de datos Iloc
print("\nIloc selección entero y slice - Oscar Poblador 20211005116")
print("\nPRUEBA CON PÁRAMETRO ENTERO")
data_frame2.iloc[2]
print("\n")
print("\nValores seleccionados")
print(data_frame2.iloc.seleccion_titulo)
print(data_frame2.iloc.seleccion_valor)
print("\nPRUEBA CON PÁRAMETRO SLICE")
data_frame2.iloc[1:3,0:2]
print("\nValores seleccionados")
print("\n")
print(data_frame2.iloc.seleccion_titulo)
print(data_frame2.iloc.seleccion_valor)


#Test función 3 iloc
# Juan David Bello Rodríguez - 20211005028
data_frame1.iloc[[1,2],[1,2]] #Selecciona filas y columnas y las imprime
data_frame1.iloc[[1,2]] #Selecciona filas y las imprime

data_frame2.iloc[[1,2],[1,2]]
data_frame2.iloc[[1,2]]





#Test Oscar-Poblador116
#data_frame1.iloc(2)
#d[3:5,0:2]
# print(seleccion_titulo)
# print(seleccion_valor)
#    A         B         C         D
#  0.469112, -0.282863, -1.509059, -1.135632
# 1.212112, -0.173215,  0.119209, -1.044236
# -0.861849, -2.104569, -0.494929,  1.071804
#  0.721555, -0.706771, -1.039575,  0.271860
# -0.424972,  0.567020,  0.276232, -1.087401
# -0.673690,  0.113648, -1.478427,  0.524988

# test funcion iat - Willian Chaparro
# df = data_frame2.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],columns=['A', 'B', 'C'])
# print(df.iat[0,1])
# print('Valor antiguo: ',df.iat[0,2])
# df.iat[0,2]=10
# print('Valor nuevo: ',df.iat[0,2])

#Test JhonatanMJ1127
# print(Jhonatan.index)
# print()


#michael063
#Describe alguno datos de la tabla
describe_pd1 = data_frame1.describe()
describe_pd2 = data_frame2.describe()

print(describe_pd1)
       
       
#Test Funcion Manuel Guio 
#Manuel Alejandro Guio Cardon - 20211005061
#Funcion seleccion por columnas y filas

data_frame1.iloc[1,3]
data_frame2.iloc[1,3]
