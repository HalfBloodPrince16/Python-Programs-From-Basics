import numpy as np 
import pandas as pd 

class dog:
	species = "mammal"
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def display(self):
		print(self.name)
		print(self.age)


a = dog("philo",5)
a.display()
