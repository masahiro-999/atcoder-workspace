def slide_max(A,k):
    q = deque()
    ret = []
    for i,a in enumerate(A,start=1):
        # remove old one
        if q and q[0][1]+k<=i:
            q.popleft()
        # aより小さいものは除く
        while q and q[-1][0] <a:
            q.pop()
        q.append((a,i))
        if i<k:
            continue
        ret.append(q[0][0])
    return ret

# a = [1,2,3,2,4,1,2,6,3,1,1,1]
# print(a)
# print(slide_max(a,3))