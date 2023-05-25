import pandas as pd
import csv
import time
from selenium import webdriver
from bs4 import BeautifulSoup

Page_Url = "https://https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("C:\\Users\\Angel Sharma\\Desktop\\PythonProjects\\Project127")
page = requests.get(Page_Url)

def Scrape():
    header = ["Star", "Constellation", "Right_Ascension", "Declination", "Apparent_Magnitude", "Distance","Spectral_Type","Mass","Radius","Discovery_Year"]

    Dwarf_Data = []
    for i in range(0,214):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        Dwarf_Data = soup.find_all('table')
        tr_tag = Dwarf_Data[7].find_all('tr')
        for td_tag in tr_tag:
            td_tags = tr_tag.find_all("td")
            temp_list = []
            for index, TD in enumerate(td_tags):
                if index!=1:
                    try:
                        temp_list.append(TD.contents[-1].strip())
                    except :
                        temp_list.append("")
                else:
                    try:
                        temp_list.append(TD.find_all("a")[0].contents[0])
                    except:
                        temp_list.append("")
            Dwarf_Data.append(temp_list)
    with open ("Scrapper.csv", "w",encoding="utf-8") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(header)
        csv_writer.writerows(Dwarf_Data)

Scrape()