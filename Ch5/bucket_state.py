#!/usr/bin/env python
# coding=UTF-8
# Ch5 三個水桶等分8公升水的問題

BUCKETS_COUNT = 3	# number of buckets
#state_list = []		# store bucket_state list in current search


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
	
	
def can_take_dump_action(state, limit, bucket_from, bucket_to):
	if (bucket_from >= 0 ) and (bucket_from < BUCKETS_COUNT):
		if (bucket_to >= 0 ) and (bucket_to < BUCKETS_COUNT):
			if ( bucket_from != bucket_to ) and (not is_bucket_empty(state, bucket_from)) and (not is_bucket_full(state, limit, bucket_to)):
				return True
	return False
	
def is_bucket_empty(state, bucket):
	return (state.buckets[bucket] == 0)
	
def is_bucket_full(state, limit, bucket):
	return (state.buckets[bucket] >= limit.buckets[bucket] )

def is_processed_state(state_list, new_state):
	for s in state_list:
		if s.buckets == new_state.buckets:
			return True
	return False
		
def is_final_state(state, final_state):
	return (state.buckets == final_state.buckets)

def print_result(state_list):
	for state in state_list:
		print(state)

def search_state_on_action(state_list, current, bucket_from, bucket_to, limit):
	if can_take_dump_action(current, limit, bucket_from, bucket_to):
		next
		
def search_state(state_list, final_state):
	current = state_list[-1]
	
	if (is_final_state(current, final_state)):
		print_result(state_list)
		return True
	
	for j in range(BUCKETS_COUNT):
		for i in range(BUCKETS_COUNT):
			search_state_on_action(state_list, current, i, j, limit)
	
if __name__ == "__main__":





	
	
