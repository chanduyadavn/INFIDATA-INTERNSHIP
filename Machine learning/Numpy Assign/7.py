import numpy as np

# Creating a 3x4 array with random numbers between 1 and 10
random_array = np.random.randint(1, 11, size=(3, 4))
print(random_array)

four_by_five=np.array([[ 1,  2,  3,  4,  5],
                       [ 6,  7,  8,  9, 10],
                       [11, 12, 13, 14, 15],
                       [16, 17, 18, 19, 20]])

print(four_by_five[2,3])

