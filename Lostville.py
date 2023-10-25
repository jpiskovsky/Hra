import random
import math
import time


text = "Lostville"
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.2)
    
print()
time.sleep(1)

text1 = "Rok 1945"
for char in text1:
    print(char, end='', flush=True)
    time.sleep(0.2)

print()
time.sleep(1)

text2 = "Johny: Jmenuju se Johny, je mi 22 let a sloužil jsem u americké armády v Itálii na Sicílii."
for char in text2:
    print(char, end='', flush=True)
    time.sleep(0.1)
    
print()
time.sleep(1)

text3 = "Válka skončila a já jedu zpátky do svého rodného města Lostville."
for char in text3:
    print(char, end='', flush=True)
    time.sleep(0.1)
    
print()
time.sleep(1)

text4 = "Na nádraží už na mě čeká můj kamarád Lišák..."
for char in text4:
    print(char, end='', flush=True)
    time.sleep(0.1)
    
    
print()
time.sleep(2)

print()
print("Celník: Vítejte v Lostville. Předložte své doklady prosím.")
time.sleep(3)

print()
print("Johny: Dobrý den, samozřejmě, tady máte.")
time.sleep(2)

print()
while(True):
    jméno = (input("Zadejte jméno hlavní postavy: "))
    Johny = ("Johny")
    vek = int(input("Zadejte věk hlavní postavy: "))
    vek_Johny = 22
    if jméno == Johny and vek == vek_Johny:
        print()
        print("Celník: V pořádku, vítejte ve městě.")
        break
    else:
        print()
        print("Celník: Zkuste to znovu.")
        time.sleep(2)
        print()
        
time.sleep(3)
print()
print("Lišák: Nazdar kámo, tak rád tě vidím.") 
time.sleep(3)
print("Jaký to bylo v Itálii?")

time.sleep(3)
print()
print("Johny: Ahoj Lišáku, taky tě rád vidím.")
time.sleep(3)
print("V Itálii?")
time.sleep(2)
print("Nooo...zrovna dovolená to nebyla, viděl jsem dost nepěkný věci.")
time.sleep(3)
print("Víc bych to nerozebíral.")

time.sleep(3)
print()
print("Lišák: To chápu, důležitý je, že seš celej. Pojď ukážu ti město.")

time.sleep(3)
print()
print("Johny: To zní dobře.")

time.sleep(3)
print()
print("Lišák: Johny?")
time.sleep(1)
print("Chceš řídit?")

time.sleep(3)
print()
rizeni = (input("Chceš řídit(ano, ne): "))
if rizeni == "ano":
    print("Lišák: Dobře, tady máš klíčky.")
    time.sleep(2)
    print("Hlavně opatrně, víš jak dlouho jsi nejezdil :D.")
    time.sleep(2)
    print()
    print("Johny: Náhodou, v armádě jsem jezdil jeepem.")
else:
    print()
    print("Lišák: Dobře, pojedu já.")
    
time.sleep(3)
print()
print("Po 10 minutáh jízdy...")

time.sleep(3)
print()
print("Lišák: Johny, tady zastav. Stavíme se na jídlo v místní hospodě.")

time.sleep(3)
print()
print("Johny: Čteš mi myšlenky kámo, mám hlad jako vlk.")

time.sleep(3)
print()
print("V hospodě je hospodský kvíz.")
time.sleep(2)
print("Čekají tě 3 otázky z oblasti elektrotechniky:")
time.sleep(3)

print()
while(True):
    otazka1 = (input("Hospodský: 1. - Jaká je základní jednotka elektrického odporu?: "))
    zakl_jednotka = "ohm"
    if otazka1 == zakl_jednotka:
        print()
        print("Hospodský: Anoo, Johny a Lišák odpověděli správně.")
        time.sleep(3)
        print()
        print("Lišák: Skvěle Johny, jen tak dál.")
        break
    else:
        print()
        print("Hospodský: Bohužel, to není správná odpověď.")
        time.sleep(2)
        print()
    

time.sleep(3)
print()
while(True):
    otazka2 = int(input("Hospodský: 2. - Jaký proud prochází spotřebičem o odporu 10 Ω , je-li připojen k napětí 20 V? (výsledek uveď bez jednotky): "))
    odpoved2 = 2 
    if otazka2 == odpoved2:
        print()
        print("Hospodský: Aaa, je to správně, další bod pro Lišáka s Johnym.") 
        time.sleep(3)
        print()
        print("Lišák: Johny výborně, výborně.")
        break
    else:
        print()
        print("Hospodský: Mrzí mě to, ale to je špatná odpověď.")
        time.sleep(2)
        print()
        
time.sleep(3)
print()
while(True):
    otazka3 = input("Hospodský: 3. - Jak se nazýva fyzikální veličina, která má značku U (odpověď s diakritikou): ")
    odpoved3 = "napětí"
    if otazka3 == odpoved3:
        print()
        print("Hospodský: To je neuvěřitelné, třetí správná odpověď za sebou. Dobrá Práce.")
        time.sleep(3)
        print()
        print("Lišák: Ty jsi v té armádě snad studoval dálkově Božetěchovu ne? Dobrá práce kámo.")
        time.sleep(3)
        print()
        print("Johny: Ty jsi vůl, ale jinak díky za pochvalu :D.")
        break
    
    else:
        print()
        print("Hospodský: Ne ne, to není správně.")
        time.sleep(2)
        print()
        

time.sleep(3) 
print()     
print("Lišák: Whohoou, povím ti, to bylo něco Johny.")

time.sleep(3)
print()
print("Johny: No jo, pořád mi to myslí.")
time.sleep(2)
print("...")
time.sleep(1)
print("Narozdíl od tebe :D.")

time.sleep(2)
print()
print("Lišák: Pojď radši :D.")
time.sleep(2)
print("Zajedeme do kasína.")
time.sleep(2)
print("Trochu se pobavit.")

time.sleep(3)
print()
print("Cestou...")

time.sleep(2)
print()
print("Booom")

time.sleep(1)
print()
print("Johny: Sakra, co to bylo za ránu??")

time.sleep(3)
print()
print("Lišák: Píchli jsme gumu.")
time.sleep(2)
print("Musíme zastavit.")

time.sleep(3)
print()
print("Johny: Je to hodně zlý?")

time.sleep(3)
print()
print("Lišák: Je to na výměnu.")
time.sleep(2)
print("Máme dvě možnosti.")
time.sleep(2)
print("Buď gumu vyměníme sami.")
time.sleep(1)
print("nebo")
time.sleep(1)
print("Auto dotlačíme k mechanikovi.")

time.sleep(3)
print()
while(True):
    guma = (input("Chceš auto opravit sám nebo zaměstnat mechanika? (odpovědi - sám/mechanik): "))
    sam = ("sám")
    mechanik = ("mechanik")
    if guma == sam:
        print("Johny: To bude hračka, opravím to sám.")
        time.sleep(2)
        print("Podej mi nářadí")
        time.sleep(2)
        print()
        print("O 20 minut později...")
        time.sleep(2)
        print()
        print("Johny: A je to, můžeme jet dál.")
        time.sleep(3)
        print()
        print("Lišák: Jseš dobrej, výměna jak od mechanika.")
        break
    else: 
        print("Na to jsme sami krátcí, budeme tu káru muset dotlačit k mechanikovi.")
        time.sleep(2)
        print("Jak je to daleko?")
        time.sleep(3)
        print()
        print("Lišák: Naštěstí kousek, hned tady za rohem.")
        time.sleep(2)
        print()
        print("O 15 minut později...")
        time.sleep(2)
        print()
        print("Lišák: Dobrej, mohl byste nám vyměnit kolo za rezervu?")
        time.sleep(2)
        print("Píchli jsme.")
        time.sleep(3)
        print()
        print("Mechanik: Dobrej chlapi, samozřejmě, není problém.")
        time.sleep(2)
        print("Mechanik: Dejte mi 10 minutek.")
        time.sleep(2)
        print()
        print("0 30 minut později...")
        break
    
time.sleep(3)
print()
print("Již před kasínem...")

time.sleep(2)
print()
print("Lišák: Tady po pravé straně máme kasíno, zastav.")

time.sleep(3)
print()
print("Nacházíš se v kasínu.")
time.sleep(2)
print("Před tebou stojí kolo štěstí.")
time.sleep(2)
print("Toč do té doby, dokud nepadne výherní červená.")

time.sleep(2)
print()
while(True):
    zvolena_barva = int(input("Zatoč (1): "))
    spin = 1
    colors = ["červená", "žlutá", "zelená", "černá"]
    vysledek = random.choices(colors, weights = [7,10,10,10])[0]
    
    if spin == 1 and vysledek == "červená":
        print(f"Vyhráváte hlavní cenu! - barva:{vysledek}")
        break
    else:
        print(f"Žádná výhra - barva: {vysledek}")
        time.sleep(1)
        print()
        print("Zkus to znovu...")
        time.sleep(1)
        print()
        
time.sleep(3)
print()
print("Lišák: Výhra, výhra...Johny my jsme vyhráli.")

time.sleep(3)
print()
print("Johny: Jooo")
time.sleep(1)
print("Ale v nejlepším se má přestat.")
time.sleep(2)
print("Pojď Lišáku, jdeme pryč.")

time.sleep(3)
print()
print("Lišák: Poslední věc, kterou bych ti ještě dnes chtěl ukázat je matematický kvíz v Salieriho baru.")
time.sleep(3)
print("Pojď, jedeme.")

time.sleep(3)
print()
print("...")

time.sleep(2)
print()
print("Lišák: Jsme tady.")
time.sleep(2)
print("Zaparkuj vedle toho modrého Mercedesu.")

time.sleep(3)
print()
print("Salieri: Mám pro vás poslední kvíz dnešního večera.")
time.sleep(3)
print("Úkolem je vypočítat 4 příklady v co nejkratším čase.")
time.sleep(3)
print("Vítěz dostane kvalitní francouzské víno!")

time.sleep(3)
print()
print("Lišák: Johny, bar je plnej...")
time.sleep(2)
print("Budeme muset máknout.")

time.sleep(3)
print()
print("Johny: Hah, neboj se.")
time.sleep(3)
print("S touhle hračkou to půjde levou zadní.")

time.sleep(3)
print()
print("Lišák: Cože? :D")
time.sleep(1)
print("Ty máš kalkulačku?")
time.sleep(2)
print("No já se poseru :D.") 

time.sleep(3)
print()
print("Salieri: 1. příklad: 17 + 29")

time.sleep(2)
print()
while(True):
    hodnota1 = int(input("Zadejte první číslo: "))
    hodnota2 = int(input("Zadejte druhé číslo: "))
    operace = input("Jakou chcete provést operaci? (+,-,*,/): ")
    vysledek1 = hodnota1 + hodnota2
    vysledek2 = hodnota1 - hodnota2
    vysledek3 = hodnota1 * hodnota2
    vysledek4 = hodnota1 / hodnota2

    if operace == "+":
        vysledek = hodnota1 + hodnota2

    elif operace == "-":
        vysledek = hodnota1 - hodnota2

    elif operace == "*":
        vysledek = hodnota1 * hodnota2

    else:
        vysledek = hodnota1 / hodnota2
  
    print() 
    if vysledek == 46:
        print(f"Johny: Výsledek je {vysledek}.")
        time.sleep(2)
        print()
        print("Salieri: Anoo, pan Johny odpověděl jako první správnou odpověď.")
        break
    else:
        print(f"Johny: Výsledek je {vysledek}.") 
        time.sleep(2)
        print()
        print("Salieri: Mrzí mě to, ale to je špatná odpoveď.")
        time.sleep(2)
        print()
    
time.sleep(3)
print()
print("Salieri: 2. příklad: 5 * 12")

time.sleep(2)
print()

while(True):
    hodnota1 = int(input("Zadejte první číslo: "))
    hodnota2 = int(input("Zadejte druhé číslo: "))
    operace = input("Jakou chcete provést operaci? (+,-,*,/): ")
    vysledek1 = hodnota1 + hodnota2
    vysledek2 = hodnota1 - hodnota2
    vysledek3 = hodnota1 * hodnota2
    vysledek4 = hodnota1 / hodnota2

    if operace == "+":
        vysledek = hodnota1 + hodnota2

    elif operace == "-":
        vysledek = hodnota1 - hodnota2

    elif operace == "*":
        vysledek = hodnota1 * hodnota2

    else:
        vysledek = hodnota1 / hodnota2
  
    print()
    if vysledek == 60:
        print(f"Johny: Výsledek je {vysledek}.")
        time.sleep(2)
        print()
        print("Salieri: Johny opět, první správná odpověď.")
        break
    else:
        print(f"Johny: Výsledek je {vysledek}.") 
        time.sleep(2)
        print()
        print("Salieri: Nene, to není správná odpověď.")
        time.sleep(2)
        print()
    
time.sleep(3)
print()
print("Salieri: 3. příklad: 333 - 97")

time.sleep(2)
print()
while(True):
    hodnota1 = int(input("Zadejte první číslo: "))
    hodnota2 = int(input("Zadejte druhé číslo: "))
    operace = input("Jakou chcete provést operaci? (+,-,*,/): ")
    vysledek1 = hodnota1 + hodnota2
    vysledek2 = hodnota1 - hodnota2
    vysledek3 = hodnota1 * hodnota2
    vysledek4 = hodnota1 / hodnota2

    if operace == "+":
        vysledek = hodnota1 + hodnota2

    elif operace == "-":
        vysledek = hodnota1 - hodnota2

    elif operace == "*":
        vysledek = hodnota1 * hodnota2

    else:
        vysledek = hodnota1 / hodnota2
  
    print() 
    if vysledek == 236:
        print(f"Johny: Výsledek je {vysledek}.")
        time.sleep(2)
        print()
        print("Salieri: Přesně tak, jako první odpověděl správně Johny.")
        break
    else:
        print(f"Johny: Výsledek je {vysledek}.") 
        time.sleep(2)
        print()
        print("Salieri: Je mi líto, to není dobře.")
        time.sleep(2)
        print()
        
time.sleep(3)
print()
print("Salieri: 4. příklad: 81 / 9")

time.sleep(2)
print()
while(True):
    hodnota1 = int(input("Zadejte první číslo: "))
    hodnota2 = int(input("Zadejte druhé číslo: "))
    operace = input("Jakou chcete provést operaci? (+,-,*,/): ")
    vysledek1 = hodnota1 + hodnota2
    vysledek2 = hodnota1 - hodnota2
    vysledek3 = hodnota1 * hodnota2
    vysledek4 = hodnota1 / hodnota2


    if operace == "+":
        vysledek = hodnota1 + hodnota2

    elif operace == "-":
        vysledek = hodnota1 - hodnota2

    elif operace == "*":
        vysledek = hodnota1 * hodnota2

    else:
        vysledek = hodnota1 / hodnota2
  
    print() 
    if vysledek == 9:
        print(f"Johny: Výsledek je {vysledek}.")
        time.sleep(2)
        print()
        print("Salieri: A znovu, Johny první!")
        break
    else:
        print(f"Johny: Výsledek je {vysledek}.") 
        time.sleep(2)
        print()
        print("Salieri: Bohužel, takový výsledek není.")
        time.sleep(2)
        print()
        
time.sleep(3)
print()
print("Lišák: Joooo")
time.sleep(1)
print("Lišák: Máme to.")

time.sleep(2)
print()
print("Johny: Yess, mám radost.")
time.sleep(3)
print("AÁAÁa")
time.sleep(3)
print("Šel bych na kutě.")
time.sleep(3)
print("Lišáku, popadni to víno a jedeme domů.")

time.sleep(3)
print()
print("Lišák: Souhlasím.")

time.sleep(3)
print()
print("Lišák: Tak tady to je - Wallstreet 6.")
time.sleep(2)
print("Bydlím v druhým patře.")

time.sleep(3)
print()
print("Později v bytě...")

time.sleep(3)
print()
print("Johny: Máš to tady moc pěkný.")
time.sleep(2)
print("To se musí nechat.")

time.sleep(3)
print()
print("Lišák: Díky, jsem rád, že se ti tu líbí.")
time.sleep(3)
print("Lišák: Buď budeš spát v kuchyni nebo v obýváku.")
time.sleep(2)
print("Vyber si.")

time.sleep(3)
print()
spani = (input("Kde chceš spát? (kuchyně, obývák): "))
if spani == "kuchyně":
    print("Lišák: Dobře nachystám ti postel v kuchyni.")
else:
    print("Lišák: Dobře, nachystám ti postel v obýváku.")
    
time.sleep(3)
print()
print("22:30...")

time.sleep(3)
print()
print("Johny: Za dnešek ti děkuju Lišáku, užil jsem si ho.")

time.sleep(3)
print()
print("Lišák: Vůbec nemáš za co Johny. Teď už odpočívej.")
time.sleep(2)
print("Dobrou noc.")

time.sleep(2)
print()
print("Johny: Dobrou")
    


