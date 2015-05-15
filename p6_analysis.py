from p6_game import Simulator
from heapq import heappush, heappop
import Queue

ANALYSIS = {}

def analyze(design):
	sim = Simulator(design)
	init = sim.get_initial_state()
	
	
	queue = []#Queue.Queue()
	discover = []
	prev = {}
	#queue.put(init)
	heappush(queue, init)
	discover.append(init)
	position, abilities = init
	ANALYSIS[init] = None
	
	
	while queue:
		state = heappop(queue)
		moves = sim.get_moves()
		#print state
		for move in moves:
			next_state = sim.get_next_state(state, move)
			
			if next_state not in discover and next_state != None:
				heappush(queue, next_state)
				discover.append(next_state)
				position, abilities = next_state
				ANALYSIS[next_state] = state
				#print ANALYSIS


def inspect((i,j), draw_line):
	pos1 = (i,j)
	for key in ANALYSIS:
		pos,abi = key
		if(pos1 == pos):
			state = ANALYSIS[key]
			while state:
				pos2, abil = state
				draw_line(pos1,pos2)
				if state in ANALYSIS:
					state = ANALYSIS[state]
					pos1 = pos2
	
	# TODO: use ANALYSIS and (i,j) draw some lines
	#raise NotImplementedError
	