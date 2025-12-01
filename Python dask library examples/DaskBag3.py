import dask.bag as db
colors  = ["red","green","red","blue","white","blue","white","red"]
def doTask():
    b = db.from_sequence(colors)
    result = b.count().compute();
    print(result)

#doTask();
if __name__=="__main__":
    doTask();