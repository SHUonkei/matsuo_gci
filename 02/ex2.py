import numpy as np
from numpy import random
from numpy import linalg as LA
a = [1,2,3,4,5]
b = [3]*5
a = np.array([1,2,3,4,5])
b = np.array([3,3,3,3,3])
print(a)
print(*a)
c = a*b
print(c,type(c))
d = np.r_[a,b]
print(*d)

print(d)

print(list(c),type(list(c)))


e = np.r_[a,b+100,d]
print(e)

def normalize(a):
    a = np.array(a)
    s = np.sum(a*a)
    s = s**(1/2)
    a *= s
    return a


idx = a%3

print(idx)

idx = a%3 == 0
print(idx)

def count_square(n):
    squered = np.array([range(1,20)])**2
    ans = np.array(squered <n)
    print(ans)
    answer = np.sum(ans)
    return answer

def count_square(n):
    array = np.arange(1,n) ** 2
    answer = np.sum((array < n))
    return answer

print(count_square(12))


a_list = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 1, 2, 3]]
a = np.array(a_list)

#axis0 = 縦軸　縦軸に沿ってみていく
print("-1",np.max(a_list,axis=0))
#-1 [9 6 7 8]



print("----------------")
print(a[0])
print(a[0,1])
print(a[[0,1]])
#print(a[[0,1]][0])
print("6666666666666666")
print(a[[[0,1]]])
print(a[[[[0,1]]]])
print("0000000000000000")
print(a[np.array([0,1])])
print(a[[0],[1]])
print(a[np.array([0]),np.array([1])])
print(a[[[0],[1]]])

print("-1--------------")
print(a[0])
#arrayの縦方向を守るからかっこが増える！
print(a[[0]])
print(a[[0,1]])


print(a[np.array([0])])
print(a[np.array([0,1])])

print("-2---------------")
#これが意味不明、縦方向を守って第一引数が行指定
#わかった
print(a[[0],[1]])
print(a[[0,1],[1]])

#err
#print(a[np.array([0])][np.array([1])])

print(a[[0],[1]][0])
print("-2--------------")
print(a[[0,1]])
print(a[[[0],[1]]])
print(a[[[0],[1]]][0])
print(a[[[0],[1]],0])

print("3-------------")
print(a[:, 1:2])
print(a[:,[1]])
print(a[:,np.array([1])])
#インデックスで[]リストをつかうとarrayとおなじ挙動する？
print(a[:,1])