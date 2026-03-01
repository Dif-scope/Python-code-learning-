"""
计算器单元测试
使用 unittest 框架验证 Calculator 功能
"""
import unittest
from 被测 import Calculator  # 导入被测试模块

class TestCalculator(unittest.TestCase):
    """计算器测试类"""
    
    def setUp(self):
        """每个测试前自动执行：创建独立计算器实例"""
        self.calc = Calculator()  # ✅ 每个测试用全新实例，避免污染
        print(f"\n[ setUp ] 初始化测试环境: {self._testMethodName}")
    
    def tearDown(self):
        """每个测试后自动执行（可选）：清理资源"""
        print(f"[ tearDown ] 清理完成")
    
    # ========== 核心测试用例 ==========
    def test_add_positive(self):
        """测试：正数相加"""
        self.assertEqual(self.calc.add(2, 3), 5)
    
    def test_add_negative(self):
        """测试：负数相加"""
        self.assertEqual(self.calc.add(-1, -1), -2)
    
    def test_subtract(self):
        """测试：减法"""
        self.assertEqual(self.calc.subtract(10, 4), 6)
    
    def test_multiply(self):
        """测试：乘法"""
        self.assertEqual(self.calc.multiply(3, 7), 21)
    
    def test_divide_normal(self):
        """测试：正常除法"""
        self.assertAlmostEqual(self.calc.divide(10, 2), 5.0)  # 浮点数用 almostEqual
    
    def test_divide_by_zero(self):
        """测试：除零异常（关键！）"""
        with self.assertRaises(ZeroDivisionError):  # ✅ 验证是否抛出指定异常
            self.calc.divide(5, 0)
    
    def test_divide_float(self):
        """测试：浮点数除法"""
        result = self.calc.divide(7, 2)
        self.assertGreater(result, 3.4)  # 验证结果 > 3.4
        self.assertLess(result, 3.6)      # 验证结果 < 3.6

# ========== 运行入口 ==========
if __name__ == '__main__':
    # 详细模式运行（显示每个测试方法）
    unittest.main(verbosity=2)