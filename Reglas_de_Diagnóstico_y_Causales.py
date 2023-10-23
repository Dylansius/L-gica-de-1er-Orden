# Variables que representan los sintomas del paciente
tiene_fiebre = True
tiene_tos = True
tiene_dolor_de_garganta = False

# Reglas de diagnostico
if tiene_fiebre and tiene_tos and tiene_dolor_de_garganta:
    print("El paciente tiene sintomas de gripe.")
elif tiene_fiebre and tiene_tos:
    print("El paciente podria tener una infeccion respiratoria.")
elif tiene_fiebre:
    print("El paciente podria tener una infeccion sin especificar.")
else:
    print("El paciente no parece tener sintomas graves.")

# Reglas causales
if tiene_fiebre:
    print("La fiebre puede ser causada por diversas enfermedades, consulte a un medico para un diagnostico preciso.")
if tiene_tos:
    print("La tos podria deberse a una infeccion respiratoria o alergia, consulte a un medico para un diagnostico adecuado.")
if tiene_dolor_de_garganta:
    print("El dolor de garganta podria ser el resultado de una infeccion viral o bacteriana, consulte a un medico para un diagnostico y tratamiento adecuados.")

