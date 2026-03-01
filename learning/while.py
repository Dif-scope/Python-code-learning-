print("你好，我可以帮您计算平均值。")
value=input("请输入一个数字，按下q结束输入：")
total=0
count=0
while value!="q":#不要忘了“”
    total+=float(value)
    count+=1
    value=input("请输入一个数字，按下q结束输入：")
if count==0:
    print("无法计算")
else:
    print("平均值为"+str(total/count))