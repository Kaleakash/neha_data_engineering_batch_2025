from dask import delayed


@delayed
def square(x):
    print('fun called..')
    return x*x;

task = square(2);
print(task)
#print(task.compute())


persistedResult = task.persist();
print(persistedResult)
print(persistedResult.compute())