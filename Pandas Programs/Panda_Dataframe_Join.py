import pandas as pd;
employees = [
    {"id":100,"name":"Ravi","age":21,"dept_id":100},
    {"id":101,"name":"Ramesh","age":22,"dept_id":101},
    {"id":102,"name":"Rajesh","age":23,"dept_id":104}
]
department = [
    {"dept_id":100,"dept_name":"IT"},
    {"dept_id":101,"dept_name":"Non-IT"},
    {"dept_id":103,"dept_name":"Marketing"}
]
emp_df = pd.DataFrame(employees)
dept_df = pd.DataFrame(department)
inner_join_result = pd.merge(emp_df,dept_df,on="dept_id",how="inner")
print(inner_join_result)
print("--------------------")
left_outer_join_result = pd.merge(emp_df,dept_df,on="dept_id",how="left")
print(left_outer_join_result)
print("--------------------")
right_outer_join_result = pd.merge(emp_df,dept_df,on="dept_id",how="right")
print(right_outer_join_result)
print("--------------------")
full_outer_join_result = pd.merge(emp_df,dept_df,on="dept_id",how="outer")
print(full_outer_join_result)