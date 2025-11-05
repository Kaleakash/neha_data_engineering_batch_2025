s1 = {""}
s2 = {1,2,3,4,5};
s3 = set();
s4 = {1,2,3,'hello', (1,2,3)};
print(type(s1))
print(type(s2))
print(type(s3)) 
print(type(s4))
print(s2)
s2.add(6)
print(s2)
s2.remove(3)
print(s2)
#s2.remove(10)  # This will raise a KeyError because 10 is not in the set
s2.discard(10)  # This will not raise an error even though 10 is not in the set
print(s2)
s5 = s2.copy();     # it creates a shallow copy of the set
print(s5)
s2.clear()
print(s2)
print(s5)
s5.pop()   # removes and returns an arbitrary element from the set
print(s5)
s5.clear()
print(s5)