import pymongo

class MongoDBConnection:
    def __init__(self,dbName , collName , dburl , port=None , hostName=None , userName = None , passwd= None):
        self.__dbName = dbName
        self.__collName = collName
        self.__port = port
        self.__host = hostName
        self.__user_name = userName
        self.password = passwd
        self.__dbURL = dburl
        self.mydb = None
        self.mycoll = None

    def create_connection(self):
        try: 
            client = pymongo.MongoClient(self.__dbURL)  #client connection
           
            database_names = client.list_database_names()
            print(f"Available databases: {database_names}")

            if self.__dbName in database_names:
                self.mydb = client[self.__dbName]

                if self.__collName in self.mydb.list_collection_names():
                    self.mycoll = self.mydb[self.__collName]
                    print(f'connection successfull : {self.__dbName} : {self.__collName}')
                    return self.mycoll
                else:
                    raise Exception("collection not found")
            else:
                raise Exception("Database not found ")

        except Exception as e:
            print(f'exception occured while making connection{e}')
            
# dbobj = MongoDBConnection('studentData','studentCollection','mongodb://localhost', 27017,'localhost')

# print(dbobj)

# coll = dbobj.create_connection()

# print(coll)

