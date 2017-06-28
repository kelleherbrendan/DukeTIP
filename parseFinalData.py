from numpy import *


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
                        if str(matches[a][b]) == ' ' and str(matches[a][b + 1]) == ' ':
                            break
                        else:
                            matches2D[a][2] += matches[a][b]
    # write to matches.txt
    original = stdout
    f = open(fileOutput, 'w')
    stdout = f
    for a in range(len(matches2D)):
        if not matches2D[a][0] == '':
            for b in range(4):
                f.write(str(matches2D[a][b]))
                if not b == 3:
                    f.write('|')
            f.write('\n')
    stdout = original
    f.close()

separate("./finaldata/old/2014-15/matches.txt", './finaldata/new/2014-15/matches.txt', 1)
separate("./finaldata/old/2015-16/matches.txt", './finaldata/new/2015-16/matches.txt', 0)
