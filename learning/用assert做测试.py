#assert可以帮助我们在程序中设置断言，来检查某个条件是否为真，如果条件不满足，就会抛出AssertionError异常，并且可以提供一个错误消息。
#assert语句的基本语法如下：
#assert 条件表达式, "可选错误提示"  （条件为 False 时触发 AssertionError）💡 核心作用
#✅ 调试期逻辑自检：验证“程序运行到此处时，某条件必须成立”
#❌ 非错误处理：不用于用户输入验证、业务异常处理（生产环境可能失效！）

#示例：
x = -5
assert x > 0, "x 必须为正数！"  # 触发 AssertionError: x 必须为正数！

# 常见调试场景
def divide(a, b):
    assert b != 0, "除数不能为0"  # 防御性编程（仅调试用！）
    return a / b

#assert一旦发现错误，就不会再往下读代码了。