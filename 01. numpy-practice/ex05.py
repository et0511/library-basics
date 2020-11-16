import numpy as np

arr1 = np.arange(10)
print(arr1.shape)

print('===== 수직축 추가 =====')

arr2 = arr1[:, np.newaxis]
print(arr2.shape)

print('===== 수평축 추가 =====')

arr3 = arr1[np.newaxis, :]
print(arr3.shape)
pairnt(arr3)
