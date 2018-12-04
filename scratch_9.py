import requests
from bs4 import BeautifulSoup
import os
#keep track of week

urls = ['https://www.ncaa.com/scoreboard/football/fbs/2018/01/all-conf','https://www.ncaa.com/scoreboard/football/fbs/2018/02/all-conf','https://www.ncaa.com/scoreboard/football/fbs/2018/03/all-conf','https://www.ncaa.com/scoreboard/football/fbs/2018/04/all-conf','https://www.ncaa.com/scoreboard/football/fbs/2018/05/all-conf','https://www.ncaa.com/scoreboard/football/fbs/2018/06/all-conf','https://www.ncaa.com/scoreboard/football/fbs/2018/07/all-conf','https://www.ncaa.com/scoreboard/football/fbs/2018/08/all-conf','https://www.ncaa.com/scoreboard/football/fbs/2018/09/all-conf','https://www.ncaa.com/scoreboard/football/fbs/2018/10/all-conf','https://www.ncaa.com/scoreboard/football/fbs/2018/11/all-conf','https://www.ncaa.com/scoreboard/football/fbs/2018/12/all-conf','https://www.ncaa.com/scoreboard/football/fbs/2018/13/all-conf','https://www.ncaa.com/scoreboard/football/fbs/2018/14/all-conf','https://www.ncaa.com/scoreboard/football/fbs/2018/15/all-conf','https://www.ncaa.com/scoreboard/football/fbs/2018/P/all-conf'
 ]
results = {}
for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    games = soup.find_all('ul',{'class':'gamePod-game-teams'})
    for game in games:
        #game could have a week key to know when it was played
        g = {'teams':[],'scores':[]}
        # print(game)
        teams = game.find_all('li')
        for team in teams:
            g['teams'].append( team.contents[5].contents[0])
            g['scores'].append(team.contents[7].contents[0])
        for team in g['teams']:
            if team in results: #checks if the team has already had results posted
                results[team]['games'].append(g)
            else:
                results[team] = {'games': [g],'name':team}

data = open('data.csv','w')

for team in results:
    data.write(team.upper())
    data.write(': ')
    data.write(', ')
    for game in results[team]['games']:
        index  = 0 if game['teams'][0] == team else 1
        #determines current team
        opponent_index = 1 if index == 0 else 0#determines opponent
        opponent_name = game['teams'][opponent_index]#references opponents name
        my_score = game['scores'][index]
        oppoent_score = game['scores'][opponent_index]

        data.write(team)
        data.write(', ')
        data.write(my_score)
        data.write(', ')
        data.write(opponent_name)
        data.write(', ')


        data.write(oppoent_score)
        data.write(', ')
    data.write('\n')
data.close()




# ncaa_football_scores = soup.find(class_='gamePod_content-division')
# ncaa_football_scores_items = ncaa_football_scores.find_all('tr')
#
# for row in ncaa_football_scores_items:
#     for item in row:
#         if len(item.find_all(lambda tag: tag.name == 'a' or tag.name == 'span')) == 0:#no links signifies empty list
#             print(item.contents[0],end=',')
#         else:#else we have link tags and should print whats within that tag
#             print(item.find_all(lambda tag: tag.name == 'a' or tag.name == 'span')[0].contents[0],end=',')
#     # names = player_name.contents[0]
#     # print(names)
#     print()
#
# import zeep
#
# wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
# client = zeep.Client(wsdl=wsdl)
# print(client.service.Method1('Zeep', 'has been inspected'))
# print('XXX')
#

# coding: utf-8