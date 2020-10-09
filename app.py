from flask import Flask, request, jsonify
from CrudOperations import *

app = Flask(__name__)

# Create the object of CrudOperations Class
crudOperations = CrudOperations()


@app.route("/api/v1/products", methods=['GET'])
def getAllProducts():
    """
    Just calls the getAllProducts() method and get the documents of products from DB
    :return: return all the document if successfully read from DB
    """
    return crudOperations.getAllProducts()


@app.route("/api/v1/insertProduct", methods=['POST'])
def insertProduct():
    """
    This method calls the insertProduct() method and passes all the request body data to insertProduct() for processing.
    :return: return success json if inserted successfully
    """
    return crudOperations.insertProduct()


@app.route("/api/v1/product/<string:id>",methods=['GET','PUT','DELETE'])
def operationOnSpecificProduct(id):
    """
    This method is used to manipulat on a single object of product document.
    :param id: accepts a string parameter passed via URL
    :return: Incase of get - returns object of specified ID, Incase of PUT and DELETE - Just return success if manipulated successfully
    """
    return crudOperations.operationOnSpecificProduct(id)


if __name__ == "__main__":
    # app.run(host="0.0.0.0")
    app.run(debug=True)
