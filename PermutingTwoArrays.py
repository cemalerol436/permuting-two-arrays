


def twoArrays(k,A,B):

    A = [1,2,2,1]
    A.sort()

    B = [3,3,4,4]
    B.sort(reverse=True)

    l=len(A)

    k = 5
    i = 0
    res = ""
    while i<l:
        if A[i]+B[i]>=k:
            res = "YES"
        else:
            return "NO"
        i += 1

    return res

n = input("n:")

k = input("k:")

A = list(map(int, input().rstrip().split()))

B = list(map(int, input().rstrip().split()))

result = twoArrays(k, A, B)

print(result)


