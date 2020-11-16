import numpy as np

print('===== 1차원 모든 요소가 0인 size 5인 배열 =====')

arr1 = np.zeros(5)
print(arr1, arr1.ndim, arr1.shape)


print('===== 2차원 모든 요소가 0인 4 x 3인 배열 =====')

arr2 = np.zeros((4, 3))
print(arr2)


print('===== 1차원 모든 요소가 1인 size 5인 배열 =====')

arr1 = np.ones(5)
print(arr1, arr1.ndim, arr1.shape)


print('===== 2차원 모든 요소가 1인 4 x 3인 배열 =====')

arr2 = np.ones((4, 3))
print(arr2)


print('===== 1차원 모든 요소가 3인 5인 배열 =====')

arr1 = np.full((5), 3)
print(arr1)


print('===== 2차원 모든 요소가 1인 4 x 3인 배열 =====')

arr2 = np.ones((4, 3))
print(arr2)

print('===== 2차원 모든 요소가 3인 4 x 3인 배열 =====')

arr2 = np.full((4, 3), 3)
print(arr2)