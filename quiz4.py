#norm(vector) takes a vector and returns the 2nd norm
def norm(vector):
  '''this function takes a vector as its argument. It squares each element in the vector and then sqaure roots the sum of the squares.
  '''
  total = 0 #this is before the for statement for adding purposes.
  for i in range(len(vector)):
    total += vector[i] ** 2 #takes each element of vector and squares them.
  total = total**(1/2)#takes the sqaure root of the sum found above.
  return total
#this function finds the normalized vector.
def normalize(vector):
  '''
  This function takes the vector as its argument and multiplies it by the (1/norm(vector))
  '''
  new = [] #new bracket
  for i in range(len(vector)):
    total = 0 #after for statement as adding is not involved.
    total += vector[i] * (1 / norm(vector))
    #divides the vector by the 2nd norm found above.
    new.append(total)
  return new

#this function takes the dot product of two vectors.
def dot(vector01, vector02):
  '''
  This function takes two vectors and multiplies each element together and then adds them.
  '''
  if len(vector01) != len(vector02):
    print('invalid input')
    for i in range(len(vector01)):
      if (type(vector01[i]) != int) and (type(vector01[i]) != float) and (type(vector01[i] != complex)):
        print('invalid input')
  total = 0 #before the for statement so it performs addition.
  for i in range(len(vector01)):
    total += vector01[i] * vector02[i] #multiplies each element of the vectors by each other and then adds them all together to get a scalar.
  return total
#ScaVecMulti takes a scalar and a vector and multiplies it together.
def ScaVecMulti(scalar, vector):
  '''
  this function takes a scalar and a vector as its arguments and returns the product of the two. It takes each element of the vector and multiplies it by the scalar to get the total. It then is put into the new brackets.
  '''
  new = [] #will be brackets for answer
  for i in range(len(vector)):
    total = 0
    total += vector[i] * scalar #takes each element of the vector and multiplies it by the scalar.
    new.append(total)#puts the total inside the brackets.
  return new
#VecSub takes two vectors and subtracts the first from the second.
def VecSub(vector01, vector02):
  '''
  This function takes two vectors as its arguments and subtracts each element in order and then returns a new vector.
  '''
  if len(vector01) != len(vector02):
    print('invalid input')
    return None
    for i in range(len(vector01)):
      if (type(vector01[i]) != int) and (type(vector01[i]) != float) and (type(vector01[i] != complex)):
        print('invalid input')
  new = [] #will be new brackets for answer.
  for i in range(len(vector01)):
    total = 0 #after for statement to reset.
    total += vector01[i] - vector02[i]#subtracts elements individually from vector02 from vector01.
    new.append(total) #adds the total into the brackets.
  return new

A = [[2, 1, 2], [1, -1, 1]]
#GrSc takes the Gram-Schmidt algorithm and returns Q and R.
def GrSc(A):
  '''
  this functions takes in the matrix A as the argument. It takes the functions above of norm, normalize, dot, scalarvectormultiplication and vector subtraction and returns the QR factorization.
  '''
  n = len(A) #row
  m = len(A[0]) #columns
  Q = [[0] * m for i in range(n)] #zeromatrix
  R = [[0] * n for i in range(n)] #zero matrix
  v = [[0] * m for i in range(n)] #zero matrix
  if len(A) != len(v):
    print('invalid input')
  for i in range(n):
    v[i] = A[i] #the vector[i] is the individual vectors of A.
  for i in range(n):
    R[i][i] = norm(v[i]) #takes the norm function above
    Q[i] = normalize(v[i]) #takes the normalize function above
    for j in range(i + 1, n):
      R[i][j] = dot(Q[i],v[j]) #takes the norm vector and the vectors and multiplies them together, and then adds them to make the scalar.
      temp = ScaVecMulti(R[i][j], Q[i]) #takes the dot product and the normalize vector and multiplies them together.
      v[j] = VecSub(v[j],temp) #subtracts the ScaVecMulti from the vectors.
  return [Q, R]


output = GrSc(A)
print(output[0])
print(output[1])
