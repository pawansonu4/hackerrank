import collections
def merge_the_tools(string, k):
    # your code goes here n=12,k=4
    n=len(string)
    array=[]
    fin_array=[]
    for i in range(0,n,k):
        array.append(string[i:i+k])
        x=string[i:i+k]
        #print(x)
        y=collections.OrderedDict.fromkeys(list(x))
        #print(y)
        z="".join(y)
        print(z)
    #print(array)
    #print(fin_array)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)