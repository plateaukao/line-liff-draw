from pymongo import MongoClient, DESCENDING
import os
import re

mongodb_path = os.environ['MONGODB_URI'],

client = MongoClient(mongodb_path)

image_collection = client.heroku_lz4vbbdx.images
user_collection = client.heroku_lz4vbbdx.users

def upsertUser(userId, displayName, thumbnail):
    key = {'_id':userId}
    data = {'displayName':displayName, 'thumbnail':thumbnail}
    user_collection.update(key, data, upsert=True)

def addImage(userId, imageId, url, thumbnail, isPublic = False):
    record = {'userId':userId,'imageId':imageId, 'url':url,'thumbnail':thumbnail, 'isPublic':isPublic}
    image_collection.insert_one(record)

def deleteImage(userId, imageId):
    query = {'userId':userId,'imageId':imageId}
    image_collection.delete_one(query)

def findImagesWithUserId(userId):
    return image_collection.find({'userId': userId}).sort('_id',DESCENDING)
