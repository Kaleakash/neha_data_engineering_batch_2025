import mysql.connector
from mysql.connector import Error


# to get database connection 
def get_db_connection():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="neha_db"
        )
        if con.is_connected():
            print("database connected successfully")
            return con;
    except Error as e:
        print("Connection error "+e)

def insert_employee_record(id,name,salary,did):
    con = get_db_connection();
    if con is None:
        print("didn't insert")
        return     
    try:
        cursor = con.cursor();
        query = "insert into employee(id,name,salary,did) values(%s,%s,%s,%s)"
        data = (id,name,salary,did)
        cursor.execute(query,data)
        con.commit();
        print("Record inserted successfully")
    except Error as e:
        print("Error generated "+e);
    finally:
        cursor.close();
        con.close();

def insert_department_record(did,dname):
    con = get_db_connection();
    if con is None:
        print("didn't insert")
        return     
    try:
        cursor = con.cursor();
        query = "insert into department(did,dname) values(%s,%s)"
        data = (did,dname)
        cursor.execute(query,data)
        con.commit();
        print("Record inserted successfully")
    except Error as e:
        print("Error generated "+e);
    finally:
        cursor.close();
        con.close();

def delete_employee_record(id):
    con = get_db_connection();
    if con is None:
        print("Connection Error")
        return     
    try:
        cursor = con.cursor();
        query = "delete from employee where id = %s"
        cursor.execute(query,(id,))
        con.commit();

        if cursor.rowcount > 0 :
            print("Record deleted successfully")
        else:
            print("Record not present") 
    except Error as e:
        print("Error generated "+e);
    finally:
        cursor.close();
        con.close();

def update_employee_salary(id,new_salary):
    con = get_db_connection();
    if con is None:
        print("Connection Error")
        return     
    try:
        cursor = con.cursor();
        query = "update employee set salary = %s where id =  %s"
        cursor.execute(query,(new_salary,id))
        con.commit();

        if cursor.rowcount > 0 :
            print("Record update successfully")
        else:
            print("Record not present") 
    except Error as e:
        print("Error generated "+e);
    finally:
        cursor.close();
        con.close();


def find_all_employee():
    con = get_db_connection();
    if con is None:
        print("Connection Error")
        return     
    try:
        cursor = con.cursor();
        query = "select * from employee"
        cursor.execute(query);
        rows = cursor.fetchall()

        print("All Employee details are")
        for row in rows:
            #print(row)
            print("Id is ",row[0]," Name is ",row[1]," Salary is ",row[2],"DeptId",row[3])
 
    except Error as e:
        print("Error generated "+e);
    finally:
        cursor.close();
        con.close();

def find_all_employee_with_department():
    con = get_db_connection();
    if con is None:
        print("Connection Error")
        return     
    try:
        cursor = con.cursor();
        query = "select e.name,e.salary,d.dname from employee e inner join department d on e.did=d.did;"
        cursor.execute(query);
        rows = cursor.fetchall()

        print("All Employee and Department details")
        for row in rows:
            #print(row)
            print("Name is ",row[0]," Salary is ",row[1]," Department Name  is ",row[2])
 
    except Error as e:
        print("Error generated "+e);
    finally:
        cursor.close();
        con.close();

if __name__=="__main__":
    #get_db_connection();

    #insert_employee_record(5,"Teena",25000,1000);
    
    #delete_employee_record(1)

    #update_employee_salary(2,18000)

    #find_all_employee();

    #insert_department_record(102,"HR")


    find_all_employee_with_department();        # using join concept