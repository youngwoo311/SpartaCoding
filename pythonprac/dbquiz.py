from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


movie = db.movies.find_one({'title':'매트릭스'})['star']
# print(movie)

same_star = list(db.movies.find({'star':movie},{'_id':False}))

for target in same_star:
    print(target['title'])
# print(same_star)

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})

