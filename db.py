import string
import datetime
class CsvDB(object):

    def __init__(self,path):
        self.path = path

    def serialize(self, data):
        return data

    def deserialize(self, line):
        return line

    def get(self):
        with open(self.path,"r") as f:
            return map(self.deserialize, map(string.strip,f.readlines()))

    def append(self, data):
        with open(self.path,"a") as f:
            f.write(self.serialize(data)+"\n")

    def reset(self):
        with open(self.path,"w") as f:
            f.write("")


class SchemaDB(CsvDB):
    schema = ["date","action","notes","minutes"]
    
    def serialize(self, data):
        return ";".join([
            str(data["date"].toordinal()),
            data.get("action",""),
            data.get("notes",""),
            str(data.get("minutes","0"))
        ])

    def deserialize(self, line):
        data = dict(zip(self.schema, line.split(';')))
        data["date"] = datetime.date.fromordinal(int(data["date"]))
        data["minutes"] = int(data["minutes"])
        return data

    def pretty(self):
        data = self.get()
        for line in data: 
            print line

