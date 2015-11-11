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
		self.cur_action = None
	
	def __str__(self):
		return str(self.buckets) + " " + str(self.cur_action)
	
	def set_buckets(self, buckets_set):
		for i in range(len(self.buckets)):
			self.buckets[i] = buckets_set[i]
	
	def set_action(self, bucket_from, bucket_to, dumped_water):
		self.cur_action = action(bucket_from = bucket_from, bucket_to = bucket_to, water = dumped_water)
	
def can_take_dump_action(state, limit, bucket_from, bucket_to):
	if (bucket_from >= 0 ) and (bucket_from < BUCKETS_COUNT):
		if (bucket_to >= 0 ) and (bucket_to < BUCKETS_COUNT):
			if ( bucket_from != bucket_to ) and (not is_bucket_empty(state, bucket_from)) and (not is_bucket_full(state, limit, bucket_to)):
				return True
	return False

	
def dump_water(current, bucket_from, bucket_to, next, limit):
	next.set_buckets(current.buckets)
	dumped = limit.buckets[bucket_to] - next.buckets[bucket_to]
	if (next.buckets[bucket_from] >= dumped):
		next.buckets[bucket_to] += dumped
		next.buckets[bucket_from] -= dumped
	else:
		next.buckets[bucket_to] += next.buckets[bucket_from]
		dumped = next.buckets[bucket_from]
		next.buckets[bucket_from] = 0
	
	if dumped > 0 :
		next.set_action(bucket_from = bucket_from, bucket_to = bucket_to, dumped_water = dumped)
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

def search_state_on_action(state_list, current, bucket_from, bucket_to, limit, final_state):
	if can_take_dump_action(current, limit, bucket_from, bucket_to):
		next = bucket_state()
		bDump = dump_water(current, bucket_from, bucket_to, next, limit)
		if bDump and (not is_processed_state(state_list, next)):
			state_list.append(next)
			search_state(state_list, limit, final_state)
			state_list.pop()
		
def search_state(state_list, limit, final_state):
	current = state_list[-1]
	
	if (is_final_state(current, final_state)):
		print_result(state_list)
		return True
	
	for j in range(BUCKETS_COUNT):
		for i in range(BUCKETS_COUNT):
			search_state_on_action(state_list, current, i, j, limit, final_state)
	
if __name__ == "__main__":
	limit = bucket_state()
	limit.set_buckets([8,5,3])
	
	final_state = bucket_state()
	final_state.set_buckets([4,4,0])
	
	state_init = bucket_state()
	state_init.set_buckets([8,0,0])
	
	state_list = []
	state_list.append(state_init)
	
	search_state(state_list, limit, final_state)
	





	
	
