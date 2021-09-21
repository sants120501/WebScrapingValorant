import requests
from bs4 import BeautifulSoup
import re
#import csv
import pandas



def playerstats(x):
    # ACESSA A PÁGINA
    url = 'https://www.vlr.gg/{}'.format(x)
    print(url)
    series = re.findall('vlr.gg/(.+)', url)

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # ACESSA UM POR UM TODAS AS DIVS QUE SERÃO NECESSÁRIAS PARA PUXAR OS DADOS

    # Player Names And Teams
    modplayer = []
    names = []
    teams = []

    temp = soup.find_all(class_='mod-player')
    for x in temp:
        temp2 = x.find_all('a')
        modplayer.append(temp2)

    for x in modplayer:
        for y in x:
            A = y.find_all(class_='text-of')
            names.append(A[0])

    for x in modplayer:
        for y in x:
            A = y.find_all(class_='ge-text-light')
            teams.append(A[0])

    # Player Agents
    modagents = []
    agentname = []

    temp = soup.find_all(class_='mod-agents')
    modagents.append(temp)

    for x in modagents:
        for y in x:
            m = re.findall('title="(.+)"', str(y))
            agentname.append(m)

    # Player Stats
    modstat = []
    templist = []
    z = 0

    temp = soup.find_all(class_='mod-stat')
    for x in temp:
        z += 1
        temp2 = x.find_all(class_='stats-sq')
        if z % 10 == 3:
            valor = temp2[0].contents[1].contents[0]
        else:
            valor = temp2[0].contents[0].strip()
        templist.append(valor)
        if z % 10 == 0:
            modstat.append(templist)
            templist = []

    # Maps
    maps = []

    temp = soup.find_all(class_='vm-stats-gamesnav-item js-map-switch')
    for x in temp:
        maps.append(x.contents[3].contents[2].strip())

    if maps == []:
        temp = soup.find_all(class_='map')
        maps.append(temp[0].contents[1].contents[1].contents[0].strip())

    totallist = []
    print(maps)

    for temp in range(0, len(names)):
        a = names[temp].contents[0].strip()
        b = teams[temp].contents[0].strip()
        c = agentname[temp][0]
        d = modstat[temp]
        # print(d)
        d[4] = d[4].replace("+", "")
        # d[5] = d[5].replace(".", ",")
        d[6] = int(d[6].replace("%", "")) / 100
        d[9] = d[9].replace("+", "")
        if temp < 10:
            finaltemp = series + [maps[0]] + [a] + [b] + [c] + d
            totallist.append(finaltemp)
        elif temp < 20:
            dummy = 0
        elif temp < 30:
            finaltemp = series + [maps[1]] + [a] + [b] + [c] + d
            totallist.append(finaltemp)
        elif temp < 40:
            finaltemp = series + [maps[2]] + [a] + [b] + [c] + d
            totallist.append(finaltemp)
        elif temp < 50:
            finaltemp = series + [maps[3]] + [a] + [b] + [c] + d
            totallist.append(finaltemp)
        elif temp < 60:
            finaltemp = series + [maps[4]] + [a] + [b] + [c] + d
            totallist.append(finaltemp)

    csvlist = totallist

    # CSV

    return csvlist




#print(soup.prettify())

