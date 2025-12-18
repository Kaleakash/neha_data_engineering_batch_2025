from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import relationship

DATABASE_URL = "mysql+mysqlconnector://root:root123@localhost/neha_db"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
# Trainer , tid(PK), tname(50), tech(50) etc 
class Trainer(Base):
    __tablename__ = "trainers"

    tid = Column(Integer, primary_key=True)
    name = Column(String(50))
    tech = Column(String(50))

    # ONE trainer → MANY students
    students = relationship("Student", back_populates="trainer")

    def __repr__(self):
        return f"Trainer(id={self.tid}, name={self.name})"


from sqlalchemy import Column, Integer, String, ForeignKey
# student table : sid(PK),sname (50),trainer_id(FK)
class Student(Base):
    __tablename__ = "students"

    sid = Column(Integer, primary_key=True)
    name = Column(String(50))

    trainer_id = Column(Integer, ForeignKey("trainers.tid"))

    # MANY students → ONE trainer
    trainer = relationship("Trainer", back_populates="students")

    def __repr__(self):
        return f"Student(id={self.sid}, name={self.name})"

#Base.metadata.create_all(engine)

#print("table created")


# insert few record in trainer table 
# try:
#     trainer1 = Trainer(name="Raj",tech="Java");
#     trainer2 = Trainer(name="Ravi",tech="Python");
#     trainer3 = Trainer(name="Ramu",tech="AI");
#     session.add(trainer1);
#     session.add(trainer2);
#     session.add(trainer3)
#     session.commit();
#     print("Trainer record stored successfully")
# except Exception as error:  
#     print("Error generated "+error)

# insert new student records in table 
# try:
#     student1 = Student(name="Meeta",trainer_id=1);
#     student2 = Student(name="Veeta",trainer_id=1);
#     student3 = Student(name="Keeta",trainer_id=2);
#     student4 = Student(name="Leeta",trainer_id=2);
#     student5 = Student(name="Yeeta",trainer_id=3);
#     student6 = Student(name="Reeta",trainer_id=3);
#     session.add(student1);
#     session.add(student2);
#     session.add(student3);
#     session.add(student4);
#     session.add(student5);
#     session.add(student6);
#     session.commit();
#     print("Student record stored successfully")
# except Exception as error:  
#     print("Error generated "+error)


# error in below code because no trainer with id as 4
# try:
#     student1 = Student(name="Qeeta",trainer_id=4)
#     session.add(student1);
#     session.commit();
#     print("Student record stored successfully")
# except Exception as error:  
#     print("Error generated ",error)

# through trainer retrieve trainer as well as associate student records 

# trainer = session.query(Trainer).filter(Trainer.tid==3).first()

# print("Trainer:", trainer.name)
# for s in trainer.students:
#     print("Student:", s.name, "-")


student = session.query(Student).filter(Student.sid==5).first()
print(student.name, "is a Student and Handler by ", student.trainer.name," Trainer")
    