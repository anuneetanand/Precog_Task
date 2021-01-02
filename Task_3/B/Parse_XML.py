# Anuneet Anand
# 2018022
# Parse Stack Overflow XML Data

import os
import pymongo
import xml.parsers.expat as tool

client = pymongo.MongoClient('localhost', 27017)
db = client.StackOverflow
Files = os.listdir("StackOverflow")

for name in Files:

	col = db[name[:-4]]
	
	def action(name, data):
		if 'Id' in data: data['_id'] = data.pop('Id')
		col.insert_one(data)

	P = tool.ParserCreate()
	P.StartElementHandler = action
	
	with open("StackOverflow/"+name,"rb") as file:
		P.ParseFile(file)
	file.close()

# END OF CODE





