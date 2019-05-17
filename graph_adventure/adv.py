from maze import Maze, roomGraph

maze = Maze('P1')
# Takes best path out of number passed into range plus one.
traversalPath = maze.traverse()
for _ in range(10):
	tempPath = maze.traverse()
	if len(tempPath) < len(traversalPath):
		traversalPath = tempPath

# TRAVERSAL TEST
visited_rooms = set()
maze.player.currentRoom = maze.world.startingRoom
visited_rooms.add(maze.player.currentRoom)
for move in traversalPath:
	maze.player.travel(move)
	visited_rooms.add(maze.player.currentRoom)

print()
if len(visited_rooms) == len(roomGraph):
	print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
	print("TESTS FAILED: INCOMPLETE TRAVERSAL")
	print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")
print()

# UNCOMMENT BELOW LINE TO WALK AROUND
# maze.manualTest()
