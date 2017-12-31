#making classes and objects and inheriting them , using multilevel inheritance , multipleinheritance , single inheritance.
import math

class Grand():
    z = 10
    def put(self):
        print "you are in grand parent class"
        
        return;
    
class Parent(Grand):
    def getdata(self):
        self.x = input("enter x")
        self.y = input("enter y")
        return;
    
    def display(self):
        print "you are in parent class"
        b = self.x+self.y- self.z
        return;

class Child(Parent):
    def displaychild(self):
        print "you are in child class"
        a = self.x - self.y  - self.z
        print a
        return;

'''class PostChild(Parent(),Child()):
    def 
'''
c = Child()
c.getdata()
c.display()
c.displaychild()

