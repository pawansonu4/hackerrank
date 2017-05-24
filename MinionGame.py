import string
def minion_game(string1):
    if string1.islower():
        exit()
    # your code goes here
    stuart_count=0
    kevin_count=0
    word_list=list(string1)
    stuart_words=[]
    kevin_words=[]

    vowels=['A','E','I','O','U']
    for j in range(len(word_list)):
        k=j+1
        for i in range(len(word_list)):
            if word_list[i] in vowels:
                if k+i > len(word_list):
                    break
                else:
                    kevin_words.append("".join(word_list[i:k+i]))
            else:
                if k + i > len(word_list):
                    break
                else:
                    stuart_words.append("".join(word_list[i:k+i]))

    set_array_stuart=set(stuart_words)
    set_array_kevin=set(kevin_words)
    for i in set_array_stuart:
        for j in stuart_words:
            if i ==j:
                stuart_count=stuart_count+1


    for i in set_array_kevin:
        for j in kevin_words:
            if i == j:
                kevin_count = kevin_count + 1

    if kevin_count > stuart_count:
        print ("Kevin " + str(kevin_count))
    elif stuart_count > kevin_count:
        print ("Stuart " + str(stuart_count))
    else:
        print("Draw")



if __name__ == '__main__':
    s = input()
    minion_game(s)