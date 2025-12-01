from dask import delayed,compute

@delayed
def add(a,b):
    print("add function called.")
    return a+b;


result1 = add(1,2);
result2 = add(3,4);
result3 = compute(result1,result2)
print(result3)  # result as tuple 