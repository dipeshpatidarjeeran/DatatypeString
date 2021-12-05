
x = 20 #int
y = 10 #int

name = 'ajay' #string data type
surname = 'parihar' # string
print(name+surname)    #  + concatination operator
print(name+" "+surname)
print(x+y)         # + addition operator
#print(name+x)
#we cannot concatinate a int/numeric datatype with strng


#string interpolation/substitution
a = 'ajay'
b = 'python'
# I am learning python from ajay

abc = " I am learning {} from {} "
# string.format()
print(abc.format(b,a))
# f string litertal string interpolotion
print(f"I am learnig {b} from {a} ")
# we are substituting the variables inside the string

a1 = 5
b1 = 4

#the result is 20
print(f"the result is {a1 * b1}")
print("I am learning %s from %s " %(b,a))