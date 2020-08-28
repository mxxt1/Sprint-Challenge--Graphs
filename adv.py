from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)



# Fill this out with directions to walk
# traversal_path = ['n', 'n']



#while the length of touched is <= the len of the graph, check if the current room is in set, if it's not then add it. add the room to cache and use get_exit to get possible movements. for each room add the movements to cache[room] go through each of the possible movements

# You may find the commands `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.

traversal_path = []
backtrack = {'e':'w','w':'e','n':'s','s':'n'}


cache = {}
touched = set()

moves_queue = []

#total rooms touched is less than the graph size
while len(touched) < len(room_graph):

#start with the first room via player.current_room.id
    room = player.current_room.id

#if not in the set add to touched with value of possible movements
    if room not in touched:
        touched.add(room)      
        cache[room] = player.current_room.get_exits()



#while there are possible moves to be made
    while len(cache[room]) >= 0:

        if len(cache[room]) > 0:
            # grab the first possible movement, remove from cache                                
            movement = cache[room].pop()

            #if it's not in the set, add it to the queue of moves and to the traversal path 
            if player.current_room.get_room_in_direction(movement).id not in touched:
                moves_queue.append(movement)

            #add the move to the trav path andn make the move to update current_room
                traversal_path.append(movement)
                player.travel(movement)                                        
                break

        # if there are no more moves to make, 
        elif len(cache[room]) == 0:

            # grab the last move and add it to the trav path and then move the player

            back = moves_queue.pop()
            
            
            traversal_path.append(backtrack[back])
            print(len(traversal_path))

            
            player.travel(backtrack[back])
            break







# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
