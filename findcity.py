import math

# Hays does not exist 
# Salina has a capitalization issue

# add edge in both directions
def add_edge(first_city, second_city, distance):
    if first_city not in city_adj:
        city_adj[first_city] = {}
    city_adj[first_city][second_city] = distance
    
    if second_city not in city_adj:
        city_adj[second_city] = {}
    city_adj[second_city][first_city] = distance

# read city coordinates from txt
city_coords = {}
with open("coordinates.txt") as f:
    for line in f:
        city, lat, lon = line.strip().split()
        city_coords[city] = (float(lat), float(lon))

# calculate distance between two cities using Pythagorean theorem
def distance(first_city, second_city):
    lat1, lon1 = city_coords[first_city]
    lat2, lon2 = city_coords[second_city]
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    return math.sqrt(dlat**2 + dlon**2)

# read city adjacencies from txt
city_adj = {}
with open("adjacencies.txt") as f:
    for line in f:
        cities = line.strip().split()
        first_city = cities[0]
        for second_city in cities[1:]:
            # add edge in both directions
            try:
                add_edge(first_city, second_city, distance(first_city, second_city))
            except KeyError:
                print("City not found: " + first_city + " or " + second_city)
                print("This may be an issue with the naming conventions of your information txt")

# A* search algorithm
def a_star(start, goal):
    #cost and the city
    paths = [(0, start)] 
    #keep track where you are at
    arrived_from = {}
    #collect cost
    accumulated_cost = {start: 0}
    while paths:
        #find minimum cost
        current_cost, current_city = min(paths, key=lambda x: x[0])
        if current_city == goal:
            #remake path
            path = [current_city]
            while current_city != start:
                current_city = arrived_from[current_city]
                path.append(current_city)
            path.reverse()
            return path
        #check adjacencies
        for neighbor in city_adj[current_city]:
            new_cost = accumulated_cost[current_city] + distance(current_city, neighbor)
            if neighbor not in accumulated_cost or new_cost < accumulated_cost[neighbor]:
                accumulated_cost[neighbor] = new_cost
                priority = new_cost + distance(neighbor, goal)
                paths.append((priority, neighbor))
                arrived_from[neighbor] = current_city
        #remove checked city
        paths.remove((current_cost, current_city)) 
    return None

# prompt user for start and goal cities 
# enabling for python 2 and 3
python_two = False
try:
    start = input("Enter start city: ")
except NameError:
    print("Looks like you are using python 2, please try again and python 2 will run\n")
    python_two = True
    start = raw_input("Enter start city: ")

#non-existent city given retry
while start not in city_coords:
    print("City not found. Please try again.")
    if python_two == False:
        start = input("Enter start city: ")
    else:
        start = raw_input("Enter start city: ")

if python_two == False:
    goal = input("Enter goal city: ")
else:
    goal = raw_input("Enter goal city: ")

#non-existent city given retry
while goal not in city_coords:
    print("City not found. Please try again.")
    if python_two == False:
        goal = input("Enter goal city: ")
    else:
        goal = raw_input("Enter goal city: ")

# find shortest path using A* search algorithm
path = a_star(start, goal)
if path:
    with open("directions.txt", "w") as f:
        print("A file has been added/edited named directions.txt \n")
        if len(path) == 2:
            print("These cities are next door to eachother")
            f.write("These cities are next door to eachother")
        print("Shortest path:")
        f.write("Shortest path:\n")
        for i, city in enumerate(path):
            f.write(city + "\n")
            print(city)
            if i < len(path) - 1:
                print(" -> distance:", distance(city, path[i+1]))
                f.write(" -> distance: " + str(distance(city, path[i+1])) + "\n")
else:
    print("No path found.")
