

class Ordinazione_Cliente():
    nome_ordinatore = ''
    piatti_ordinati = {}
    #piatti_ordinati = [pl1,pl2,pl3,pl4]
    spesa_totale = 0

Ordinazione_1=Ordinazione_Cliente()

menu_piatti = ['pasta', 'carne', 'pesce', 'dolce']
menu_prezzi = [20,25,30,10]

flag= True

while flag==True:
      
    scelta =int(input('(1) Ordina (2) esci'))

    # SCELTA 1: il cliente inserisce un nuovo piatto
    if scelta ==1:  
        
        flag_2 = True
        while flag_2==True:

            operazione=int(input('cosa vuoi fare? (1) aggiungi ordine (2) modifica (3) conto (4) menu iniziale'))

            # (1) AGGIUNGI ORDINE
            if operazione ==1:
                nome = input('inserisci nome cliente:')
                Ordinazione_1.nome_ordinatore=nome
                
                piatto = int(input('inserisci piatto: (0)pasta (1)carne (2)pesce (3)dolce'))
                Ordinazione_1.piatti_ordinati[menu_piatti[piatto]]=menu_prezzi[piatto]


            # (3) STAMPA IL CONTO
            elif operazione == 3:
                conto=0
                for key in Ordinazione_1.piatti_ordinati:
                    conto += Ordinazione_1.piatti_ordinati[key][0]*Ordinazione_1.piatti_ordinati[key][1]


            # (4) TORNA AL MENU INIZIALE
            elif operazione == 4:
                flag_2= False



    # SCELTA 2: esci
    elif scelta == 2:
        flag=False