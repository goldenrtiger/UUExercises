import numpy as np

#-- 1.
# Create a null vector of size 10 but the fifth value which is 1
a = np.empty(10)
a[5] = 1
print( 'a. Create a null vector of size 10 but the fifth value which is 1 \n --- ', a )

# Create a vector with values ranging from 10 to 49
b = np.arange(10, 50, 1, dtype=int)
print( 'b. Create a vector with values ranging from 10 to 49 \n --- ', b )

# Reverse a vector (first element becomes last)
c = np.linspace(0, 10, num=20)
cf = np.flip( c )
print('c. Reverse a vector (first element becomes last \n', c, '\n flip \n', cf)

# Create a 3x3 matrix with values ranging from 0 to 8
d = np.arange(0, 9, 1, dtype=int).reshape(3,3)
print( 'd. Create a 3x3 matrix with values ranging from 0 to 8 \n ---', d)

# Find indices of non-zero elements from [1,2,0,0,4,0]
e1 = np.array( [1,2,0,0,4,0] )
e2 = e1[e1!=0] # return values
e = np.nonzero( e1 )
print( 'e. Find non-zero elements from [1,2,0,0,4,0] \n --- ', e2)
print( 'e. Find indices of non-zero elements from [1,2,0,0,4,0] \n ---', e)

# Create a random vector of size 30 and find the mean value
f = np.random.randint((30))
fm = np.mean( f )
print( 'f. Create a random vector of size 30 and find the mean value \n ---', fm)

# Create a 2d array with 1 on the border and 0 inside
g = np.ones((3, 3))
g[1:-1,1:-1] = 0
print( 'g. Create a 2d array with 1 on the border and 0 inside \n ---', g )

# Create a 8x8 matrix and fill it with a checkerboard pattern
# Double colon, every yth element from the list/array
# the additional syntax of a[x::y] means get every yth element starting at position x
# >>> a = [1,2,3,4,5,6,7,8,9]
# >>> a[::3]
# [1, 4, 7]

# >>> a[2::3]
# [3, 6, 9]
i = np.zeros((8,8),dtype=int)
i[1::2, ::2] = 1
i[::2, 1::2] = 1
print('i. Create a 8x8 matrix and fill it with a checkerboard pattern \n ---', i)

# Given a 1D array, negate all elements which are between 3 and 8, in place
# Use bitwise AND to create a mask and multiply by -1
j = np.arange(11)
jj = (j > 3) & (j < 8)
j[jj] *= -1
print('j. Given a 1D array, negate all elements which are between 3 and 8, in place \n ---', j)

# Create a random vector of size 10 and sort it
k = np.random.random(10)
np.sort(k, axis=None)
print('k. Create a random vector of size 10 and sort it \n ---', k)

# l. Consider two random array A anb B, check if they are equal
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = (A==B)
print( 'l. Consider two random array A anb B, check if they are equal \n ---', equal)

# m. How to convert an integer (32 bits) array into a float (32 bits) in place?
m = np.arange(10, dtype=np.int32)
print(m.dtype)
m = m.astype(np.float32)
print('m. How to convert an integer (32 bits) array into a float (32 bits) in place? \n ---', m.dtype)

# n. How to get the diagonal of a dot product?
n1 = np.arange(9).reshape(3,3)
n2 = n1 + 1
n3 = np.dot(n1, n2)
n4 = np.diag( n3 )
print( 'How to get the diagonal of a dot product? \n --- dot product:', n3, 'diagonal:', n4 )

# a. Create a "Person" class which takes firstname and lastname as arguments to the constructor (___init___) and define a method that returns the full name of the person as a combined string.
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return '%s %s' % (self.firstname, self.lastname)

    # def getName(self):
    #     return self.name

person = Person( 'Jing', 'Xu' )
# print('persons name  \n --- ', person.getName())
print('persons name  \n --- ', person.__str__())

# b. Create a "Student" class which inherits from the "Person" class, takes the subject area as an additional argument to the constructor and define a method that prints the full name and the subject area of the student.
class Student(Person):
    def __init__(self, firstname, lastname, subject):
        super().__init__(firstname, lastname)
        self.subject = subject
    
    def __str__(self):
        return super().__str__() + 'and subject: %s ' % self.subject

    def printNameSubject(self):
        print(self.__str__())

studentA = Student('Jing', 'Xu', 'Engineering')
print('Only student firstname %s' % studentA.firstname)
print('Student name and subject: %s' % studentA.__str__())

me = Student('Benedikt', 'Daurer', 'physics')
me.printNameSubject()

# d. Create a "Teacher" class which also inherits from "Person", takes the name of the course (e.g. Python programming) as an argument and define a method that prints the full name of the teacher and the course he teaches.
class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        super().__init__(firstname, lastname)
        self.course = course

    def __str__(self):
        return '%s %s is teaching %s course.' % (self.firstname, self.lastname, self.course)
    
    def printNameCourse(self):
        print(self.__str__())

teacherA = Teacher('Filipe', 'Maia', 'Advanced Scientific Programming with Python')
teacherA.printNameCourse()



