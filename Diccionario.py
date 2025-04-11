import time
meme_dict = {
            "NOJODA": "Algo que no te gusta o que te da rabia",
            "ECHE": "Qujarse de algo",
            "PSS": "No estar de acuerdo con alguien",
            "LUKAS": "Forma de decir cuando dinero quieres. ej: 2 lukas = 2 mil pesos",
            "PILAS": "Forma de apresurar a alguien",
            "PILLA": "Forma de decir mira lo que encontre",
           
            }

while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
        print("---------------------------------------------------")
        time.sleep(0.5)
    else:
        print("Perdon, esa palabra no esta :(")
        print("---------------------------------------------------")
        time.sleep(0.5)
