def average(array):
    # your code goes here
    x=set(array)
    sum=0
    for i in x:
        sum=sum+i
    avg=sum/len(x)
    return avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)