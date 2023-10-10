import pandas as pd


data = {
    'Nombre': ['Persona1', 'Persona2', 'Persona3', 'Persona4', 'Persona5'],
    'is_dead': [1, 0, 1, 0, 0],
    'edad': [32, 45, 21, 29, 38],
    'genero': ['M', 'F', 'M', 'F', 'M'],
    'fuma': ['S', 'S', 'N', 'S', 'N']
}

df = pd.DataFrame(data)

print("\n***************************************************************\n")

print(df)

print("\n***************************************************************\n")

tipos_de_datos = df.dtypes
print("Tipos de datos en cada columna:")

print(tipos_de_datos)

print("\n***************************************************************\n")
cantidad_hombres_fumadores = df[(df['genero'] == 'M') & (df['fuma'] == 'S')].shape[0]
cantidad_mujeres_fumadoras = df[(df['genero'] == 'F') & (df['fuma'] == 'S')].shape[0]

print("\nCantidad de hombres fumadores:", cantidad_hombres_fumadores)
print("Cantidad de mujeres fumadoras:", cantidad_mujeres_fumadoras)

print("\n***************************************************************\n")
