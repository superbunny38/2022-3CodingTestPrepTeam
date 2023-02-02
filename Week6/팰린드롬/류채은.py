#10066

def is_palindrome(sentence):
    if sentence == sentence[::-1]:
        return True
    else:
        return False

max_len = 0
str_arr = input()
for i in range(len(str_arr),-1,-1):
    for j in range(0,i):
        checking = str_arr[j:i]
        #print(checking,"len:",i-j)
        if is_palindrome(checking) == True:
            count = str_arr.count(checking)
            #print("checking:",checking,"score:",count*(i-j))
            max_len = max(max_len,count*(i-j))
print(max_len)
        
