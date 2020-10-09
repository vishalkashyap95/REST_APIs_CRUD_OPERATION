from bson.objectid import ObjectId
from flask import request, jsonify, json, Response

from CommonUtilities import *


class CrudOperations:

    # Creating object of CommonUtilities class
    commonUtils = CommonUtilities()

    product_collection = None

    """
    Read the values from property files and store it to the respective variables
    """
    sDbName = commonUtils.getDbDetails('DB_DETAILS', 'db.name')
    sDbUsername = commonUtils.getDbDetails('DB_DETAILS', 'db.username')
    sDbPassword = commonUtils.getDbDetails('DB_DETAILS', 'db.password')
    sCollectionName = commonUtils.getDbDetails('DB_DETAILS', 'db.collection.name')


    """
    This piece of code will run when the Object of the class is created. 
    If no errors in reading values from Properties file then connect to the Mongo DB cloud else set the variable value 
    "product_collection" to None.
    On successfull connection to Mongo DB cloud, we get the collection Object in return
    """
    if (sDbName is not None) and (sDbUsername is not None) and (sDbPassword is not None) and (
            sCollectionName is not None):
        sConnectionString = "mongodb://{0}:{1}@productcluster-shard-00-00.jcvab.mongodb.net:27017," \
                            "productcluster-shard-00-01.jcvab.mongodb.net:27017," \
                            "productcluster-shard-00-02.jcvab.mongodb.net:27017/" \
                            "{2}?ssl=true&replicaSet=atlas-14aexf-shard-0&authSource=admin" \
                            "&retryWrites=true&w=majority".format(sDbUsername, sDbPassword, sDbName)
        connectMongoDbCloud = commonUtils.connectMongoDbCloud(sConnectionString=sConnectionString, sDbName=sDbName,
                                                              sCollectionName=sCollectionName)
        if connectMongoDbCloud is not None:
            product_collection = connectMongoDbCloud
        else:
            product_collection = None
    else:
        product_collection = None
        print("FAILED to read the configuration data.")

    def getAllProducts(self):
        """
        This method is used to get all the documents from the connected product_collection object.
        :return: After getting documents from collection, It returns the entire document in json format.
        """
        if request.method == 'GET':
            if self.product_collection is not None:
                all_docs = self.product_collection.find({})
                if all_docs.count() > 0:
                    # print("Inside doc", self.product_collection.count_documents({}))
                    return Response(json.dumps(list(all_docs), default=str), mimetype="application/json"), 200
                else:
                    return jsonify(success="false", message="No data found"), 404
            else:
                return jsonify(success="false", message="Unable to connect mongo DB :("), 500
        else:
            return jsonify(success="false", message="Method not allowed."), 405

    def insertProduct(self):
        """
        This method helps in inserting the data into the database
        :return: Returns id of newly created object
        """
        if request.method == 'POST':
            if self.product_collection is not None:
                _id = ObjectId()
                try:
                    new_product = {
                        "_id": _id,
                        "brand_name": request.json['brand_name'],
                        "classification_l1": request.json['classification_l1'],
                        "classification_l2": request.json['classification_l2'],
                        "classification_l3": request.json['classification_l3'],
                        "classification_l4": request.json['classification_l4'],
                        "currency": request.json['currency'],
                        "image_url": request.json['image_url'],
                        "name": request.json['name'],
                        "offer_price_value": int(request.json['offer_price_value']),
                        "regular_price_value": int(request.json['regular_price_value'])
                    }
                    # print(new_product)
                    self.product_collection.insert_one(new_product)
                    return jsonify(success=True, message="Successfully inserted with id :" + str(_id)), 201
                except:
                    return jsonify(success="false", message="Someting went wrong."), 500
            else:
                return jsonify(success="false", message="Unable to connect mongo DB :("), 500
        else:
            return jsonify(success="false", message="Method not allowed."), 405

    def operationOnSpecificProduct(self, idProduct):
        """
        This method just calls respective method based on the requested method
        :param idProduct: ID of the product on which we need to manipulate
        :return: Incase of GET method - It return the object of specified ID, Incase of PUT and DELETE method - Just return success if manipulated successfully
        """
        if request.method == 'GET':
            return self.getSingleProduct(idProduct)
        elif request.method == 'PUT':
            return self.updateSingleProduct(idProduct)
        elif request.method == 'DELETE':
            return self.deleteSingleProduct(idProduct)
        else:
            return jsonify(success="false", message="Method not allowed."), 405

    def getSingleProduct(self, idProduct):
        """
        This method find the product in the DB by id
        :param idProduct: ID of the product for which we need to send the detail of
        :return: return object of specified ID if found else No data found
        """
        try:
            sProduct = self.product_collection.find({"_id": ObjectId(idProduct)})
            if sProduct.count() > 0:
                return Response(json.dumps(list(sProduct), default=str), mimetype="application/json"), 200
            else:
                return jsonify(success="false", message="No data found")
        except:
            return jsonify(success="false", message="Something went wrong."), 500

    def updateSingleProduct(self, idProduct):
        """
        This method is used to update all the fields of particular object, first it finds the object in the DB
        if found then it updates it else No data found
        :param idProduct: id of the product on which we need to manipulate
        :return: returns success json if updated successfull else "Something went wrong" 500
        """
        try:
            sProduct = self.product_collection.find({"_id": ObjectId(idProduct)})
            if sProduct.count() == 1:
                self.product_collection.update({"_id": ObjectId(idProduct)}, {"$set": {
                    "brand_name": request.json['brand_name'],
                    "classification_l1": request.json['classification_l1'],
                    "classification_l2": request.json['classification_l2'],
                    "classification_l3": request.json['classification_l3'],
                    "classification_l4": request.json['classification_l4'],
                    "currency": request.json['currency'],
                    "image_url": request.json['image_url'],
                    "name": request.json['name'],
                    "offer_price_value": int(request.json['offer_price_value']),
                    "regular_price_value": int(request.json['regular_price_value'])
                }})
                return jsonify(success=True, message="Successfully updated."), 200
            else:
                return jsonify(success="false", message="No data found."), 404
        except:
            return jsonify(success="false", message="Something went wrong."), 500

    def deleteSingleProduct(self, idProduct):
        """
        This method is used to delete entire object from DB. First it will find the object in DB by ID
        if found then delete it else return No data found.
        :param idProduct: id of the product which we want to delete
        :return: return success json if deleted successfully.
        """
        try:
            sProduct = self.product_collection.find({"_id": ObjectId(idProduct)})
            if sProduct.count() == 1:
                self.product_collection.delete_one({"_id": ObjectId(idProduct)})
                return jsonify(success=True, message="Successfully deleted."), 200
            else:
                return jsonify(success="false", message="No data found."), 404
        except:
            return jsonify(success="false", message="Something went wrong."), 500
