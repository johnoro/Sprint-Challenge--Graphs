from oppositeDirs import opposite

class Room:
	def __init__(self, name, description, _id=0, x=None, y=None):
		self.id = _id
		self.name = name
		self.description = description
		self.n_to = None
		self.s_to = None
		self.e_to = None
		self.w_to = None
		self.x = x
		self.y = y
	
	def __str__(self):
		return f"\n-------------------\n\n{self.name}\n\n   {self.description}\n\n{self.getExitsString()}\n"
	
	def printRoomDescription(self):
		print(str(self))
	
	def getDir(self, d):
		return getattr(self, f'{d}_to')
	
	def setDir(self, d, room):
		setattr(self, f'{d}_to', room)

	def getExits(self):
		exits = []
		for d in 'nswe':
			if self.getDir(d) is not None:
				exits.append(d)
		return exits
	
	def getExitsString(self):
		return f"Exits: [{', '.join(self.getExits())}]"
	
	def connectRooms(self, direction, connectingRoom):
		if direction in 'nsew':
			self.setDir(direction, connectingRoom)
			connectingRoom.setDir(opposite[direction], self)
		else:
			print("INVALID ROOM CONNECTION")
	
	def getRoomInDirection(self, direction):
		if direction in 'nsew':
			return self.getDir(direction)
		else:
			return None
	
	def getCoords(self):
		return [self.x, self.y]
