To run the file

>python findcity.py

If there are city naming issues the error will output 
Then you will be asked to input a start city something like 

Enter start city: >Salina

This was tested in Python 2 and at the start if you use python 2 it will ask you to try again with raw_input instead of input, and remember that for the duration of the run

After you have inputed the correct start city it will then ask for goal city
Enter goal city: >Wichita 

For these start and goal examples with the provided coordinates.txt and Adjacencies.txt you should get a directions.txt file with this information
Shortest path:
Salina
 -> distance: 0.455124704678
McPherson
 -> distance: 0.42895119552
Newton
 -> distance: 0.403965310795
Wichita

If you would like to input your own test data simply edit the coordinates and Adjancencies txt with your own desired map addresses


Helpful Sources:

Artificial Intelligence Second Edition Stephen Lucci,Danny Kopec Pages 77-82 Hueristics 

Artificial Intelligence Second Edition Stephen Lucci,Danny Kopec Pages 86-87 Priority Queue

Artificial Intelligence Second Edition Stephen Lucci,Danny Kopec Page 99 A* search

Add_Edge function explanation http://projectpython.net/chapter18/

Class Prompt:
Given a list of cities and their adjacencies—from city A, what cities are next to it—can a route be found from city A to city X?
For this program, you’ll be implementing a heuristically guided search: Maintain a list of cities you know how to reach.
At the beginning, this will have one city—the origin. Cities adjacent to the origin are cities that you know how to reach; cities that you can reach, 
but have not yet visited (and so don’t yet know if they’re on the route) form the frontier. Which city on the frontier should you choose to visit next?
To make things a bit less complex for this problem, we’re going to go one step back and implement a best-first search, you’ll order the cities you can 
get to (but haven’t visited yet) by distance from your starting point. In the more efficient A* search, you choose the one that is closest, or estimated 
as closest, to your destination. If you’re trying to find a route from Kansas City to Denver, you’ll consistently head in a generally western direction 
if possible. If you’re partway there and hit a detour eastward, you’ll try to return to westward travel as soon as possible, and so on. From the new city 
you select, update the frontier, and re-assess which city on the frontier is closest to the destination. What if you hit a dead end? Suppose a particular 
city looks promising, but you get there and find there’s no route to your destination. In this case you will eventually exhaust the places you can get to 
from there, and the best- first heuristic will keep you from getting too far off course. Also, if the detour is getting too large, the algorithm will need 
to return to a different frontier city and try again from there. For each city visited, you will probably want to store where you came to that city from 
so the list can be used to reconstruct the path you’ve taken so far.
• Ask the user for their starting and ending towns, making sure they’re both towns in the database. Use either best-first or A* search to find a route to 
the destination, if one exists; print the route you find in order, from origin to destination. You might be interested in looking at a map and see how 
the route your program finds compares with reality. Note that your database is very limited, and I left out a lot of roads and routes. *Also, all we’re 
looking at is adjacency, not distance between adjacent cities. If you put into the database that Topeka is adjacent to Denver, it’s going to find a route 
between them very quickly, and say it’s ‘only’ one step. On the other hand, a real mapping application often gives directions such as “get onto I-70, and 
go west until you reach the I-225 exit at Aurora, Colorado.” It’s only one step, but it’s a large one.
