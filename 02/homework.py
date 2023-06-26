# インポート
import numpy as np
import numpy.linalg as linalg
A = np.array([[3,2,1],[5,3,7],[1,1,1]])
# !!WRITE ME!!に処理を記入する（homework関数を提出することに注意）
def homework(A):
    A *= A
    ans = sum(A)**(1/2)

    return ans