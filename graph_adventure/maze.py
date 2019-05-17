from room import Room
from player import Player
from world import World
from roomGraphs import largest as roomGraph
from queue import Queue

from random import randint

class Maze:
	def __init__(self, playerName):
		self.world = World()
		self.world.loadGraph(roomGraph)

		self.player = Player(playerName, self.world.startingRoom)
		
		self.inverse = {'n': 's', 'w': 'e', 's': 'n', 'e': 'w'}

		self.reset(initial=True)

	def buildQueue(self):
		roomId = self.player.currentRoom.id
		currentExits = self.graph[roomId]
		unexploredExits = []
		for _exit in currentExits:
			if currentExits[_exit] == '?':
				unexploredExits.append(_exit)

		if len(unexploredExits) == 0:
			for _next in self.backtrack():
				for _exit in self.graph[roomId]:
					if self.graph[roomId][_exit] == _next:
						self.queue.enqueue(_exit)
						roomId = _next
						break
		else:
			self.queue.enqueue(unexploredExits[
				randint(0, len(unexploredExits)-1)
			])

	def backtrack(self):
		tq = Queue([self.player.currentRoom.id])
		visited = set()
		while len(tq) > 0:
			path = tq.dequeue()
			last = path[-1]
			if last not in visited:
				visited.add(last)
				for _exit in self.graph[last]:
					_exit = self.graph[last][_exit]
					if _exit == '?':
						return path
					else:
						tq.enqueue(path + [_exit])
		return []

	def traverse(self):
		self.reset()
		while len(self.queue) > 0:
			start = self.player.currentRoom.id
			_next = self.queue.dequeue()
			self.player.travel(_next)
			self.traversal.append(_next)
			end = self.player.currentRoom.id
			self.graph[start][_next] = end
			if end not in self.graph:
				self.graph[end] = {}
				for _exit in self.player.currentRoom.getExits():
					self.graph[end][_exit] = '?'
			self.graph[end][self.inverse[_next]] = start
			if len(self.queue) == 0:
				self.buildQueue()
		return self.traversal

	def manualTest(self):
		self.reset()
		self.player.currentRoom.printRoomDescription()
		while True:
			cmds = input("-> ").lower().split(" ")
			if cmds[0] in ["n", "s", "e", "w"]:
				self.player.travel(cmds[0], True)
			else:
				print("I did not understand that command.")

	def reset(self, initial = False):
		self.resetStorage()
		if not initial:
			self.player.currentRoom = self.world.startingRoom
		self.resetGraph()
		self.buildQueue()

	def resetStorage(self):
		self.queue = Queue()
		self.traversal = []

	def resetGraph(self):
		room = self.player.currentRoom
		self.graph = {room.id: {}}
		for _exit in room.getExits():
			self.graph[room.id][_exit] = '?'
