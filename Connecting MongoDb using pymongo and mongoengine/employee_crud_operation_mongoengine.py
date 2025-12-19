from mongoengine import connect,Document,IntField,StringField,FloatField

def db_connection():
    connect(
        db="neha_db",
        host="localhost",
        port=27017
    )

class Employee(Document):
    eid = IntField(primary_key=True)
    ename = StringField(require=True)
    esalary = FloatField(required=True)

    def __str__(self):
        return f"Employee(Employee Id ={self.eid}, Employee Name is ={self.ename}), Employee salary = {self.esalary})"
    
# create a function which store employee object in mongo db 
def create_employee(e_id,e_name,e_salary):
    db_connection();
    emp = Employee(eid=e_id,ename=e_name,esalary=e_salary)      # we convert e_id,e_name,e_salary to employee object 
    try:
        emp.save();             #       insert query 
        print("Employee object stored successfully")
    except Exception as error:
        print("Error generated ",error)

# passing employee details to store document 
#create_employee(102,"Ramu",32000)

# update document salary property using id property  
def update_employee(e_id,e_salary):
    db_connection();
    db_emp = Employee.objects(eid=e_id).first();
    try:
        if db_emp:
            db_emp.esalary = e_salary;       # update new salary 
            db_emp.save();                 # save once again with same information with updated salary 
            print("Employee record updated")
        else:
            print("Employee record not present")
    except Exception as error:
        print("Error generated ",error)

#update_employee(100,45000);

# delete document from collection  
def delete_employee(e_id):
    db_connection();
    db_emp = Employee.objects(eid=e_id).first();
    try:
        if db_emp:
            db_emp.delete();
            print("Employee record deleted")
        else:
            print("Employee record not present")
    except Exception as error:
        print("Error generated ",error)

#delete_employee(100)

# delete document from collection  
def find_all_employees():
    db_connection();
    db_employees = Employee.objects();
    try:
        print("All Employee details are ")
        for emp in db_employees:
            print(emp)
    except Exception as error:
        print("Error generated ",error)

find_all_employees();