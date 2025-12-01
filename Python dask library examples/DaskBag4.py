import dask.bag as db
import dask.array as da;
import dask.dataframe as dd;

emp = [
    {id:1,"name":"Raj","salary":45000,"city":"Bangalore"},
    {id:2,"name":"Ravi","salary":43000,"city":"Mumbai"},
    {id:3,"name":"Ramu","salary":48000,"city":"Mumbai"},
    {id:4,"name":"Ramesh","salary":49000,"city":"Bangalore"}
]
def doTask():
    b = db.from_sequence(emp)
    result = b.groupby("city").compute();
    print(result)

#doTask();
if __name__=="__main__":
    doTask();