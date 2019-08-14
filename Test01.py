'''a,b=0,1
while b<10:
    print(b,end=" ")
    a,b=b,a+b

    nn=1
while nn==1:
    num=int(input("请输入一个数字: "))
    print("输入的数字=%d"%(num))
    '''

'''
num=int(input("请输入一个数字："))
if num>5:
    print("num大于5")
else:
    print("num小于5")

n=100
sum=0
counter=1
while counter<=n:
    sum+=counter
    counter+=1
print("sum=%d" %(sum));




list01=[1,22,33,444,555,'666','77777']
for ii in list01:
    print(ii)


import sys

list=[1,2,3,4,5,6,7]
it=iter(list)

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()'''

def f01(Width,Height):
    return Width*Height

def f02(name):
    print("Welcome",name)

print("面积area=",f01(5,10))
f02("Tom")




