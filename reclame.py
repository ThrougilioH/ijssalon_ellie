def aanbieding_1(smaak, prijs, korting):
    korting_prijs = prijs * korting
    nieuwe_prijs = prijs - korting_prijs
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro.")

aanbieding_1("aardbei", 4, 0.1)