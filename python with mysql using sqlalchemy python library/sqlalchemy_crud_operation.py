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
        return f"<Product(pid={self.pid}), PName={self.pname}and Price={self.price}/>"
    
def get_session():
    engine = create_engine("mysql+pymysql://root:root123@localhost:3306/neha_db",echo=False)
    Session = sessionmaker(bind=engine)
    return Session();

def create_tables():
    engine = create_engine("mysql+pymysql://root:root123@localhost:3306/neha_db",echo=False)
    Base.metadata.create_all(engine);
    print("Table created successfully")



if __name__ == "__main__":
    #insert_record(3,"Pen Drive",1500)
    pass