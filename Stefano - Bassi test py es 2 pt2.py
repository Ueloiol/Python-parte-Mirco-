# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CuS48ypo2BY2TQSvqLOJL2KCUsbp9b8i
"""

#10- Creare un menu ad iserimento che permetta in loop di inserire 
#    un nome e una password e che dopo li verifichi scrivendo "loggato!"

#11 


class Utente:
    def __init__(self, User, Pass):     # costruttore 
        self.Username = User
        self.Password = Pass
    
   # def stampatore(self):
      #print(self.Username)
      #print(self.Password)

class Ferie(Utente):
    def __init__(self, User, Pass, spesa, tempo, vista):     # costruttore 
        super().__init__(User, Pass)
        self.spesa = spesa
        self.tempo = tempo
        self.vista = vista

    def stampatore_ferie(self):
        print('nome utente:',self.Username)
        print('password:',self.Password)
        print('spesa totale:', self.spesa)
        print('tempo soggiorno:',self.tempo)
        print('vista mare:',self.vista)  


# inserisco utente
utente_1= Utente('giacomo', '123stella')

#inserisco tipo ferie
Ferie_utente_1= Ferie('giacomo', '123stella', 15000, '7 giorni', True)

# stampo il tipo di vacanza dell'utente
Ferie_utente_1.stampatore_ferie()

#11 


class Utente:
    def __init__(self, User, Pass):     # costruttore 
        self.Username = User
        self.Password = Pass
    
   # def stampatore(self):
      #print(self.Username)
      #print(self.Password)

class Ferie(Utente):
    def __init__(self, User, Pass, spesa, tempo, vista):     # costruttore 
        super().__init__(User, Pass)
        self.spesa = spesa
        self.tempo = tempo
        self.vista = vista

    def stampatore_ferie(self):
        print('nome utente:',self.Username)
        print('password:',self.Password)
        print('spesa totale:', self.spesa)
        print('tempo soggiorno:',self.tempo)
        print('vista mare:',self.vista)  


# inserisco utente
utente_1= Utente('giacomo', '123stella')

#inserisco tipo ferie
Ferie_utente_1= Ferie('giacomo', '123stella', 15000, '7 giorni', True)


flag= True

while flag == True:
  x=int(input('scegli cosa fare: 1. esci 2. login'))
  if x==1:
    flag=False
  elif x==2:
        user_login=input('accedi inserendo il nome utente')
        password_login= input('accedi inserendo la password')
        if utente_1.Username == user_login and utente_1.Password == password_login :
          print('congratulazioni hai effettuato il login con successo')

          # stampo il tipo di vacanza dell'utente
          Ferie_utente_1.stampatore_ferie()