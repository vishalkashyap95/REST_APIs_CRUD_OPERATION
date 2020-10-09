import configparser
import random
from pymongo import MongoClient


class CommonUtilities:

    def getDbDetails(self,sPropertySection,sPropertyName):
        """
        This method is used to read the property from a properties file. This method accepts 2 parameters
        :param sPropertySection: Property section, What section in property file we need to access. Property section in the property file is define inside [](square brackets)
        :param sPropertyName: What property value we need to access
        :return: It will return value if successfully read the property else None
        """
        try:
            configFile = configparser.RawConfigParser()
            configFile.read('configFile.properties')
            return configFile.get(sPropertySection,sPropertyName)
        except:
            return None

    def connectMongoDbCloud(self,sConnectionString,sDbName,sCollectionName):
        """
        This method is used to connect to Mongo DB cloud, It accepts 3 parameters.
        :param sConnectionString: DB connection url
        :param sDbName: What Database we need to connect
        :param sCollectionName: What collection from the DB we need to access
        :return: It returns the collection object if successfully connected else None
        """
        try:
            client = MongoClient(sConnectionString)
            db = client.get_database(sDbName)
            return db[sCollectionName]
        except:
            return None


    def getRandomString(self,length):
        """
        This method generates random string with the mixture of 0-1 numbers and a-z lower letters
        :param length: what length of random string to be generated
        :return: It returns random string of specified length, Incase of exception it returns empty string
        """
        try:
            letters = "1234567890abcdefghijklmnopqrstuvwxyz"
            randomString =  ''.join(random.choice(letters) for i in range(length))
            return randomString
        except:
            return ""