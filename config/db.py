from pymongo import MongoClient

#ver de dejar en un archivo .env 
#tuve conflictos por que el ambiente virtualizado lo llame .env
from env import URL_MONGO 

#import os
#from dotenv import load_dotenv
#load_dotenv()

#urlConnectionMongo = os.getenv('URL_MONGO')

client = MongoClient(URL_MONGO)

db = client.chatBoot

collection_name = db["temas"]