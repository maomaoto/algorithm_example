#!/usr/bin/env python
# coding=UTF-8
# Ch6 妖怪與和尚過河問題

class Boat_Location:
	LOCAL = 0
	REMOTE = 1
	
	rev = ['LOCAL', 'REMOTE']

class Action_Name:
	ONE_MONSTER_GO = 0
	TWO_MONSTER_GO = 1
	ONE_MONK_GO = 2
	TWO_MONK_GO = 3
	ONE_MONSTER_ONE_MONK_GO = 4
	ONE_MONSTER_BACK = 5
	TWO_MONSTER_BACK = 6
	ONE_MONK_BACK = 7
	TWO_MONK_BACK = 8
	ONE_MONSTER_ONE_MONK_BACK = 9
	INVALID_ACTION_NAME = 10
	
	rev = ['ONE_MONSTER_GO', 'TWO_MONSTER_GO', 'ONE_MONK_GO', 'TWO_MONK_GO', 'ONE_MONSTER_ONE_MONK_GO', 'ONE_MONSTER_BACK',
		'TWO_MONSTER_BACK', 'ONE_MONK_BACK', 'TWO_MONK_BACK', 'ONE_MONSTER_ONE_MONK_BACK', 'INVALID_ACTION_NAME']
	
class Item_State:
	'''
		Describe the state
	'''
	MONSTER_COUNT = 3
	MONK_COUNT = 3
	
	def __init__(self):
		self.Local_Monster = None
		self.Local_Monk = None
		self.Remote_Monster = None
		self.Remote_Monk = None
		self.Boat = None
		self.Curr_Act = None
	
	def can_take_action(self, ae):
		if (self.Boat == ae.Boat_To):
			return False
		if (self.Local_Monster + ae.Move_Monster < 0) or (self.Local_Monster + ae.Move_Monster > Item_State.MONSTER_COUNT):
			return False
		if (self.Local_Monk + ae.Move_Monk < 0) or (self.Local_Monk + ae.Move_Monk > Item_State.MONK_COUNT):
			return False
		
		return True

	def is_final_state(self):
		if (self.Local_Monster == 0) and (self.Local_Monk == 0) and (self.Remote_Monster == Item_State.MONSTER_COUNT) and (self.Remote_Monk == Item_State.MONK_COUNT):
			return True
		else:
			return False
	
	def is_valid_state(self):
		if (self.Local_Monk != 0) and (self.Local_Monk < self.Local_Monster):
			return False
		if (self.Remote_Monk != 0) and (self.Remote_Monk < self.Remote_Monster):
			return False
		
		return True
		
	
	def __str__(self):
		return "[{0}, {1}, {2}, {3}, {4}] do {5}".format(self.Local_Monster, self.Local_Monk, self.Remote_Monster, self.Remote_Monk, Boat_Location.rev[self.Boat], Action_Name.rev[self.Curr_Act])
		
		
		
		
	
class Action_Effection:
	def __init__(self, act, boat_to, move_monster, move_monk):
		self.Act = act
		self.Boat_To = boat_to
		self.Move_Monster = move_monster
		self.Move_Monk = move_monk

	def __str__(self):
		return Action_Name.rev[self.Act]
		
act_effect = [
	Action_Effection(act = Action_Name.ONE_MONSTER_GO, 				boat_to = Boat_Location.REMOTE, move_monster = -1, move_monk = 0),
	Action_Effection(act = Action_Name.TWO_MONSTER_GO, 				boat_to = Boat_Location.REMOTE, move_monster = -2, move_monk = 0),
	Action_Effection(act = Action_Name.ONE_MONK_GO, 				boat_to = Boat_Location.REMOTE, move_monster = 0, move_monk = -1),
	Action_Effection(act = Action_Name.TWO_MONK_GO, 				boat_to = Boat_Location.REMOTE, move_monster = 0, move_monk = -2),
	Action_Effection(act = Action_Name.ONE_MONSTER_ONE_MONK_GO, 	boat_to = Boat_Location.REMOTE, move_monster = -1, move_monk = -1),
	Action_Effection(act = Action_Name.ONE_MONSTER_BACK, 			boat_to = Boat_Location.LOCAL, move_monster = 1, move_monk = 0),
	Action_Effection(act = Action_Name.TWO_MONSTER_BACK, 			boat_to = Boat_Location.LOCAL, move_monster = 2, move_monk = 0),
	Action_Effection(act = Action_Name.ONE_MONK_BACK, 				boat_to = Boat_Location.LOCAL, move_monster = 0, move_monk = 1),
	Action_Effection(act = Action_Name.TWO_MONK_BACK, 				boat_to = Boat_Location.LOCAL, move_monster = 0, move_monk = 2),
	Action_Effection(act = Action_Name.ONE_MONSTER_ONE_MONK_BACK, 	boat_to = Boat_Location.LOCAL, move_monster = 1, move_monk = 1)
]
		
		
def search_state(State_List):
	current = State_List[-1]
	
	if (current.is_final_state()):
		print_result(State_List)
		print("")
		return True
	
	for i in range(len(act_effect)):
		#print(i)
		search_state_on_new_action(State_List = State_List, current = current, ae = act_effect[i])
		
		
def search_state_on_new_action(State_List, current, ae):
	next = Item_State()
	if (make_action_new_state(current, ae, next)):
		#print(next)
		#print(next.is_valid_state())
		if next.is_valid_state() and (not is_processed_state(State_List, next)):
			State_List.append(next)
			
			search_state(State_List)
			State_List.pop()
		
	
def make_action_new_state(curr_state, ae, new_state):
	if (curr_state.can_take_action(ae)):
		new_state.Local_Monster = curr_state.Local_Monster + ae.Move_Monster
		new_state.Local_Monk = curr_state.Local_Monk + ae.Move_Monk
		new_state.Remote_Monster = curr_state.Remote_Monster - ae.Move_Monster
		new_state.Remote_Monk = curr_state.Remote_Monk - ae.Move_Monk
		new_state.Boat = ae.Boat_To
		new_state.Curr_Act = ae.Act
		return True
	else:
		return False

def is_processed_state(state_list, new_state):
	for s in state_list:
		if (s.Local_Monster == new_state.Local_Monster) and (s.Local_Monk == new_state.Local_Monk):
			if (s.Remote_Monster == new_state.Remote_Monster) and (s.Remote_Monk == new_state.Remote_Monk) and (s.Boat == new_state.Boat):
				return True
	return False

def print_result(state_list):
	for state in state_list:
		print(state)
	
if __name__ == "__main__":
	state_init = Item_State()
	state_init.Local_Monster = Item_State.MONSTER_COUNT
	state_init.Local_Monk = Item_State.MONK_COUNT
	state_init.Remote_Monster = 0
	state_init.Remote_Monk = 0
	state_init.Boat = Boat_Location.LOCAL
	state_init.Curr_Act = Action_Name.INVALID_ACTION_NAME
	
	state_list = []
	state_list.append(state_init)
	
	search_state(state_list)





	
	
