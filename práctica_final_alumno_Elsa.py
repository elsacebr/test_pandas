#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import numpy as np


# Cargar datos

# In[10]:


# Importamos el dataset de los datos de los pokemon
df = pd.read_csv('dataset_final.csv')
df.head()


# In[11]:


'''
1. ¿Cuántos pokémon hay en el dataset?
'''
len(df)


# In[12]:


'''
2. ¿Cuántos pokémon hay de tipo Poison? (Type 1)
'''
print(len(df[df['Type 1'] == 'Poison']))


# In[13]:


'''
3. ¿Cuántos tipos diferentes de pokémon hay? (Type 1)
'''
len(set(df['Type 1']))


# In[14]:


'''
2. ¿Cuántos pokémon hay de cada tipo? (Type 1)
'''

print([[x,list(df['Type 1']).count(x)] for x in set(df['Type 1'])])

'''
2.1 ¿cual es el tipo de pokémon con más pokémon? (Type 1)
'''

print(max(list(df['Type 1']),key=list(df['Type 1']).count))


# In[15]:


'''
3. ¿Cuál es el pokémon más rápido?
'''

df.sort_values('Speed', ascending=False).head(1)


# In[16]:


'''
4. ¿Cuántos pokemon tiene una defensa superior a 100?
'''
print(len(df[df['Defense'] > 100]))

'''
4.1 ¿Cuántos pokemon tiene una defensa superior a 100?
'''


# In[17]:


'''
5. ¿Cuántos pokemon tiene una defensa superior a 100 y una velocidad superior a 100?
'''

velocidad = len(df[df['Speed'] > 100])
defensa = len(df[df['Defense'] > 100])
print(defensa + velocidad)


# In[18]:


'''
6. Ordena el dataset por el tipo 1 y por el tipo 2
'''

df.sort_values(['Type 1', 'Type 2'])


# In[19]:


'''
7. Crea un nuevo dataset con los pokémon de tipo Water y Fire como primer tipo
'''

df1 = df[df['Type 1'].str.contains('Water|Fire')]
df1


# In[20]:


'''
8. Crea un nuevo dataset con los pokemon Legendary
'''

df2 = (df[df['Legendary'] == True])
df2


# In[21]:


'''
9. Calcula el promedio de stats de los pokemon Legendary (HP, Attack, Defense, Sp. Atk, Sp. Def, Speed) y los no Legendary
'''
 
column_names = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
print(df2.groupby('Legendary')[column_names].mean())

df3 = (df[df['Legendary'] == False])
print(df3.groupby('Legendary')[column_names].mean())


# In[22]:


'''
10. Crea un nuevo dataframe con el resultado del anterior ejercicio comparando ambos promedios

ejemplo:
                HP  Attack  Defense  Sp. Atk  Sp. Def  Speed
Legendary       99      90       89       91       94     90
No Legendary    80      95       75       12       43     87

'''

column_names = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
print(df2.groupby('Legendary')[column_names].mean())
print(df3.groupby('Legendary')[column_names].mean())


# In[68]:


'''
11. Añade una nueva colunma ['Doble tipo'] al dataframe inicial que indique si el pokemo tiene dos tipos o no
'''

df.loc[df['Type 2'].isnull(), 'Doble Tipo'] = 'False' 
df.loc[df['Type 2'].notnull(), 'Doble Tipo'] = 'True'

df.tail(10)


# In[73]:


'''
12. Muestra las columas Name, Type 1, Type 2 de los pokémon que tienen dos tipos y ordenalos por Type 1 , Type 2 y Name
'''

df[['Type 1', 'Type 2', 'Name']][df['Doble Tipo'] == 'True'].sort_values(by=['Type 1', 'Type 2', 'Name'], ascending=[True, True, True])


# In[76]:


from functools import reduce

'''
13. Dada una lista de Artículos con sus precio. Define las siguientes funciones:
Puedes definir más funciones si lo consideras necesario.
'''
articulos = {
    'Camisa': 20,
    'Pantalón': 30,
    'Calcetines': 5,
    'Zapatos': 50,
    'Gorra': 10,
    'Bufanda': 15,
    'Gafas': 25,
    'Reloj': 35,
    'Corbata': 40,
}

compra = ['Camisa', 'Pantalón', 'Pantalón', 'Gorra', 'Gafas', 'Corbata']


# A. Una función que calcule el precio total de la compra USAR REDUCE

def calculate_total_price(articulos, compra):
    return reduce(lambda x, y: x + y, [articulos[item] for item in compra])

print(calculate_total_price(articulos,compra))


#B. Una función que calcule el precio total de la compra con un descuento del 10% 

def discount(articulos, compra):
    total_price = calculate_total_price(articulos, compra)
    return total_price - (total_price * 0.1)
    
print(discount(articulos, compra))

#C. Una función que calcule el precio total de la compra con un descuento del 10% si la compra supera los 100€

def discount2(articulos, compra):
    total_price = calculate_total_price(articulos, compra)
    if total_price > 100:
        return total_price - (total_price * 0.1)
    else:
        return total_price
    
    
print(discount2(articulos, compra))


# D. Una función que calcule el precio total aplicando el IVA (21%)

def iva(articulos, compra):
    total_price = calculate_total_price(articulos, compra)
    return total_price * 1.21
    
print(iva(articulos,compra))

# E.lista los artículos cuyo precio es superior a 20€ USAR FILTER


dict(filter(lambda articulo: articulo[1] > 20, articulos.items()))

'''
def above_20(articulos): # Se entiende mucho mejor
    plus_20 = []
    for key, value in articles.items():
        if value > 20:
            plus_20.append(key)
    return plus_20

print(above_20(articulos))
'''


# In[63]:


'''
14. Dada una lista de tuplas con el nombre de un alumno, apellidos, curso y sus notas. 

 Define una funcion que reciba el curso y saque una lista en la que aparezca e nombre y apellidos y el promedio de sus notas.
 Puedes definir más funciones si lo consideras necesario.
'''

alumnos = [('Juan', 'Pérez', '1', [5, 6, 7, 8, 9]),
            ('Ana', 'García', '2', [5, 6, 7, 8, 9]),
            ('Luis', 'González', '1', [5, 6, 7, 8, 9]),
            ('María', 'Martínez', '2', [5, 6, 7, 8, 9]),
            ('Pedro', 'Rodríguez', '1', [5, 6, 7, 8, 9]),
            ('Lucía', 'Hernández', '2', [5, 6, 7, 8, 9]),
            ('Marta', 'López', '1', [5, 6, 7, 8, 9]),
            ('Sara', 'Díaz', '2', [5, 6, 7, 8, 9]),
            ('Javier', 'Sánchez', '1', [5, 6, 7, 8, 9]),
            ('Miguel', 'Fernández', '2', [5, 6, 7, 8, 9]),
            ('Sergio', 'Jiménez', '1', [5, 6, 7, 8, 9]),
            ('Sandra', 'Ruiz', '2', [5, 6, 7, 8, 9]),
            ('Pablo', 'Álvarez', '1', [5, 6, 7, 8, 9]),
            ('María', 'Gómez', '2', [5, 6, 7, 8, 9]),
]




def sacar_alumnos(curso):
    # filtrar por curso
    alumnos_por_curso = list(filter(lambda alumno: alumno[2] == curso, alumnos))
    alumnos_con_promedio = []
    for alumno in alumnos_por_curso:
        grades = alumno[3]
        average = (reduce(lambda x, y: x + y, grades)) / len(grades)
        alumnos_con_promedio.append((alumno[0], alumno[1], average))
    return alumnos_con_promedio

print(sacar_alumnos('1'))
print(sacar_alumnos('2'))
    


# In[ ]:




