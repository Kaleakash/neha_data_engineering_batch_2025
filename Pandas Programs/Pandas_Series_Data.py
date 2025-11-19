import pandas as pd
# list = [100,200,300,400,500,600]
# listIndex = ["A","B","C","D","E","F"]
# s = pd.Series(list);
# s1 = pd.Series(list,listIndex)
# print(list)
# print(s)
# print(s1)

# converting Pandas serries for dictionary 
# data = {"id":100,"name":"Ravi","age":21};
# s = pd.Series(data);
# print(s)
# print(s["id"],s["name"],s["age"])

# converting list to pandas and apply filter 
s = pd.Series(range(100,150));
#print(s)
#print(s>120)       #return True or False 
#print(s[s>120])    #display those value > 120
#print(s[s%2==0])    # display only even number 
print(s[s%2!=0])    # display only odd number 
