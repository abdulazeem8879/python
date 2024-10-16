x=1
while x<10:
    # print('python is very easy')
    x=x+1

# ................
y=1

while y<6:
    y=y+1
    if y==2:
        continue #skip below code and move to the top of loop
    if y==4:
        break #it will come out of the loop
    print(f"python {y}")
    
   
   
    print('out side of loop')
    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
for i in range(4):
    print(i)

l1=[10,20,30,40]
for x in l1:
    print(x)

person={"name":"sam","age":21,"address":"nanded"}

for keys in person:
    print(keys)

for val in person.values():
    print(val)
    
for all in person.items():
    print(all)

#  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

num=0

while num<20 :
    num=num+2
    print(num)
    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
for u in range(10):
    print(f" {2}*{u}={u*2}")