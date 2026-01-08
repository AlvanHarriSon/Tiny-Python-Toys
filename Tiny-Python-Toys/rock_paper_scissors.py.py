import random

def play_game(scores):
    options = ['石头', '剪刀', '布']
    computer = random.choice(options)
    player = input("请出拳（石头/剪刀/布）: ").strip()
    
    if player not in options:
        print("无效输入，请重新选择！")
        return
    
    print(f"你出了: {player}")
    print(f"电脑出了: {computer}")
    
    if player == computer:
        print("平局！")
        scores['平局'] += 1
    elif (player == '石头' and computer == '剪刀') or \
         (player == '剪刀' and computer == '布') or \
         (player == '布' and computer == '石头'):
        print("你赢了！")
        scores['赢'] += 1
    else:
        print("你输了！")
        scores['输'] += 1

def main():
    scores = {'赢': 0, '输': 0, '平局': 0}
    
    while True:
        play_game(scores)
        print(f"\n当前比分：赢 {scores['赢']} 次，输 {scores['输']} 次，平局 {scores['平局']} 次")
        
        again = input("再玩一次？(y/n): ").lower()
        if again != 'y':
            break

main()
