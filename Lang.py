

def switch(lang):
    while(lang != "esci"):
        if lang == "Javascript":
            return "you can become a web developer"
        elif lang == "PHP":
            return "you can become a backend developer"
        elif lang == "Python":
            return "you can become a data scientist"
        elif lang == 'Solidity':
            return "You can become a blockchain developer"
        elif lang == "Java":
            return "You can become a mobile app developer"
        elif lang == "esci":
            break
        else:
            continue

        
lang= "ok"

while(lang != "esci" ):

    lang = input ("inserisci elemento")

    print(switch(lang))