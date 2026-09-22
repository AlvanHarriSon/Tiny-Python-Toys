import secrets
from random import SystemRandom
import string

def generate_password(length=8, include_digits=True, include_symbols=True):
    if isinstance(length, bool) or not isinstance(length, int):
        raise ValueError("密码长度必须是整数")
    if length < 4:
        raise ValueError("密码长度必须至少为4以确保包含所有类型的字符")

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits if include_digits else ''
    symbols = string.punctuation if include_symbols else ''


    # 确保密码至少包含一个大写字母、一个小写字母、一个数字和一个特殊符号
    password = [
        secrets.choice(upper),
        secrets.choice(lower),
        secrets.choice(digits) if include_digits else '',
        secrets.choice(symbols) if include_symbols else ''
    ]

    # 去除空字符串
    password = [char for char in password if char]

    remaining_length = length - len(password)
    all_characters = upper + lower + digits + symbols

    for _ in range(remaining_length):
        password.append(secrets.choice(all_characters))

    SystemRandom().shuffle(password)
    return "".join(password)

def get_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    strength = 0
    if length >= 8:
        strength += 1
    if length >= 12:
        strength += 1
    if has_upper and has_lower and has_digit and has_symbol:
        strength += 1

    if strength == 3:
        return "强"
    elif strength == 2:
        return "中"
    else:
        return "弱"


if __name__ == "__main__":
    try:
        length = int(input("请输入密码长度(默认8): ") or 8)
        include_digits = input("是否包含数字(y/n，默认y): ").lower() in ['y', '']
        include_symbols = input("是否包含特殊符号(y/n，默认y): ").lower() in ['y', '']

        password = generate_password(length, include_digits, include_symbols)
        print(f"生成的密码是: {password}")

        strength = get_password_strength(password)
        print(f"密码强度是: {strength}")
    except ValueError as e:
        print(e)
