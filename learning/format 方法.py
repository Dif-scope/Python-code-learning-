#方法一
message_content = """
律回春渐，新元肇启。
新岁甫至，福气东来。
金{0}贺岁，欢乐祥瑞。
金{0}敲门，五福临门。
给{1}及家人拜年啦！
新春快乐，{0}年大吉！
""".format("马", "你")

print(message_content)

#方法二
message_content = """
律回春渐，新元肇启。
新岁甫至，福气东来。
金{year}贺岁，欢乐祥瑞。
金{year}敲门，五福临门。
给{person}及家人拜年啦！
新春快乐，{year}年大吉！
""".format(year="马", person="你")

print(message_content)

#方法三
year="马"
person="你"
#注意这里下面有f字符的！其用处就是可以让{}中的变量被替换成对应的值。
message_content = f""" 
律回春渐，新元肇启。
新岁甫至，福气东来。
金{year}贺岁，欢乐祥瑞。
金{year}敲门，五福临门。
给{person}及家人拜年啦！
新春快乐，{year}年大吉！
"""

print(message_content)

