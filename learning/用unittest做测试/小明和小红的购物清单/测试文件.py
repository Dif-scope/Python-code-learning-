import unittest #①引入库
from 主体被测文件 import ShoppingList #②导入主体文件中的类或者函数
#④接下来创建一个用来测试的类
class TestShoppingList(unittest.TestCase): #测试类必须继承unittest.TestCase,注意拼写
    def setUp(self): #⑤如果有需要，创建setUp方法。setUp方法会在每个test_开头调用，可以初始化一些数据
        #接下来定义一些属性和测试数据，注意这里的测试数据是用来测试主体文件中的方法的，所以要用到主体文件中的类或者函数
        #看看小明的
        self.xiaoming_list=ShoppingList("小明的购物清单",{"胡萝卜":3.5,"黄瓜":2.0,"香蕉":1.5}) #这里定义了一个属性xiaoming_list，并且用主体文件中的类ShoppingList来创建一个对象，传入一些测试数据。
        #看看小红这个富婆的
        self.xiaohong_list=ShoppingList("小红的购物清单",{"拖鞋":999,"裙子":666,"包包":50000,"手机":8000,"限定口红":9999,"兰博基尼定制款":99999999})
    #⑥定义测试方法（你想要怎样测试？）
    def test_caculate_total_price(self): #必须要以test_开头，要定位
        #使用assertEqual来看看数据是否一致吧
        self.assertEqual(self.xiaoming_list.caculate_total_price(),7.0)
        self.assertEqual(self.xiaohong_list.caculate_total_price(),11106666) #故意算错，直接给小红去了一位数，但是小红表示不差这点钱哈

        #必须要弄清楚self.xiaohong_list.caculate_total_price(),11106666这里一大坨每个部分的意义
        #self用于访问当前对象的属性和方法，这里访问的就是setUp里面定义的属性xiaohong_list
        #caculate_total_price()是主体文件中的方法，这里调用来计算总价

        

    
#主体文件在这里。  # ← 你的注释原样保留！❤️

# ⭐⭐⭐ 仅添加以下2行（修复"无反馈"问题）⭐⭐⭐
if __name__ == '__main__':
    unittest.main(verbosity=2)

# 这段代码是 Python 中常见的测试启动模式，主要用于单元测试。它的含义如下：
# 
# 1. **`if __name__ == '__main__':`**  
#    这是一个条件判断，用于检查当前模块是否作为主程序直接运行（而不是被其他模块导入）。  
#    - 当直接运行该脚本时，`__name__` 变量的值会被设置为 `'__main__'`，因此条件成立，缩进的代码块会被执行。  
#    - 如果该模块被其他模块通过 `import` 导入，则 `__name__` 为模块的实际名称（例如文件名），此时条件不成立，代码块不会执行。  
#    这种写法允许模块既可以被导入使用，也可以独立运行测试。
# 
# 2. **`unittest.main(verbosity=2)`**  
#    这是 Python 内置单元测试框架 `unittest` 的入口函数，用于执行当前模块中定义的所有测试用例（即继承 `unittest.TestCase` 的类中的 `test_` 开头的方法）。  
#    - `verbosity` 参数控制输出信息的详细程度，可选值为 0、1、2：  
#      - `0`：静默模式，只显示总结果。  
#      - `1`（默认）：显示每个测试用例的简单进度（用 `.` 表示成功，`F` 表示失败等）。  
#      - `2`：详细模式，会显示每个测试方法的名称及其结果，便于调试。  
#    此外，`unittest.main()` 也会解析命令行参数，例如运行脚本时加上 `-v` 选项等价于 `verbosity=2`。
# 
# **综合起来**：这段代码的意思是，当该脚本被直接运行时，启动单元测试，并以详细模式（`verbosity=2`）输出每个测试用例的执行过程和结果。这是 Python 测试脚本的标准写法。