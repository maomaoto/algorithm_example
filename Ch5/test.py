#!/usr/bin/env python
BUCKETS_COUNT = 3

class action:
	'''
		Define action
		From 'bucket_from' to 'bucket_to' with water quantity 'water'
	'''
	def __init__(self, bucket_from = 0, bucket_to = 0, water = 0):
		self.bucket_from = bucket_from
		self.bucket_to = bucket_to
		self.water = water
	
	def __str__(self):
		return "do {{{0}, {1}, {2}}}".format(self.bucket_from, self.bucket_to, self.water)
		
class bucket_state:
	'''
		Store bucket state and current action
	'''
	def __init__(self):
		self.buckets = [0]*BUCKETS_COUNT
		self.cur_action = action()
	
	def __str__(self):
		return str(self.buckets) + " " + str(self.cur_action)

def app(a):
	a.append(1)

def change(state):
	state.buckets = [1,2,3]

if __name__ == "__main__":
	a = [1,2,3]
	app(a)
	print(a)
	
	next = bucket_state()
	print(next)
	change(next)
	print(next)