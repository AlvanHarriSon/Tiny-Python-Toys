import math

def calculator():
    print("简易计算器")
    print("支持的操作：加法 (+), 减法 (-), 乘法 (*), 除法 (/), 幂运算 (**), 平方根 (sqrt(x))")
    print("输入 'q' 退出计算器")
    
    history = []
    
    while True:
        print("\n当前历史记录：", history)
        expression = input("请输入表达式: ")
        
        if expression.lower() == 'q':
            print("再见！")
            break
        
        try:
            # 使用 eval 计算表达式，注意安全性
            result = eval(expression)
            history.append(result)
            print(f"结果: {result}")
        except ZeroDivisionError:
            print("错误：除数不能为零！")
        except ValueError:
            print("错误：无效的数字输入！")
        except NameError:
            print("错误：无效的操作符或函数！请输入有效的表达式。")
        except SyntaxError:
            print("错误：无效的语法！请输入有效的表达式。")

calculator()
