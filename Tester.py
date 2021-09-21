from Players import playerstats
import pandas

list = []
for x in range(2000,50000):
    try:
        a = playerstats(x)
        list.append(a)
    except:
        dummy = 0


df = pandas.DataFrame(list,
                          columns=['MatchID', 'Map', 'Player', 'Team', 'Agent', 'ACS', 'Kills', 'Deaths', 'Assists',
                                   'PlusMinusKD', 'ADR', 'HS%', 'FK', 'FD', 'PlusMinusFK'])
df.to_csv('PlayersALL.csv', encoding='utf-8', index=False)