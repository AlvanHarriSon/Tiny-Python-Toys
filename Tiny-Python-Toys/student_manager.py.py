class Student:
    def __init__(self, name, age, major, university, grade):
        self.name = name
        self.age = age
        self.major = major
        self.university = university
        self.grade = grade
    
    def introduce(self):
        return f"大家好，我是{self.name}，今年{self.age}岁，是{self.university}{self.major}专业{self.grade}的学生。"
    
    def study(self, subject):
        return f"{self.name}正在学习{subject}。"
    
    def take_exam(self, subject):
        return f"{self.name}正在参加{subject}考试。"
    
    def graduate_plan(self):
        return f"{self.name}计划毕业后继续深造或寻找工作机会。"

# 创建xxx的学生对象
xxx = Student(
    name="xxx",
    age=20,
    major="数据科学与大数据技术",
    university="清华大学",
    grade="大二"
)

# 演示学生信息
print("=== 学生信息 ===")
print(xxx.introduce())
print()

print("=== 学习活动 ===")
print(xxx.study("数据结构与算法"))
print(xxx.study("数据库系统"))
print(xxx.take_exam("高等数学"))
print()

print("=== 未来规划 ===")
print(xxx.graduate_plan())
