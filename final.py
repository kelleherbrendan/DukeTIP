from numpy import *

movieNames = loadtxt("./finalData/2014-15/1-premierleague.conf", dtype={
    'names': ('id', 'name'),
    'formats': ('int', 'S128')}, delimiter="|", usecols=(0, 1))
movieDict = dict(zip(movieNames['id'], movieNames['name']))
movieData = loadtxt("./movieData/u.data", dtype={
    'names': ('user', 'movie', 'rating'),
    'formats': ('int', 'int', 'int')}, usecols=(0, 1, 2))