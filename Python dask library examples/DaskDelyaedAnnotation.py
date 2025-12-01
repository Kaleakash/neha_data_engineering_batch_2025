from dask import delayed

@delayed
def add(a,b):
    print("add function called.")
    return a+b;


result1 = add(1,2);
print(result1.compute())