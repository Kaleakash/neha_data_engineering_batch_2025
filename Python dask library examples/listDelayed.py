from dask import delayed

@delayed
def double(x):
    return x*2;

items = [1,2,3,4,5];
tasks = [double(t) for t in items]
#print(tasks)
print([t.compute() for t in tasks])
