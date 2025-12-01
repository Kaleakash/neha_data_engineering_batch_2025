from dask import delayed

def add(a,b):
    print("add function called.")
    return a+b;

#result1 = add(100,200)
#print(result1)

# to make add function as lazy initialization 
#result2 = delayed(add)(1,2);
#print(result2.compute()) # it execute and get the result of that function 

result3 = delayed(add)(100,200);
result4 = delayed(add)(1000,2000);

result5 = delayed(add)(result3,result4)
print(result5.compute())