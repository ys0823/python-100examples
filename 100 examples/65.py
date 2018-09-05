#--------------------------------------
#题目：以下的代码的输出将是什么? 说出你的答案并解释。
#2018-8-23
#-------------------------------------
class Parent(object):
    x =1
class Child1(Parent):
    pass
class Child2(Parent):
    pass
print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x , Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x) #父类被改变会影响到任何未重写该值的子类当中的值