try: #放入你觉得可能产生异常的代码
    user_weight = float(input("请输入您的体重（单位: kg）: "))
    user_height = float(input("请输入您的身高（单位: m）: "))
    user_BMI = user_weight / user_height ** 2
except ValueError: #然后对每种异常进行处理
    print("输入不为合理数字，请重新运行程序，并输入正确的数字。")
except ZeroDivisionError: #这里是针对分母为零时系统的报错进行提示
    print("身高不能为零，请重新运行程序，并输入正确的数字。")
except:  #面对没料到的错误，这是一个通用的处理
    print("发生了未知错误，请重新运行程序。")
else: #如果都没错，正常输出
    print("您的BMI值为: " + str(user_BMI))
finally: #无论如何，终将输出
    print("程序结束运行。")