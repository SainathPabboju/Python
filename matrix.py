R,C = (input()).split()
R = int(R)
C = int(C)
# initializing an empty matrix
matrix = []

for i in range(R):
   
   row = list(map(int, input().split()))
   
   matrix.append(row)
# printing the matrix
print("output:")
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print()
    