import numpy

A = numpy.array([[1, 2, 3], [4, 5, 6]])
B = numpy.array([[7, 8, 9], [10, 11, 12]])

print("A:", A)
print("B:", B)

print("Matrix Addition:\n", A+B)

print("Matrix Subtraction:\n", A-B)

print("Element-wise Multiplication:\n", A*B)

print("Matrix Multiplication (Dot Product):\n", numpy.dot(A,B.T))

print("Transpose of A:\n", numpy.transpose(A))
