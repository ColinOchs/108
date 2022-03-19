import json
from flask import Flask, abort
from mock_data import catalog



app = Flask("Server")


@app.route("/")
def home():
    return "Hey, Hey! Let's play with my Python"

@app.route("/me")
def about_me():
    return "Colin Ochs"

###################################################################
#################      API Endpoints      #########################
######################   Return JSON  ############################
###################################################################



@app.route("/api/catalog", methods=["get"])
def get_catalog():
    return json.dumps(catalog)

@app.route("/api/catalog", methods=["post"])
def save_product():
    pass

# /api/catalog/count  ->  how many products exist in the catalog

@app.route("/api/catalog/count")
def product_count():
    count = len(catalog)
    return json.dumps(count)

# /api/catalog/total  ->  total of products in the catalog

@app.route("/api/catalog/total")
def catalog_total():
    total = 0
    for prod in catalog:
        total+=prod["price"]
    return json.dumps(total)

# get /api/product/wasdfalglkj3456g

@app.route("/api/product/<id>")
def get_by_id(id):
    #find the product with _id is equal to id
    
    for prod in catalog:
        if prod["_id"]==id:
            return json.dumps(prod)
        ## if not found return 404 
    return abort(404, "no such product can be located")


app.run(debug=True)