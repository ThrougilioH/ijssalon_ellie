import statistics
from algemene_functies import mijn_functie_2  

def aanbieding_1(smaak, prijs, korting):
    korting_prijs = prijs * korting
    nieuwe_prijs = prijs - korting_prijs
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * float(btw / 100)
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]

def gemiddelde(mijn_lijst):
    bedrag = statistics.mean(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {bedrag} euro."

def meervoudig(invoer_lijst):
    if invoer_lijst > 4 and invoer_lijst < 11:
        return laag_en_hoog(int(invoer_lijst))
    
def combinatie(invoer_lijst_2): 
    korte_lijst = meervoudig(invoer_lijst_2)
    return mijn_functie_2(korte_lijst)