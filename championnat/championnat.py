#LISTE DES IMPORT
from cProfile import label
from cgitb import text
from multiprocessing.sharedctypes import Value
import bs4
from bs4 import BeautifulSoup
import requests
import re


#LISTE DES CHAMPIONNATS A SCRAPPER
Bundesliga='https://www.footmercato.net/allemagne/bundesliga/classement'
Premier_league='https://www.footmercato.net/angleterre/premier-league/classement'
Liga='https://www.footmercato.net/espagne/liga/classement'
Ligue_1='https://www.footmercato.net/france/ligue-1/classement'
Serie_A='https://www.footmercato.net/italie/serie-a/classement'


#PRESENTATION DES CHAMPIONNATS 
print("Pour le championnat Allemand tapez 1")
print("Pour le championnat Anglais tapez 2")
print("Pour le championnat Espagnol tapez 3")
print("Pour le championnat Français tapez 4")
print("Pour le championnat Italien tapez 5")

#SELECTION CHAMPIONNAT
choix_championnat=int(input("Sélectionnez votre championnat en tapant sur  1  , 2 , 3 , 4 , 5 : "))

#BUNDESLIGA
#classement__team -> class des équipes composant le championnat Allemand


#traitement Championnat 1(BUNDESLIGA)
if choix_championnat ==1 :
    Bundesliga="https://www.footmercato.net/allemagne/bundesliga/classement"
    first_bundesliga=requests.get(Bundesliga)
    response_first_bundesliga=BeautifulSoup(first_bundesliga.text, "html.parser")
    
    tableau=response_first_bundesliga.find_all(class_="classement__team")
    print(tableau[1])
    