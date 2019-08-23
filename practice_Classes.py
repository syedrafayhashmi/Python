#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Cereal():
    def __init__(self,name,brand,fiber):
        self.x = name
        self.y = brand
        self.z = fiber
    def __str__(self):
        return  '{} cereal is produced by {} and has {} grams of fiber in every serving!'.format(self.x,self.y,self.z)
c1=Cereal("Corn Flakes" , "Kellogg's", 2)
c2=Cereal("Honey Nut Cheerios" , "General Mills", 3)
print(c1)
print(c2)


# In[5]:


class Point:

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

p = Point(3,4)
q = Point(5,12)
mid = p.halfway(q)
# note that you would have exactly the same result if you instead wrote
# mid = q.halfway(p)
# because they are both Point objects, and the middle is the same no matter what

print(mid)
print(mid.getX())
print(mid.getY())


# In[6]:


class Bike():
    def __init__(self,color,price):
        self.color = color
        self.price = price
testOne = Bike('blue',89.99)
testTwo = Bike('purple',25.0)


# In[41]:


class AppleBasket():
    def __init__(self,x,y):
        self.apple_color = x
        self.apple_quantity = y
    
    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity,self.apple_color)
    def increase(self):
        self.apple_quantity += 1 
        return self.apple_quantity
print(AppleBasket('red',4))

a= AppleBasket('red',4).increase()

print(a)

        


# In[42]:


class BankAccount():
    def __init__(self,name,amt):
        self.name = name
        self.amt = amt
    def __str__(self):
        return  "Your account, {}, has {} dollars.".format(self.name,self.amt)
t1 = BankAccount('Bob',100)
print(t1)


# In[ ]:




