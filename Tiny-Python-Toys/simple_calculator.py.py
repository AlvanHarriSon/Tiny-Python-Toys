import ast
import math
import operator


def evaluate_expression(expression):
    """Evaluate bounded arithmetic only; never execute Python user input."""
    if len(expression) > 1000:
        raise ValueError("表达式过长")
    tree = ast.parse(expression, mode="eval")
    if sum(1 for _ in ast.walk(tree)) > 100:
        raise ValueError("表达式过于复杂")
    binary = {ast.Add: operator.add, ast.Sub: operator.sub,
              ast.Mult: operator.mul, ast.Div: operator.truediv,
              ast.FloorDiv: operator.floordiv, ast.Mod: operator.mod,
              ast.Pow: operator.pow}

    def visit(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            result = node.value
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = visit(node.operand)
            result = value if isinstance(node.op, ast.UAdd) else -value
        elif isinstance(node, ast.BinOp) and type(node.op) in binary:
            left, right = visit(node.left), visit(node.right)
            if isinstance(node.op, ast.Pow) and abs(right) > 1000:
                raise ValueError("指数过大")
            result = binary[type(node.op)](left, right)
        elif (isinstance(node, ast.Call) and not node.keywords and len(node.args) == 1
              and (isinstance(node.func, ast.Name) and node.func.id == "sqrt"
                   or isinstance(node.func, ast.Attribute) and node.func.attr == "sqrt"
                   and isinstance(node.func.value, ast.Name) and node.func.value.id == "math")):
            result = math.sqrt(visit(node.args[0]))
        else:
            raise ValueError("只支持数字、算术运算和 sqrt")
        if type(result) not in (int, float) or abs(result) > 1e100 or not math.isfinite(result):
            raise ValueError("结果超出支持的范围")
        return result

    return visit(tree.body)


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
            result = evaluate_expression(expression)
            history.append(result)
            print(f"结果: {result}")
        except ZeroDivisionError:
            print("错误：除数不能为零！")
        except (ValueError, OverflowError):
            print("错误：无效的数字输入！")
        except NameError:
            print("错误：无效的操作符或函数！请输入有效的表达式。")
        except SyntaxError:
            print("错误：无效的语法！请输入有效的表达式。")


if __name__ == "__main__":
    calculator()
