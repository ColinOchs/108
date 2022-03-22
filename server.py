import json
from flask import Flask, abort
from mock_data import catalog



app = Flask("Server")


@app.route("/")
def home():
    return "Greetings, welcome to the website "

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



# Get /api/product/cheapest
# should return product with lowest price
# if the price of your prod is lower than the price of your solution variable
#     set your solutions variable equal to your prod

# return solution

@app.route("/api/product/cheapest")
def cheapest_product():
    solution = catalog[0]
    for prod in catalog:
        if prod["price"] < solution["price"]: 
            solution=prod
    return json.dumps(solution)


#create a variable(solution) with on of the elements from the list
# create a for loop to travel catalog
@app.get("/api/categories")
def unique_categories():
    categories = []
    for prod in catalog:
        cat = prod["category"]
        if not cat in categories:
            categories.append(cat)
    return json.dumps(categories)


# Ticket 2345
# Create and endpoint that allow the client to get all the products
# for an specified category 
#\
@app.get("/api/catalog/<category>")
def prods_by_category(category):
    result = []
    for prod in catalog:
        if prod["category"] == category:
            result.append(prod)

    return json.dumps(result)




app.run(debug=True)