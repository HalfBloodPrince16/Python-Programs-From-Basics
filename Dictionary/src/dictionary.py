import math

dic ={'jack':' is brave','tina':' is pretty','john':' is insane'}

s = raw_input("enter the keyword to search in dictionary")
flag = 0;
for k,v in dic.items():

    if k == s:
        print(dic[s])
        flag = 1
        break;

if flag == 0:
    print "sorry ur search not found"