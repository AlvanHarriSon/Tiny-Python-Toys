todos = []
completed_todos = []

def show_todos():
    if not todos:
        print("你的待办事项列表是空的！")
    else:
        print("你的待办事项:")
        for i, todo in enumerate(todos, 1):
            print(f"{i}. {todo}")
    
    if completed_todos:
        print("\n已完成的待办事项:")
        for i, todo in enumerate(completed_todos, 1):
            print(f"{i}. {todo}")

def add_todo():
    todo = input("请输入新的待办事项: ").strip()
    if todo:
        todos.append(todo)
        print("已添加！")
    else:
        print("输入不能为空！")

def remove_todo():
    show_todos()
    if todos:
        try:
            num = int(input("输入要删除的待办事项编号: "))
            if 1 <= num <= len(todos):
                removed = todos.pop(num-1)
                print(f"已删除: {removed}")
            else:
                print("无效编号！")
        except ValueError:
            print("请输入有效数字！")
    else:
        print("没有待办事项可删除！")

def mark_completed():
    show_todos()
    if todos:
        try:
            num = int(input("输入要标记为已完成的待办事项编号: "))
            if 1 <= num <= len(todos):
                completed = todos.pop(num-1)
                completed_todos.append(completed)
                print(f"已标记为已完成: {completed}")
            else:
                print("无效编号！")
        except ValueError:
            print("请输入有效数字！")
    else:
        print("没有待办事项可标记为已完成！")

while True:
    print("\n待办事项管理器")
    print("1. 查看待办事项")
    print("2. 添加待办事项")
    print("3. 删除待办事项")
    print("4. 标记为已完成")
    print("5. 退出")
    choice = input("请选择操作(1/2/3/4/5): ").strip()
    
    if choice == '1':
        show_todos()
    elif choice == '2':
        add_todo()
    elif choice == '3':
        remove_todo()
    elif choice == '4':
        mark_completed()
    elif choice == '5':
        print("再见！")
        break
    else:
        print("无效选择，请重试！")
