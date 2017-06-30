from numpy import *
from sys import stdout


def separate(fileInput, fileOutput, version):
    # import printing system
    from sys import stdout

    # load data
    matchesOld = loadtxt(fileInput, dtype={
        'names': ['line'],
        'formats': ['S128']}, delimiter="\\")

    # decode
    matches = []
    for a in range(len(matchesOld)):
        matches.append(matchesOld[a]['line'].decode('utf-8'))

    # adding data to 2D array
    matches2D = []
    for a in range(len(matches)):
        matches2D.append([])
        for b in range(4):
            if b == 0 or b == 2:
                matches2D[a].append('')
            if b == 1 or b == 3:
                matches2D[a].append(int(0))

    # separating match data (version: 0 is no white space before data, 1 has white space before data)
    if version == 0:
        for a in range(len(matches)):
            phase = 1
            if not matches[a][0:8] == 'Matchday' and not matches[a][0] == '[':
                for b in range(len(matches[a])):
                    if phase == 1:
                        if str(matches[a][b]) == ' ' and str(matches[a][b + 1]) == ' ':
                            phase = 2
                            continue
                        else:
                            matches2D[a][0] += matches[a][b]
                    if phase == 2:
                        if not str(matches[a][b]) == ' ':
                            matches2D[a][1] = matches[a][b]
                            phase = 3
                            continue
                    if phase == 3:
                        if not str(matches[a][b]) == '-':
                            matches2D[a][3] = matches[a][b]
                            phase = 4
                            continue
                    if phase == 4 and not str(matches[a][b + 1]) == ' ':
                        phase = 5
                        continue
                    if phase == 5:
                        if str(matches[a][b]) == ' ' and str(matches[a][b + 1]) == ' ':
                            break
                        else:
                            matches2D[a][2] += matches[a][b]
    if version == 1:
        for a in range(len(matches)):
            phase = 0
            if not matches[a][0:8] == 'Matchday' and not matches[a][0] == '[':
                for b in range(len(matches[a])):
                    if phase == 0 and not str(matches[a][b + 1]) == ' ':
                        phase = 1
                        continue
                    if phase == 1:
                        if str(matches[a][b]) == ' ' and str(matches[a][b + 1]) == ' ':
                            phase = 2
                            continue
                        else:
                            matches2D[a][0] += matches[a][b]
                    if phase == 2:
                        if not str(matches[a][b]) == ' ':
                            matches2D[a][1] = matches[a][b]
                            phase = 3
                            continue
                    if phase == 3:
                        if not str(matches[a][b]) == '-':
                            matches2D[a][3] = matches[a][b]
                            phase = 4
                            continue
                    if phase == 4 and not str(matches[a][b + 1]) == ' ':
                        phase = 5
                        continue
                    if phase == 5:
                        if b + 1 == len(matches[a]):
                            matches2D[a][2] += matches[a][b]
                            break
                        if str(matches[a][b]) == ' ' and str(matches[a][b + 1]) == ' ':
                            break
                        else:
                            matches2D[a][2] += matches[a][b]

    # remove space at end
    for a in range(len(matches2D)):
        if not matches2D[a][0] == '':
            if matches2D[a][0][len(matches2D[a][0])-1] == ' ':
                matches2D[a][0] = matches2D[a][0][0:len(matches2D[a][0])-1]
        if not matches2D[a][2] == '':
            if matches2D[a][2][len(matches2D[a][2]) - 1] == ' ':
                matches2D[a][2] = matches2D[a][2][0:len(matches2D[a][2]) - 1]

    # write to matches.csv
    original = stdout
    f = open(fileOutput + '.csv', 'w')
    stdout = f
    f.write('Team 1,Goals 1,Team 2,Goals 2\n')
    for a in range(len(matches2D)):
        if not matches2D[a][0] == '':
            for b in range(4):
                f.write(str(matches2D[a][b]))
                if b == 3:
                    f.write('\n')
                else:
                    f.write(',')
    stdout = original
    f.close()

    # write to matches.txt
    original = stdout
    g = open(fileOutput + '.txt', 'w')
    stdout = g
    for a in range(len(matches2D)):
        if not matches2D[a][0] == '':
            for b in range(4):
                g.write(str(matches2D[a][b]))
                if b == 3:
                    g.write('\n')
                else:
                    g.write('|')
    stdout = original
    g.close()


def sortData(data):
    for a in range(len(data)):
        if data[a][0] > data[a][2]:
            temp1 = data[a][0]
            temp2 = data[a][1]
            data[a][0] = data[a][2]
            data[a][1] = data[a][3]
            data[a][2] = temp1
            data[a][3] = temp2
    return data


def matchDict(data):
    for a in range(len(data)):
        if not data[a][0] + ' vs. ' + data[a][2] in matches:
            matches[data[a][0] + ' vs. ' + data[a][2]] = []
        matches[data[a][0] + ' vs. ' + data[a][2]].append(data[a][1] - data[a][3])

# separate/parse data
separate("./finaldata/old/2013-14/matches.txt", './finaldata/new/2013-14/matches', 1)
separate("./finaldata/old/2014-15/matches.txt", './finaldata/new/2014-15/matches', 1)
separate("./finaldata/old/2015-16/matches.txt", './finaldata/new/2015-16/matches', 0)

# load data
raw_data_13 = loadtxt('./finaldata/new/2013-14/matches.txt', delimiter='|', dtype={
    'names': ('team 1', 'goals 1', 'team 2', 'goals 2'),
    'formats': ('S128', 'int', 'S128', 'int')})
raw_data_14 = loadtxt('./finaldata/new/2014-15/matches.txt', delimiter='|', dtype={
    'names': ('team 1', 'goals 1', 'team 2', 'goals 2'),
    'formats': ('S128', 'int', 'S128', 'int')})
raw_data_15 = loadtxt('./finaldata/new/2015-16/matches.txt', delimiter='|', dtype={
    'names': ('team 1', 'goals 1', 'team 2', 'goals 2'),
    'formats': ('S128', 'int', 'S128', 'int')})

# decode
data13_14 = []
data14_15 = []
data15_16 = []
for a in range(len(raw_data_13)):
    data13_14.append([raw_data_13[a]['team 1'].decode('utf-8'),
                      raw_data_13[a]['goals 1'],
                      raw_data_13[a]['team 2'].decode('utf-8'),
                      raw_data_13[a]['goals 2']
                      ]
                     )
for a in range(len(raw_data_14)):
    data14_15.append([raw_data_14[a]['team 1'].decode('utf-8'),
                      raw_data_14[a]['goals 1'],
                      raw_data_14[a]['team 2'].decode('utf-8'),
                      raw_data_14[a]['goals 2']
                      ]
                     )
for a in range(len(raw_data_15)):
    data15_16.append([raw_data_15[a]['team 1'].decode('utf-8'),
                      raw_data_15[a]['goals 1'],
                      raw_data_15[a]['team 2'].decode('utf-8'),
                      raw_data_15[a]['goals 2']
                      ]
                     )

# sort data by name
data13_14 = sortData(data13_14)
data14_15 = sortData(data14_15)
data15_16 = sortData(data15_16)

# calculate match dictionary
matches = {}
matchDict(data13_14)
matchDict(data14_15)
matchDict(data15_16)

# linear regressions for matches and error
# mae: Mean Absolute Error, mse: Mean Squared Error, rmse: Root Mean Squared Error
matchEQ = {}
eqCount = 0
mae = 0
mse = 0
for a in matches:
    if len(matches[a]) > 2:
        matchEQ[a] = poly1d(polyfit(range(len(matches[a])-1), matches[a][:-1], 1))
        mae += matchEQ[a](len(matches[a])-1) - matches[a][-1]
        mse += (matchEQ[a](len(matches[a])-1) - matches[a][-1]) ** 2
        eqCount += 1
mae /= eqCount
mse /= eqCount
rmse = mse ** 0.5

# write report
original = stdout
report = open('report.txt', 'w')
stdout = report
report.write('STATISTICS FOR SOCCER GAME CALCULATIONS\n\n')
report.write('ERROR:\n')
report.write('Mean Absolute Error: ' + str(mae) + '\n')
report.write('Mean Squared Error: ' + str(mse) + '\n')
report.write('Root Mean Squared Error: ' + str(rmse) + '\n\n')
report.write('DATA:')
for a in matches:
    report.write('\n\nMatchup: ' + a)
    for b in range(len(matches[a])):
        report.write('\nGame ' + str(b + 1) + ':\n')
        report.write('    Winner: ')
        if matches[a][b] > 0:
            report.write('Team A')
        elif matches[a][b] == 0:
            report.write('Tie')
        else:
            report.write('Team B')
        report.write('\n    Spread: ' + str(abs(matches[a][b])))
    if a in matchEQ:
        report.write('\nPredictions for final game:\n    Winner: ')
        if matchEQ[a](len(matches[a]) - 1) > 0:
            report.write('Team A')
        elif matchEQ[a](len(matches[a]) - 1) == 0:
            report.write('Tie')
        else:
            report.write('Team B')
        report.write('\n    Spread: ' + str(abs(matchEQ[a](len(matches[a]) - 1))))
stdout = original
report.close()
