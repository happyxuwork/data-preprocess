# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''

# a = [2,4,6,8,20,30,40]
# print(a[::2])
# print(a[-2:])

# list1 = [3,6,8,4,9,5,6]
# list2 = [5,6,10,17,11,2]
# list3 = list1+list2
# print(sorted(list(set(list3))))

# def test(a,b,*args):
#     print(a)
#     print(b)
#     print(args)
# test(11,22,33,44,55,66,77,88,99)

func = lambda x : x % 2
result = filter(func,[1,2,3,4,5])
print(list(result))