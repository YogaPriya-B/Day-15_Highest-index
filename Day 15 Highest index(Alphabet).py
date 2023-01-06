import json
name=input()
a=0
str1=""
name=name.lower()
for i in name:
    if(ord(i)>a):
        a=ord(i)
        b=i
  

str1+=str(a-96)
str1+=str(b) 
print(json.dumps(str1))
