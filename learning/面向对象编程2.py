class Student:
    def __init__(self, name, student_id): #本质上还是一个函数
        self.name = name
        self.student_id = student_id
        self.grades = {"语文": 0, "数学": 0, "英语": 0} #在初始化函数里设置一个属性（字典）来存储成绩，初始值为0分，此成绩不需要输入绑定，交给另一个函数来设置

    def set_grade(self, course, grade): #用另外一个函数设置成绩
        if course in self.grades:
            self.grades[course] = grade
        
    
    def print_grades(self): #用于输出某个学生所有成绩
        print(f"学生{self.name}（学号：{self.student_id}）的成绩为：") 
        for course in self.grades:
            print(f"{course}：{self.grades[course]}分") #self.grades[course]是通过课程名称来获取成绩的值（读字典）。字典名[键]，这里的键是course，值是grade。
#以上函数均属于student类的方法，作用域是有限的，必须通过student类对象来调用

chen = Student("小陈", "100618")
chen.set_grade("语文", 85)
chen.set_grade("数学",100)
chen.set_grade("英语", 99)
chen.print_grades() #不可以直接print_grades(chen),这种调用方法是错误的，作为student类的方法，必须通过student类对象来调用，即chen.print_grades()，在方法前加上对象名和点号。
zeng = Student("小曾", "100622")
print(chen.name)
zeng.set_grade("数学", 95) #对zeng这个对象运用方法（此处为函数）设置成绩
print(zeng.grades)
