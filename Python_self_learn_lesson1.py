#numpy study
# print("hello world!!!")
import numpy as np
arr=np.array(5) #0 维数组
print(arr)
print(arr.ndim)
arr=np.array([1,2,3,4,5]) #1 维数组
print(arr)
print(arr.ndim)

#循环结构
sum=0
for x in range(101): #1-100
    # sum=sum+x
    sum+=x
print(sum)

for x in range(90,100,3): #range, 步长
    print(x)

#While 循环，重点在于什么时候结束循环
start=1
while start<=10:
    print(start)
    start+=1
print(start)

is_continue=True
while is_continue==True:
    print('1:修改菜单')
    print('2:添加菜单')
    print('3:删除菜单')
    print('0:退出操作')
    id=int(input("id="))
    if id==1:
        print('修改成功')
    if id==2:
        print('添加成功')
    if id==3:
        print('删除成功')
    if id==0:
        print('退出系统')
        is_continue=False
