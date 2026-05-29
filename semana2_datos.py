import json

# 1. Abrimos el archivo en modo lectura ('r' de read) con codificación UTF-8 para evitar problemas con tildes o la 'ñ'
with open("data/test_dataset.json", "r", encoding="utf-8") as archivo:
    
    # 2. Convertimos el contenido del JSON en una lista de diccionarios de Python
    dataset = json.load(archivo)

print("--- DATASET CARGADO CORRECTAMENTE ---")

# 3. Recorremos cada caso de prueba con un bucle para comprobar qué hemos leído
for caso in dataset:
    id_caso = caso["id"]
    texto = caso["texto"]
    esperado = caso["esperado"]
    
    # Imprimimos un resumen en la consola usando f-strings
    # [:20] sirve para recortar el texto y que no nos llene la pantalla si es muy largo
    print(f"Caso {id_caso}: Evaluar '{texto[:20]}...' -> Resultado Esperado: {esperado}")