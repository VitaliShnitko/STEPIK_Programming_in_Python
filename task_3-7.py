'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.
'''

n = int(input())
teams = {}
for i in range(n):
    team1, goal1, team2, goal2 = input().split(';')

    if team1 not in teams:
        teams[team1] = {'plays': 0, 'wins': 0, 'draws': 0, 'loses': 0, 'score': 0}

    if team2 not in teams:
        teams[team2] = {'plays': 0, 'wins': 0, 'draws': 0, 'loses': 0, 'score': 0}

    if goal1 > goal2:  # team1 wins
        teams[team1]['wins'] += 1
        teams[team1]['score'] += 3

        teams[team2]['loses'] += 1
        teams[team2]['score'] += 0

    elif goal2 > goal1:  # team2 wins
        teams[team1]['loses'] += 1
        teams[team1]['score'] += 0

        teams[team2]['wins'] += 1
        teams[team2]['score'] += 3

    elif goal1 == goal2:  # draw
        teams[team1]['draws'] += 1
        teams[team1]['score'] += 1

        teams[team2]['draws'] += 1
        teams[team2]['score'] += 1

    teams[team1]['plays'] += 1
    teams[team2]['plays'] += 1

for team in teams:
    values_order = ['plays', 'wins', 'draws', 'loses', 'score']
    print("{}:{}".format(str(team), ' '.join([str(teams[team][key]) for key in values_order])))
