"""
简易计算器模块
提供加、减、乘、除基础运算
"""
class Calculator:
    """四则运算计算器"""
    
    def add(self, a, b):
        """加法：返回 a + b"""
        return a + b
    
    def subtract(self, a, b):
        """减法：返回 a - b"""
        return a - b
    
    def multiply(self, a, b):
        """乘法：返回 a * b"""
        return a * b
    
    def divide(self, a, b):
        """
        除法：返回 a / b
        Raises:
            ZeroDivisionError: 当除数 b 为 0 时
        """
        if b == 0:
            raise ZeroDivisionError("除数不能为零")
        return a / b