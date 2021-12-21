
#Fuction controls two arrays if they can make more than "k" number.

def twoArrays(k, first_array, second_array):

    first_array = [1,2,2,1]
    first_array.sort()

    second_array = [3,3,4,4]
    second_array.sort(reverse=True)

    len_a = len(first_array)

    i = 0
    res = ""


    #In this Loop it check the summarize of two arrays.
    while i < len_a:
        if first_array[i]+second_array[i] >= k:
            res = "YES"
        else:
            return "NO"
        i += 1

    return res


# "k" number is the number sum of arrays suppose to be bigger.

k = int(input("k:"))

first_array = list(map(int, input().rstrip().split()))

second_array = list(map(int, input().rstrip().split()))

result = twoArrays(k, first_array, second_array)

print(result)


