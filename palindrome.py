text = input ("Enter text: ")
text1 = text.upper()
text2 = text1.replace(" ", "")
if len(text2)<1:
    print ("not palindrome")
else: 
    lst=[]
    for i in text2:
        lst.append(i)
    count = 0
    for i in range(len(lst)):
        if lst[i]==lst[-1-i]:
            count +=1
    if count == len(lst):
        print ("it is palindrome")
    else: 
        print ("not palindrome") 
        
        

