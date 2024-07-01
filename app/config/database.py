from mongoengine import connect

def initialize_db(app):
    connect('crudpy', host='localhost', port=27017)
