from room import Room
from player import Player
from world import World
from roomGraphs import largest as roomGraph
from queue import Queue

from random import randint

# Load world
world = World()

world.loadGraph(roomGraph)
# world.printRooms()
player = Player('P1', world.startingRoom)
queue = Queue()
traversalPath = []
graph = {}
graph[player.currentRoom.id] = {}
for _exit in player.currentRoom.getExits():
	graph[player.currentRoom.id][_exit] = '?'

def buildQueue():
	room = player.currentRoom.id
	currentExits = graph[room]
	unexploredExits = []
	for _exit in currentExits:
		if currentExits[_exit] == '?':
			unexploredExits.append(_exit)
	
	if len(unexploredExits) == 0:
		path = backtrack()
		for _next in path:
			for _exit in graph[room]:
				if graph[room][_exit] == _next:
					queue.enqueue(_exit)
					room = _next
					break
	else:
		queue.enqueue(unexploredExits[
			randint(0, len(unexploredExits)-1)
		])


def backtrack():
	tq = Queue([player.currentRoom.id])
	visited = set()
	while len(tq) > 0:
		path = tq.dequeue()
		last = path[-1]
		if last not in visited:
			visited.add(last)
			for _exit in graph[last]:
				_exit = graph[last][_exit]
				if _exit == '?':
					return path
				else:
					tq.enqueue(path + [_exit])
	return []


buildQueue()

inverse = {'n': 's', 'w': 'e', 's': 'n', 'e': 'w'}
while len(queue) > 0:
	start = player.currentRoom.id
	_next = queue.dequeue()
	player.travel(_next)
	traversalPath.append(_next)
	end = player.currentRoom.id
	graph[start][_next] = end
	if end not in graph:
		graph[end] = {}
		for _exit in player.currentRoom.getExits():
			graph[end][_exit] = '?'
	graph[end][inverse[_next]] = start
	if len(queue) == 0:
		buildQueue()

# print(traversalPath)

# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)
for move in traversalPath:
	player.travel(move)
	visited_rooms.add(player.currentRoom)

print()
if len(visited_rooms) == len(roomGraph):
	print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
	print("TESTS FAILED: INCOMPLETE TRAVERSAL")
	print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")
print()

#######
# UNCOMMENT TO WALK AROUND
#######
# player.currentRoom.printRoomDescription(player)
# while True:
# 	cmds = input("-> ").lower().split(" ")
# 	if cmds[0] in ["n", "s", "e", "w"]:
# 		player.travel(cmds[0], True)
# 	else:
# 		print("I did not understand that command.")
