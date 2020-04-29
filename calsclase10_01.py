import re

text = "Mi nombre es magali y tengo 28 años"
buscar = "nombre"

if re.search(buscar, text):
    print(f"La cadena contiene {buscar} entre sus caracteres")
else:
    print(f"La cadena no contiene {buscar} entre sus caracteres")

found_text = re.search()
