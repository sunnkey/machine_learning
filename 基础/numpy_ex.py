import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))

# arr = np.array(object=(2, 4), dtype="int64")
# print(arr)

# arr = np.ones((2, 3), dtype="int32")
# print(arr)
# print(type(arr.shape))

# arr = np.array(range(1, 9))
# print(arr)
# arr.shape = (2, 2, 2)
# print(arr)
# print("*" * 20)
# print(arr[0][1])
# print(arr[1, 1, 1])

# dtype_info = {
#     'names': ['name', 'age', 'score'],
#     'formats': ['U10', 'int64', '3int'],
# }
#
# data = [
#     ('sun', 33, [99, 98, 97]),
#     ('han', 36, [79, 68, 87]),
# ]
#
# arr = np.array(data, dtype=dtype_info)
# print(arr['age'])

# arr = np.arange(1, 10).reshape(3, 3)
# print(arr[:2, :1])

# arr = np.arange(1, 101).reshape(20, 5)
# arr_x = arr[:, :-1]
# arr_y = arr[:, -1]
# print(arr[:, -1])

# 数组掩码操作
# a = np.arange(1, 11)
# mask = [True, True, False, True, False, True, True, True, False, True]
# print(a[mask])

# arr = np.arange(1, 101)
# res = arr[(arr % 10 == 0) & (arr % 12 == 0)]
# print(res)

# person = np.array(["sun", "han", "yi", "yue"])
# # mask = [0, 2, 1, 3]
# mask = [0, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
# res = person[mask]
# print(res)

import cv2

# img = cv2.imread('1.jpg', 0)
# img = cv2.resize(img, (200, 200))
# print(img)
# cv2.imshow('img', img)
#
# cv2.waitKey()
# cv2.destroyAllWindows()

# 合并：stack  拆分：split
# 垂直:vertical  水平：horizontal  深度：deep
# ary = np.arange(1, 7).reshape(2, 3)
# bry = np.arange(7, 13).reshape(2, 3)
# res = np.dstack((ary, bry))
# print(res)
# 深度方向合并后，只能再拆分为深度数组
# np.concatenate axios 0 垂直  1 水平 2 深度

ary = np.array([1, 2, 3, 4, 5])
bry = np.array([6, 7, 8, 9])

bry = np.pad(bry, pad_width=(0, 1), mode="constant", constant_values=-1)
c = np.vstack((ary, bry))
print(c)
