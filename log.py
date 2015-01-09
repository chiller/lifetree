#start 16:05
from db import SchemaDB
import datetime
import sys
today = datetime.date.today
from main import *
def main():
    data = SchemaDB("data.db")
    if len(sys.argv)==3:
        (action, minutes) = sys.argv[1:]
        notes = ""
    elif len(sys.argv)==4:
        (action, notes, minutes) = sys.argv[1:]
    date = today()
    data.append(locals())
    level()


if __name__ == '__main__':
    main()