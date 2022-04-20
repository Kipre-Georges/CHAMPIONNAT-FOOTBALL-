 
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
print("Pour les 5 championnats important d'Europe tapez 6 ")

#SELECTION CHAMPIONNAT
choix_championnat=int(input("Sélectionnez votre championnat en tapant sur  1  , 2 , 3 , 4 , 5 , 6 : "))



if choix_championnat == 1 :
    
    first_bundesliga=requests.get(Bundesliga)
    response_first_bundesliga=BeautifulSoup(first_bundesliga.text, "html.parser")
    tableau_Bundesliga=response_first_bundesliga.find_all(class_="classement__team")
    point_bundesliga=requests.get(Bundesliga)
    response_point_bundesliga=BeautifulSoup(point_bundesliga.text,"html.parser")
    tableau_point_bundesliga=response_point_bundesliga.find_all(class_="classement__highlight")

    print("")
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
    
if choix_championnat == 2 :
    first_premier_league=requests.get(Premier_league)
    response_first_premier_league=BeautifulSoup(first_premier_league.text,"html.parser")
    tableau_premier_league=response_first_premier_league.find_all(class_="classement__team")
    point_premier_league=requests.get(Premier_league)
    response_point_premier_league=BeautifulSoup(point_premier_league.text,"html.parser")
    tableau_point_premier_league=response_point_premier_league.find_all(class_="classement__highlight")

    print("")
    print("Le premier de Premier League est :", tableau_premier_league[1].text.lstrip().rstrip(),"avec " , tableau_point_premier_league[1].text, "Points.")    
    print("")
    print("Le deuxième de Premier League est :", tableau_premier_league[2].text.lstrip().rstrip(),"avec " , tableau_point_premier_league[2].text, "Points.") 
    print("")  
    print("Le troisième de Premier League est :", tableau_premier_league[3].text.lstrip().rstrip(),"avec " , tableau_point_premier_league[3].text, "Points.")
    print("")  
    print("Le quatrième de Premier League est :", tableau_premier_league[4].text.lstrip().rstrip(),"avec " , tableau_point_premier_league[4].text, "Points.")
    print("")   
    print("Le cinquième de Premier League est :", tableau_premier_league[5].text.lstrip().rstrip(),"avec " , tableau_point_premier_league[5].text, "Points.")
    print("")

if choix_championnat == 3 :
    first_liga=requests.get(Liga)
    response_first_liga=BeautifulSoup(first_liga.text,"html.parser")
    tableau_liga=response_first_liga.find_all(class_="classement__team")
    point_liga=requests.get(Liga)
    response_point_liga=BeautifulSoup(point_liga.text,"html.parser")
    tableau_point_liga=response_point_liga.find_all(class_="classement__highlight")

    print("")
    print("Le premier de Liga est :", tableau_liga[1].text.lstrip().rstrip(),"avec " , tableau_point_liga[1].text, "Points.")    
    print("")
    print("Le deuxième de Liga est :", tableau_liga[2].text.lstrip().rstrip(),"avec " , tableau_point_liga[2].text, "Points.") 
    print("")  
    print("Le troisième de Liga est :", tableau_liga[3].text.lstrip().rstrip(),"avec " , tableau_point_liga[3].text, "Points.")
    print("")  
    print("Le quatrième de Liga est :", tableau_liga[4].text.lstrip().rstrip(),"avec " , tableau_point_liga[4].text, "Points.")
    print("")   
    print("Le cinquième de Liga est :", tableau_liga[5].text.lstrip().rstrip(),"avec " , tableau_point_liga[5].text, "Points.")
    print("")

if choix_championnat == 4 :
    first_ligue_1=requests.get(Ligue_1)
    response_first_ligue_1=BeautifulSoup(first_ligue_1.text,"html.parser")
    tableau_ligue_1=response_first_ligue_1.find_all(class_="classement__team")
    point_ligue_1=requests.get(Ligue_1)
    response_point_ligue_1=BeautifulSoup(point_ligue_1.text,"html.parser")
    tableau_point_ligue_1=response_point_ligue_1.find_all(class_="classement__highlight")

    print("")
    print("Le premier de Ligue 1 est :", tableau_ligue_1[1].text.lstrip().rstrip(),"avec " , tableau_point_ligue_1[1].text, "Points.")    
    print("")
    print("Le deuxième de Ligue 1 est :", tableau_ligue_1[2].text.lstrip().rstrip(),"avec " , tableau_point_ligue_1[2].text, "Points.") 
    print("")  
    print("Le troisième de Ligue 1 est :", tableau_ligue_1[3].text.lstrip().rstrip(),"avec " , tableau_point_ligue_1[3].text, "Points.")
    print("")  
    print("Le quatrième de Ligue 1 est :", tableau_ligue_1[4].text.lstrip().rstrip(),"avec " , tableau_point_ligue_1[4].text, "Points.")
    print("")   
    print("Le cinquième de Ligue 1 est :", tableau_ligue_1[5].text.lstrip().rstrip(),"avec " , tableau_point_ligue_1[5].text, "Points.")
    print("")

if choix_championnat == 5 :
    first_serie_a=requests.get(Serie_A)
    response_first_serie_a=BeautifulSoup(first_serie_a.text,"html.parser")
    tableau_serie_a=response_first_serie_a.find_all(class_="classement__team")
    point_serie_a=requests.get(Serie_A)
    response_point_serie_a=BeautifulSoup(point_serie_a.text,"html.parser")
    tableau_point_serie_a=response_point_serie_a.find_all(class_="classement__highlight")

    print("")
    print("Le premier de Serie A est :", tableau_serie_a[1].text.lstrip().rstrip(),"avec " , tableau_point_serie_a[1].text, "Points.")    
    print("")
    print("Le deuxième de Serie A est :", tableau_serie_a[2].text.lstrip().rstrip(),"avec " , tableau_point_serie_a[2].text, "Points.") 
    print("")  
    print("Le troisième de Serie A est :", tableau_serie_a[3].text.lstrip().rstrip(),"avec " , tableau_point_serie_a[3].text, "Points.")
    print("")  
    print("Le quatrième de Serie A est :", tableau_serie_a[4].text.lstrip().rstrip(),"avec " , tableau_point_serie_a[4].text, "Points.")
    print("")   
    print("Le cinquième de Serie A est :", tableau_serie_a[5].text.lstrip().rstrip(),"avec " , tableau_point_serie_a[5].text, "Points.")
    print("")

if choix_championnat == 6 :
    first_bundesliga=requests.get(Bundesliga)
    response_first_bundesliga=BeautifulSoup(first_bundesliga.text, "html.parser")
    tableau_Bundesliga=response_first_bundesliga.find_all(class_="classement__team")
    point_bundesliga=requests.get(Bundesliga)
    response_point_bundesliga=BeautifulSoup(point_bundesliga.text,"html.parser")
    tableau_point_bundesliga=response_point_bundesliga.find_all(class_="classement__highlight")

    first_premier_league=requests.get(Premier_league)
    response_first_premier_league=BeautifulSoup(first_premier_league.text,"html.parser")
    tableau_premier_league=response_first_premier_league.find_all(class_="classement__team")
    point_premier_league=requests.get(Premier_league)
    response_point_premier_league=BeautifulSoup(point_premier_league.text,"html.parser")
    tableau_point_premier_league=response_point_premier_league.find_all(class_="classement__highlight")

    first_liga=requests.get(Liga)
    response_first_liga=BeautifulSoup(first_liga.text,"html.parser")
    tableau_liga=response_first_liga.find_all(class_="classement__team")
    point_liga=requests.get(Liga)
    response_point_liga=BeautifulSoup(point_liga.text,"html.parser")
    tableau_point_liga=response_point_liga.find_all(class_="classement__highlight")

    first_ligue_1=requests.get(Ligue_1)
    response_first_ligue_1=BeautifulSoup(first_ligue_1.text,"html.parser")
    tableau_ligue_1=response_first_ligue_1.find_all(class_="classement__team")
    point_ligue_1=requests.get(Ligue_1)
    response_point_ligue_1=BeautifulSoup(point_ligue_1.text,"html.parser")
    tableau_point_ligue_1=response_point_ligue_1.find_all(class_="classement__highlight")

    first_serie_a=requests.get(Serie_A)
    response_first_serie_a=BeautifulSoup(first_serie_a.text,"html.parser")
    tableau_serie_a=response_first_serie_a.find_all(class_="classement__team")
    point_serie_a=requests.get(Serie_A)
    response_point_serie_a=BeautifulSoup(point_serie_a.text,"html.parser")
    tableau_point_serie_a=response_point_serie_a.find_all(class_="classement__highlight")

    print("")
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

    print("")
    print("Le premier de Premier League est :", tableau_premier_league[1].text.lstrip().rstrip(),"avec " , tableau_point_premier_league[1].text, "Points.")    
    print("")
    print("Le deuxième de Premier League est :", tableau_premier_league[2].text.lstrip().rstrip(),"avec " , tableau_point_premier_league[2].text, "Points.") 
    print("")  
    print("Le troisième de Premier League est :", tableau_premier_league[3].text.lstrip().rstrip(),"avec " , tableau_point_premier_league[3].text, "Points.")
    print("")  
    print("Le quatrième de Premier League est :", tableau_premier_league[4].text.lstrip().rstrip(),"avec " , tableau_point_premier_league[4].text, "Points.")
    print("")   
    print("Le cinquième de Premier League est :", tableau_premier_league[5].text.lstrip().rstrip(),"avec " , tableau_point_premier_league[5].text, "Points.")
    print("")

    print("")
    print("Le premier de Liga est :", tableau_liga[1].text.lstrip().rstrip(),"avec " , tableau_point_liga[1].text, "Points.")    
    print("")
    print("Le deuxième de Liga est :", tableau_liga[2].text.lstrip().rstrip(),"avec " , tableau_point_liga[2].text, "Points.") 
    print("")  
    print("Le troisième de Liga est :", tableau_liga[3].text.lstrip().rstrip(),"avec " , tableau_point_liga[3].text, "Points.")
    print("")  
    print("Le quatrième de Liga est :", tableau_liga[4].text.lstrip().rstrip(),"avec " , tableau_point_liga[4].text, "Points.")
    print("")   
    print("Le cinquième de Liga est :", tableau_liga[5].text.lstrip().rstrip(),"avec " , tableau_point_liga[5].text, "Points.")
    print("")

    print("")
    print("Le premier de Ligue 1 est :", tableau_ligue_1[1].text.lstrip().rstrip(),"avec " , tableau_point_ligue_1[1].text, "Points.")    
    print("")
    print("Le deuxième de Ligue 1 est :", tableau_ligue_1[2].text.lstrip().rstrip(),"avec " , tableau_point_ligue_1[2].text, "Points.") 
    print("")  
    print("Le troisième de Ligue 1 est :", tableau_ligue_1[3].text.lstrip().rstrip(),"avec " , tableau_point_ligue_1[3].text, "Points.")
    print("")  
    print("Le quatrième de Ligue 1 est :", tableau_ligue_1[4].text.lstrip().rstrip(),"avec " , tableau_point_ligue_1[4].text, "Points.")
    print("")   
    print("Le cinquième de Ligue 1 est :", tableau_ligue_1[5].text.lstrip().rstrip(),"avec " , tableau_point_ligue_1[5].text, "Points.")
    print("")

    print("")
    print("Le premier de Serie A est :", tableau_serie_a[1].text.lstrip().rstrip(),"avec " , tableau_point_serie_a[1].text, "Points.")    
    print("")
    print("Le deuxième de Serie A est :", tableau_serie_a[2].text.lstrip().rstrip(),"avec " , tableau_point_serie_a[2].text, "Points.") 
    print("")  
    print("Le troisième de Serie A est :", tableau_serie_a[3].text.lstrip().rstrip(),"avec " , tableau_point_serie_a[3].text, "Points.")
    print("")  
    print("Le quatrième de Serie A est :", tableau_serie_a[4].text.lstrip().rstrip(),"avec " , tableau_point_serie_a[4].text, "Points.")
    print("")   
    print("Le cinquième de Serie A est :", tableau_serie_a[5].text.lstrip().rstrip(),"avec " , tableau_point_serie_a[5].text, "Points.")
    print("")
    
