import random

nums=[4,6,2,7,8,65,45,43]

# mao pao pai xu
# j=0
# while j<len(nums)-1:
#     i=0
#     Flag = True
#     while i<len(nums)-1-j:
#         if  nums[i]>nums[i+1]:
#             nums[i],nums[i+1]=nums[i+1],nums[i]
#             Flag=False
#         i+=1
#
#     if Flag==True:
#         break
#     j+=1
# print(nums)
#sort pai xu
nums.sort(reverse=True)
#lambda biaodashi
print(nums)
a=lambda x,y:x*y
a(3,4)

#shan chu chongfu shu ju, zidian de key mei chongfu
# print(a(3,4))
# a=[2,3,4,2,3,7,5,8,7]
# b={}
# b=b.fromkeys(a)
# print(b)
# c=list(b.keys())
# print(c)
#
# #yuan zu zhuan liebiao
# tuple_list=(2,4,6,32)
# m=list(tuple_list)
# print(m)
# #lie biao zhuan yuan zu
# list_num=[3,45,32,22]
# m=tuple(list_num)
# print(m)

m=random.randint(0,3)#suiji fanhui zhe ge fan wei de yige zhengshu
# print(m)
n=random.random()#suiji fan hui 0dao1 zhijiao de suiji xiaoshu
# print(n)
c=random.randrange(2,10,3)#suiji fan hui 2dao10 zhijian de 3wei jieti de shu :2,5,8
# print(c)
# for i in range (2,5):#shengcheng 2dao5 de zhengshu ,zuo bi you kai





