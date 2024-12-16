from helper import *
from presentatie import *
import csv


inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vannile-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsje-ijs-totaal" : 750
}

totaal_inkomsten = int(som(inkomsten))

presenteer(inkomsten, totaal_inkomsten)

with open('boekhouding.csv', 'w',newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimter=';') 
    writer.writerow([key,value])