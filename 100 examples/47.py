#--------------------------------------
#阅读以下代码的输出结果
#class 类
#2018-8-15
#---------------------------------------
#-*- coding=utf-8 -*-
class A(object):
    def go(self):
        print('go A go! ')
    def stop(self):
        print('stop A stop!')
    def pause(self):
        return Exception('Not Implemented')

class B(A):
    def go(self):
        super(B, self).go()
        print('go B go!')

class C(A):
    def go(self):
        super(C, self).go()
        print('go C go!')
    def stop(self):
        super(C, self).stop()
        print('stop C stop!')

class D(C,B):
    def go(self):
        super(D, self).go()
        print('go D go!')
    def stop(self):
        super(D, self).stop()
    def pause(self):
        print('wait D wait')

class E(B,C):
    pass
print('function a:')
a = A()
a.go()
a.stop()
a.pause()
print('')

print('function B:')
b =B()
b.go()
b.stop()
b.pause()
print('')

print('function C:')
c = C()
c.go()
c.stop()
c.pause()
print('')

print('function D:')
d = D()
d.go()
d.stop()
d.pause()
print('')

print('function E:')
e = E()
e.go()
e.stop()
e.pause()
print('')
