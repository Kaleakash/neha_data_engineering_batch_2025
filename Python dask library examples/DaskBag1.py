import dask.bag as db
item = [1,2,3,4,5,6,7,8,9,10]
def doTask():
    b = db.from_sequence(item)
    print(b)
    result = b.map(lambda x:x*2).compute();
    print(result)

#doTask();
if __name__=="__main__":
    doTask();