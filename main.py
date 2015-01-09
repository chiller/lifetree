#start 16:05
from db import SchemaDB
import datetime
import sys
today = datetime.date.today
#TODO: rewrite this in fp

data = SchemaDB("data.db")

trees = ["lifetree","coursera","euler"]

def xp():
    return sum(map(lambda x:x['minutes'], filter(lambda x: x['action'] in trees,data.get())))

def level():
    xpamt = xp()
    level = int((xpamt/100.0)**0.5) + 1
    lower = (level - 1) ** 2 * 100
    upper = (level) ** 2 * 100
    pct = int((xpamt - lower)*1.0 / (upper - lower) * 10)
    print "Level", level, "Xp",xpamt
    print lower, "*"*pct+'.'*(10-pct) ,upper
