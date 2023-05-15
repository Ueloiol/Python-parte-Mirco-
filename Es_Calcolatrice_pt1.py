

# OPERAZIONE





class Operazioni:
    def __init__(self, numero1, numero2):
      self.addizione_1 = numero1 + numero2
      self.sottrazione_2 = numero1 - numero2
      self.moltiplicazione_3 = numero1 * numero2


flag= True

while flag == True:

    scelta = int(input('inserisci l operazione che vuoi eseguire: (1) uscire \n (2) operazioni \n (3) stampa '))
    print(scelta)

    if scelta == 1:
        flag = False

    elif scelta == 2:

        risultati= [0]*3

        for i in [0,1,2]:
            a= int(input('inserisci il primo numero: '))
            b= int(input('inserisci il secondo numero: '))
            scelta_bis= int(input('inserisci il tipo di operazione: (1) addizione (2) sottrazione (3) moltiplicazione'))

            Tentativo = Operazioni(a,b)

            if scelta_bis == 1:
                addizione = Tentativo.addizione_1
                risultati[i]=addizione

            elif scelta_bis == 2:
                sottrazione = Tentativo.sottrazione_2
                risultati[i]=sottrazione

            elif scelta_bis == 3:
                moltiplicazione = Tentativo.moltiplicazione_3
                risultati[i]=moltiplicazione
        
        somma= risultati[0] + risultati[1] + risultati[2]
        print(somma)

    elif scelta == 3:
        print(risultati[0])
        print(risultati[1])
        print(risultati[2])


    









 


        