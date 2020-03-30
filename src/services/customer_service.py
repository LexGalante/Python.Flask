from __main__ import mongo


def get_all_customers():
    return mongo.db.customers.find()


def filter_customer():
    return mongo.db.customers.find()
