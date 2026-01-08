import random

def guess_number_game():
    print("欢迎来到猜数字游戏！请选择游戏难度：")
    print("1. 简单（1-50）")
    print("2. 中等（1-100）")
    print("3. 困难（1-200）")
    
    difficulty = input("请输入难度编号（1, 2, 或 3）：")
    
    if difficulty == '1':
        number_range = (1, 50)
        max_attempts = 5
    elif difficulty == '2':
        number_range = (1, 100)
        max_attempts = 10
    elif difficulty == '3':
        number_range = (1, 200)
        max_attempts = 15
    else:
        print("输入无效，请选择1, 2, 或 3。")
        return
    
    number = random.randint(*number_range)
    attempts = 0
    
    print(f"我已经想了一个{number_range[0]}到{number_range[1]}之间的数字。你最多有{max_attempts}次机会猜测。")
    
    while attempts < max_attempts:
        try:
            guess = int(input("你的猜测是："))
        except ValueError:
            print("请输入一个有效的数字。")
            continue
        
        attempts += 1
        
        if guess < number:
            print("太小了！")
        elif guess > number:
            print("太大了！")
        else:
            print(f"恭喜你！你用了{attempts}次猜对了！")
            break
        
        if attempts % 3 == 0 and guess != number:
            clue = get_clue(number)
            print(f"提示：这个数字{clue}。")
    
    if attempts == max_attempts and guess != number:
        print(f"很遗憾，你没有在规定次数内猜对。这个数字是{number}。")

def get_clue(number):
    clues = []
    if number % 2 == 0:
        clues.append("是偶数")
    else:
        clues.append("是奇数")
    
    if number % 3 == 0:
        clues.append("能被3整除")
    
    return "和".join(clues)

guess_number_game()
