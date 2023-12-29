# 2次元累積和
# ABC228F

def get_sum(accA,i,j,h,w):
    return accA[i+h][j+w]-accA[i][j+w]-(accA[i+h][j]-accA[i][j])

def create_2d_acc(A):
    A1 =[list(accumulate(a, initial=0)) for a in A]
    A2 = list(zip(*A1))
    A3 =[list(accumulate(a, initial=0)) for a in A2]
    accA = list(zip(*A3))
    return accA
