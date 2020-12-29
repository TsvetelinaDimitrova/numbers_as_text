#Zahlen einliest.py
zahl = input("Geben Sie eine Zahl (max 9 Stellen) ein:")
lang  = len(zahl)
result = ""
for i in range(lang):
    if zahl[i] == "1":
        result +=" Eins "
    elif zahl[i] == "2": 
        result +=" Zwei "
    elif zahl[i] == "3": 
        result +=" Drei "
    elif zahl[i] == "4": 
        result +=" Vier "
    elif zahl[i] == "5": 
        result +=" Fünf "
    elif zahl[i] == "6": 
        result +=" Sechs  "
    elif zahl[i] == "7": 
        result +=" Sieben "
    elif zahl[i] == "8": 
        result +=" Acht "
    elif zahl[i] == "9": 
        result +=" Neun "
    elif zahl[i] == "0":
        result += " Null "
    else:
        result += ""    
print(result)

input("Bitte mit Eingabetaste beenden")
