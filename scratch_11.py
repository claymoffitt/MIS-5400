import pymongo
from pymongo import MongoClient
import os
import csv
import requests
from bs4 import BeautifulSoup

# connect to the MongoDB
connection = MongoClient('mongodb://claymoffitt:XXX@ds255403.mlab.com:55403/ncaafb')

# connect to test collection
db = connection.ncaafb.ncaafb

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

path = "/Users/cmoffitt/Library/Preferences/PyCharm2018.2/scratches"
list_of_files = {}
for filename in os.listdir(path):
    # if the element is a csv file then..
    if filename[-4:] == ".csv":
        list_of_files[filename] = path + "/" + filename
        print(list_of_files[filename])
        with open(list_of_files[filename], encoding="utf8") as f:
            csv_f = csv.reader(f)
            for i, row in enumerate(csv_f):
                if i > 5 and len(row) > 1:
                    print(row)
                    db.insert_one({'F1': row[0], 'F2': row[1]})

# find all documents
results = db.find()

print()
print('==============================')

# display documents from collection
for record in results:
    # print out the document
    print(record['F1'] + ',', record['F2'])

print()

# close the connection to MongoDB
connection.close()

# import pymongo
# from pymongo import MongoClient

# class ncaafb(object):
#     connection_params = {
#         'user': 'claymoffitt',
#         'password': 'Ohbilly!1',
#         'host': 'ds255403.mlab.com',
#         'port': 55403,
#         'namespace': 'ncaafb',
#     }
#
#     connection = MongoClient(
#         'mongodb://{user}:{password}@{host}:'
#         '{port}/{namespace}'.format(**connection_params)
#     )
#
#     db = connection.ncaafb
#
#     print(db.list_collection_names())