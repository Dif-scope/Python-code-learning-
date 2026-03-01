#文件的写用"w"来实现，如果文件不存在，则自动创建。如果文件存在，则会覆盖原有内容。
#如果不想覆盖，则可以使用"a"来实现追加写入。
#此外，写入文件时，可以使用write()方法来写入字符串，也可以使用writelines()方法来写入一个字符串列表。
#如果既想读又想写，可以使用"r+"模式来打开文件，这样就可以同时进行读写操作了。

#在当前文件夹写一个文件
with open(r"D:\Python warehouse\code\for learning\poem.txt","w",encoding="utf-8") as f:
    f.write("庭院深深深几许，杨柳堆烟，帘幕无重数。\n")

#然后续写上面的古诗
with open(r"D:\Python warehouse\code\for learning\poem.txt","a",encoding="utf-8") as f:
    f.write("玉勒雕鞍游冶处，楼高不见章台路。\n")


