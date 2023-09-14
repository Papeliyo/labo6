###---=== ejercicio 1 ===---

lista = [5,3,7,2,8]
lista.append(10)
lista.append(20)
lista.insert(0,0)
print(f'Lista: {lista}')
lista.remove(10)
new_list = lista.index(20)
lista.sort(reverse=True)
print(f'Lista: {lista}')
print(f'index de 20: {new_list}')

###---=== ejercicio 2 ===---

tupla = ["python", "programacion", "python", "desarrollo", "python"]
conteo = tupla.count("python")
indice = tupla.index("programacion")
print(f"Conteo de python en la tupla: {conteo}, y el indice de programacion es {indice}")

###---=== ejercicio 3 ===---

diccionario = {"a": 1, "b": 2, "c": 3}
diccionario.update({"d": 4})
valor = diccionario.get("b")
print(f"Diccionario final: {diccionario}, y el valor de b: {valor}")
diccionario.update({"c": 30})
print(f"Diccionario actualizado: {diccionario}")
