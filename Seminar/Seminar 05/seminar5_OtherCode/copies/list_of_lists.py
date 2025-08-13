import copy

matrix = [[20, 19, -8], [41, 2, 5], [60, 71, 85]]
matrix_b = matrix
shallow_copy = copy.copy(matrix)
deep_copy = copy.deepcopy(matrix)

print('ID matrix:', id(matrix))
print('ID matrix_b (obtinuta prin assignment):', id(matrix_b))

print('ID shallow copy:', id(shallow_copy))
print('ID deep copy:', id(deep_copy))

print("id(matrix[0]) == id(shallow_copy[0])")
print(id(matrix[0]) == id(shallow_copy[0]))
print("id(matrix[0]) == id(deep_copy[0])")
print(id(matrix[0]) == id(deep_copy[0]))

print("Setting matrix[1][1] to 555.")
matrix[1][1] = 555

print('Initial matrix:', matrix)
print('Shallow copy:', shallow_copy)
print('Deep copy:', deep_copy)

print('-----' * 20)
print("Setting shallow_copy[0][1] to -99.")

shallow_copy[0][1] = -99
print('Initial matrix:', matrix)
print('Shallow copy:', shallow_copy)
print('Deep copy:', deep_copy)
print('-----' * 20)

# print("Setting shallow_copy[0] to 1.")
# shallow_copy[0] = 1
# print('Initial matrix:', matrix)
# print('Shallow copy:', shallow_copy)
# print('Deep copy:', deep_copy)
