import pandas as pd
data = {
    "Name":["Raj","Seeta","John","Steven","Mahesh",None],
    "Age":[34,44,23,None,46,35],
    "Department":["IT","Non-IT",None,"IT","Marketing","Non-IT"],
    "Salary":[43000,45000,34000,56000,32000,28000]
}
#print(data)
df = pd.DataFrame(data);
# print(df)
# # Adding new column with some maths operation 
# df["Bonus"]=df["Salary"]*0.10
# print("---------------------------------------------")
# print(df)
# # in existing column do some maths operation 
# df["Salary"]=df["Salary"]*0.15;
# print("---------------------------------------------")
# print(df)
# print("---------------------------------------------")
# print(df.info())
# print("---------------------------------------------")
# # display specific column 
# print("Display only name")
# print(df['Name'])
# print("Display Name and Age")
# print(df[['Name',"Age"]])
# filter the data 
# IT_department_filter = df[df["Department"]=='Non-IT']
# print(IT_department_filter)
# print("--------------------------------------------")
# High_Salary_Employee = df[df["Salary"]>35000];
# print(High_Salary_Employee)
# print("---------------------------------")
# print(df.dropna())
# print("---------------------------------")
# #print(df.fillna(0))
# print("---------------------------------")
# #group by department
# group_by_department_sum = df.groupby("Department")["Salary"].sum();
# print("Sum")
# print(group_by_department_sum)
# print("---------------------------------")
# group_by_department_max = df.groupby("Department")["Salary"].max()
# print("Max")
# print(group_by_department_max)
# print("---------------------------------")
# group_by_department_min = df.groupby("Department")["Salary"].min()
# print("Min")
# print(group_by_department_min)
# print("---------------------------------")
# print("Avg")
# group_by_department_avg = df.groupby("Department")["Salary"].mean()
# print(group_by_department_avg)

# applying some function logic return new column 
df["SalaryAfterBonus"]= df["Salary"].apply(lambda salary:salary+salary*.10);
print("------------------")
print(df) 