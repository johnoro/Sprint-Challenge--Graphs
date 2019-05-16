from room import Room
from player import Player
from world import World
from roomGraphs import smallest as roomGraph
from queue import Queue

import random

# Load world
world = World()

world.loadGraph(roomGraph)
world.printRooms()
player = Player("Name", world.startingRoom)


# FILL THIS IN
queue = Queue(['n'])
visited = set()
while len(queue) > 0:
    path = queue.dequeue()
    v = path[-1]
    if v == '?':
        break
    if v not in visited:
        visited.add(v)
        for sv in self.vertices[v]:
            if sv not in visited:
                queue.enqueue(path + [sv])
print(path)
traversalPath = path


# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)
for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == len(roomGraph):
    print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")
