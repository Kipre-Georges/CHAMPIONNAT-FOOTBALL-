 
#LISTE DES IMPORT
from cProfile import label
from cgitb import text
from dataclasses import replace
from multiprocessing.sharedctypes import Value
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


#traitement Championnat 1(BUNDESLIGA)
if choix_championnat == 1 :
    
    first_bundesliga=requests.get(Bundesliga)
    response_first_bundesliga=BeautifulSoup(first_bundesliga.text, "html.parser")
    tableau_Bundesliga=response_first_bundesliga.find_all(class_="classement__team")
    point_bundesliga=requests.get(Bundesliga)
    response_point_bundesliga=BeautifulSoup(point_bundesliga.text,"html.parser")
    tableau_point_bundesliga=response_point_bundesliga.find_all(class_="classement__highlight")
    
    print("Le premier de Bundesliga  est :", tableau_Bundesliga[1].text.lstrip().rstrip(),"avec "  , tableau_point_bundesliga[1].text, "Points.")    
    print("")
    print("Le deuxième de Bundesliga  est :", tableau_Bundesliga[2].text.lstrip().rstrip(),"avec " , tableau_point_bundesliga[2].text, "Points.")
    print("") 
    print("Le troisième de Bundesliga  est :", tableau_Bundesliga[3].text.lstrip().rstrip(),"avec " , tableau_point_bundesliga[3].text, "Points.")  
    print("")  
    print("Le quatrième de Bundesliga  est :", tableau_Bundesliga[4].text.lstrip().rstrip(),"avec " , tableau_point_bundesliga[4].text, "Points.")
    print("")    
    print("Le cinquième de Bundesliga  est :", tableau_Bundesliga[5].text.lstrip().rstrip(),"avec " , tableau_point_bundesliga[5].text, "Points.")   
    print("") 
    
    
    


    
    
