from sqlalchemy import Column,Integer,String,Float,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

# create the Base of SQLAlchemy 
Base = declarative_base();

# class of type 
class Product(Base):
    __tablename__ ="product"    

    pid = Column(Integer, primary_key=True)
    pname = Column(String(25))
    price = Column(Float)

    def __init__(self,pid,pname,price):
        self.pid=pid;
        self.pname=pname;
        self.price=price
        print("object created")

    def __repr__(self):
        return f"<[Product(pid={self.pid}), PName={self.pname}, and Price={self.price}]/>"
    
def get_session():
    engine = create_engine("mysql+pymysql://root:root123@localhost:3306/neha_db",echo=False)
    Session = sessionmaker(bind=engine)
    return Session();

def create_tables():
    engine = create_engine("mysql+pymysql://root:root123@localhost:3306/neha_db",echo=False)
    Base.metadata.create_all(engine);
    print("Table created successfully")

def insert_record(p_id,p_name,p_price):
    session = get_session();
    try:
        product = Product(p_id,p_name,p_price)  # we convert those value to product object 
        session.add(product)                    # we store object in db not writing insert query 
        session.commit()
        print("Product details stored successfully")
    except Exception as error:
        session.rollback();
        print("error generated "+error)
    finally:
        session.close();

def update_product_price(p_id,new_price):
    session = get_session();
    try:
        db_product = session.query(Product).filter(Product.pid==p_id).first(); 
        if db_product:
            db_product.price=new_price; 
            session.commit();    
            print("Product updated successfully")
        else:
            print("Product not present")
    except Exception as error:
        session.rollback();
        print("error generated "+error)
    finally:
        session.close();

def delete_product(p_id):
    session = get_session();
    try:
        db_product = session.query(Product).filter(Product.pid==p_id).first(); 
        if db_product:
            session.delete(db_product);
            session.commit();    
            print("Product deleted successfully")
        else:
            print("Product not present")
    except Exception as error:
        session.rollback();
        print("error generated "+error)
    finally:
        session.close();

def find_all():
    session = get_session();
    try:
        products = session.query(Product).all();
        print("All Product details are")
        for product in products:
            print(product)
    except Exception as error:
        print("error generated "+error)
    finally:
        session.close();

if __name__ == "__main__":
    #insert_record(3,"Pen Drive",1700)
    #find_all();
    #update_product_price(1,58000)
    delete_product(1)