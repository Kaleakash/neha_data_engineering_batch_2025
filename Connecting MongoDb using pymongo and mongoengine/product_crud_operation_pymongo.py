from pymongo import MongoClient
# it connect database locally, connect db in database and return collection 
def get_db_collection():
    client = MongoClient("mongodb://localhost:27017")  # connection mongo db locally 
    db = client["neha_db"];     # database name is neha_db
    return db["product"]        # collection name is product 


# insert document in product collection 
def insert_document(p_id,p_name,p_price):
    collection = get_db_collection();
    product = {"_id":p_id,"pname":p_name,"price":p_price}
    try:
        collection.insert_one(product);
        print("Product document inserted")
    except Exception as error:
        print("Error generated ",error)


#insert_document(101,"Computer",32000);


# retrieve document from collection  
def find_document():
    collection = get_db_collection();
    try:
        products = collection.find();       
        print("All Product details are ")
        for product in products:
            print(product)
    except Exception as error:
        print("Error generated ",error)

#find_document();

# update product price 

# insert document in product collection 
def update_document(p_id,new_price):
    collection = get_db_collection();
    try:
        result = collection.update_one(
            {"_id":p_id},
            {"$set":{"price":new_price}}
        );

        if result.modified_count > 0:
            print("document updated successfully")
        else:
            print("document didn't update")
    except Exception as error:
        print("Error generated ",error)

#update_document(100,48000);

# insert document in product collection 
def delete_document(p_id):
    collection = get_db_collection();
    try:
        result = collection.delete_one({"_id":p_id})

        if result.deleted_count > 0:
            print("document deleted successfully")
        else:
            print("document not present")
    except Exception as error:
        print("Error generated ",error)
#delete_document(100);

# search document using _id property 

def find_document_by_id(p_id):
    collection = get_db_collection();
    try:
        product = collection.find_one({"_id":p_id})       
        if product==None:
            print("Product not present")
        else:
            print(product)
    except Exception as error:
        print("Error generated ",error)

find_document_by_id(101)