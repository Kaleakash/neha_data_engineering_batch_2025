import pandas as pd;
df = pd.read_csv("employees.csv")
#print(df)
# first_name_field = df["FIRST_NAME"]
# print(first_name_field)
# first_name_and_salary = df[["FIRST_NAME","SALARY"]]
# print(first_name_and_salary)
# high_salary = df[df["SALARY"]>=13000]
# print(high_salary)

#new_employee = {"EMPLOYEE_ID":207,"FIRST_NAME":"Raj","LAST_NAME":"Deep","SALARY":19000};
#data = df.append(new_employee,ignore_index=True)       # Error
# update salary like where clause 

# df.loc[df["FIRST_NAME"]=="Steven","SALARY"]=25000
# print(df) 

# delete data frame records 
# df = df[df["EMPLOYEE_ID"]!=100];
# print(df)

# df = df[df["JOB_ID"]!='ST_CLERK'];
# print(df)

# sort the employee information using salary 
# sorted_employee_asc_by_salary = df.sort_values(by="SALARY",ascending=True);
# print(sorted_employee_asc_by_salary)
# print("--------------------")
# sorted_employee_desc_by_salary = df.sort_values(by="SALARY",ascending=False);
# print(sorted_employee_desc_by_salary)


# stored filter or manipulated data in file 
#df = df[df["JOB_ID"]!='ST_CLERK'];
#print(df)
#df.to_csv("non_st_clerk_employee.csv",index=False);

# group by department_id wise sum salary 
# sum_salary_department_id_wise = df.groupby("DEPARTMENT_ID")["SALARY"].sum();
# print(sum_salary_department_id_wise)

# aggregate_operation_on_salary_department_id_wise = df.groupby("DEPARTMENT_ID")["SALARY"].agg(["count","min","max","mean","sum"])
# #print(aggregate_operation_on_salary_department_id_wise)
# aggregate_operation_on_salary_department_id_wise.to_csv("aggregate_operation.csv",index=False);
