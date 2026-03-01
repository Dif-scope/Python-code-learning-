with open(r"C:\Users\fish\Desktop\Aikefei's Legendary Quest Ultimate Treasure.txt","r",encoding="utf-8") as f:
    content=f.readlines() #有f.read()和f.readlines()两种读取方式，前者一次性读取整个文件，后者按行读取并返回一个列表。
    for line in content:
        print(line)

#with open具有自动关闭文件的功能，不需要使用f.close().关闭。
#注意缩进