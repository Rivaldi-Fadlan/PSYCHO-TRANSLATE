import gridfs
from pymongo import MongoClient


URL = "mongodb://fadlann:psycho@localhost:27017"
client = MongoClient(URL)
# inggris
db = client["translate"]
fs = gridfs.GridFS(db)



# indonesia
dbi = client["indonesia"]
fsi = gridfs.GridFS(dbi)




