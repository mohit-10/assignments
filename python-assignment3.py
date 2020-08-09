
#1.1 Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()


def do_sum(x1, x2): 
    return x1 + x2


def my_reduce(operation,sequence):
	first_element = sequence[0]
	for i in sequence[1:]:
		first_element=operation(first_element,i)
	return first_element

input_list=[]

input_list = [int(item) for item in input("Enter the list items : ").split()]
print(type(input_list))
print(my_reduce(do_sum, input_list))


#1.2 Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()
def iseven(x):
	if(x%2==0):
		return True
	else:
		return False

def myfilter(anyfunc, sequence):

	result = []
	for item in sequence:
		if iseven(item):
			result.append(item)
	return result

input_list=[]

input_list = [int(item) for item in input("Enter the list items : ").split()]

print(myfilter(iseven, input_list))


#2. Implement List comprehensions to produce the following lists. Write List comprehensions to produce the following Lists


#List comprehension 1
input_list = ['x','y','z']
output1 = [ item*num for item in input_list for num in range(1,5)  ]
print((output1))

#List Comprehension 2 
input_list = ['x','y','z']
output2 = [ item*num for num in range(1,5) for item in input_list  ]
print(output2)

#List Comprehension 3

input_list = [2,3,4,5]
result = [ [item+num] for item in input_list for num in range(0,4)]
print("[2,3,4] =>" +  str(result))