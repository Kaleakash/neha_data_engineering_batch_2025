num1 = [];      # Empty list using literal style 
num2 = [1, 2, 3, 4, 5];
num3 = list();  # Empty list using constructor or function style 
num4 = list((1, 2, 3, 4, 5));
print(type(num1));
print(type(num2));
print(type(num3));
print(type(num4));
print(num1);
print(num2);
num2.append(6);     # append() method to add an element to the end of the list
print(num2);
num2.insert(3,100); # insert() method to add an element at a specific index
print(num2);
num2.remove(2);     # remove() method to remove the first occurrence of a specific element
print(num2);
num2.pop();        # pop() method to remove and return the last element of the list
print(num2);
num2.pop(2);     # pop() method to remove and return the element at a specific index
print(num2);
print(len(num2));  # len() function to get the number of elements in the list
print(num2[0]);    # Accessing elements using indexing