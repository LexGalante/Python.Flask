from __main__ import app
from flask import Response
from bson.json_util import dumps
from services.customer_service import get_all_customers


@app.route("/customer", methods=['GET'])
def get_customers():
    customers = dumps(get_all_customers())
    return customers
