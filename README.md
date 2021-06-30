## ASSIGNMENT 1 REPORT
###### Course: Elements of AI(SP21-BL-CSCI-B551-37653)
###### CS B551 - Assignment 1: Searching
###### Name: Bharath Kumar Maturi, Jonathan Satish Tirupuranthakam, Tarika Sadey
###### UserName: bkmaturi-josatiru-tsadey
###### GIT repo: bkmaturi-josatiru-tsadey-a1

---------------------------------------------------------------------------- 
### PART 1: THE 2021 PUZZLE

Problem given to us is to obtain goal state from the given state using the pre-defined rotations like particular 
row/column can rotate only in particular direction.

Pre-defined rotations given to us are:
* 1st and 3rd rows can rotate only in LEFT direction
* 2nd and 4th rows can rotate only in RIGHT direction
* 1st, 3rd and 5th columns can rotate only in UP direction
* 2nd and 4th columns can rotate only in DOWN direction

#### Problem statement
* Here, input will be given in form of 1-D array with 20 elements. We divided this into 4X5 2-D array with 4-Rows and 
  5-Columns. 
  
* Using the pre-defined rotations, our goal is to obtain goal state which is 
  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]. 

#### Successor function
* Here, we have implemented a successor function which takes current state as input and gives all possible next states 
  as output. 
  
* In the successor function, we have used in-built python rotate function to rotate the particular row/column in particular 
  direction. 
  
* We appended the rotation direction of child node along with the state while storing the successors, to provide the 
  output path if goal state is obtained.

#### Heuristic function
* Here, we have used cost evaluation function f(s) = h(s)+g(s) where h(s)-cost from current state to goal state 
  and g(s) is cost from initial state to current state.
  
* The heuristic(h(s)) we used in this problem is calculating the misplaced tiles at each state.
  g(s) is number of steps it to obtain from initial state to current state. 

* Here, misplaced tiles is admissible because it's value reduce everytime when we move to next state. 
  If we consider the manhattan distance as heuristic, it fails to be admissible for edge column values.
  (For the last column values, even though we can reach its goal position by one rotation.... manhattan distance will be 
  four instead of  one)


#### A brief description of how our search algorithm works:

* Here, our algorithm will take initial/given state as input. 
  
* We have created a fringe(Priority Queue) which will pop the priority element first. 
  
* Popped out element from fringe have 4 parameters. (cost evaluation value(h+g), current state, Direction to reach 
  current state, value of g)
  
* While fringe is not empty, will iterate through the elements in fringe and will check if goal state is obtained. 
  
* If it reached goal state, we will terminate the code and return the path/directions to reach goal state from initial 
  state. 
  
* Else, algorithm will find the successor states of current state using the successor function implemented and it will 
  append them to fringe.

#### Discussion of any problems faced, simplifications, and/or design decisions made.

* At the start, we have tried many heuristic functions like manhattan distance, Inversion count, Manhattan+Linear conflict. 

* But we got either wrong output or the program went in to infinite loop. 

* Also, we struggled with the successor function like how to rotate only one row/column and also in storing the path/direction.

* In the solver function, input is giving in form of tuple but we converted that data type into list for our operations 
  and simplicity. 

********-------------------------------------********

### PART 2: ROAD TRIP!

#### Design

* As traversing through the huge network of cities in US map is hard the traditional methods of Breadth First Search(BFS) 
  and Depth First Search(DFS) takes huge amount of time for planning out the route so, we come across the better version 
  by calculating the heuristic value and using A* Search.

* The state space in this case will be all possible routes from the source to destination.

* The successor function in this case will be the function which returns the intermediate cities of source city before 
  reaching destination and also which returns destination city.

* The edge weights are considered in the format g(s), the value of g(s) will be same to all the nodes on same level and 
  gets incremented by 1 after travelling to next node.

* The goal state will be the destination city.

* The heuristic value h(s) will be depending on the heuristic chosen in our case there are four heuristic functions
  (number of segments, number of miles, time taken and the probability of accident). In this case all the four heuristics 
  are admissible as the values are predefined in question itself and the values are never overestimated and are fixed.
  
#### Program Description

* The first step is loading road segments and we stored in a dictionary of dictionary format for easy access where the 
  first key is the start_city and the second key is end_city which consists of the values number of miles, speed limit 
  and the highway name

* After that we load the co-ordinates of the cities.

* We have four types of cost function number of segments, distance, time and safety so we wrote a function which returns 
  the cost value depending on the input we give.

* For calculating the distance between we the two cities we considered Euclidean method.

* Now for getting the route we defined an empty fringe and inserted initial state which has priority index value which 
  was calculated depending on the heuristic considered, route which is start_city, number of miles which is 0, number 
  of segments which is 0, number of accidents which is 0 and time taken which will be zero initially.

* So depending on the sum of heuristic value and cost function(g) and the destination that user has to go, the fringe gets 
  popped out of the priority queue and then the successor states get added to fringe and finally when we pop out the 
  destination from the fringe we will terminate the program and then return the output in the required format.

#### Problem Faced.
* Initially when we tried to import data from raw data files, we faced lot of difficulty on which data structure can give 
  us better results like whether to use dictionary or 2D-array or other.
* Among the 4 heuristic parameters given(time, segments, distance, safety), calculating segments took more efforts from 
  us compared to other three. 

********-------------------------------------********

### PART 3: CHOOSING TEAMS
* The problem poses a search optimization technique to assign students into groups according to their preferences and 
  raise complaints if there occurs an assignment error.
  
* Our goal is to assign students into groups that would minimize the total number of complaints raised by students.

#### Search Abstraction : 
The search abstraction used in solving this problem is defined below
* The state space in this case will consist of all the possible teams that can be formed along with their assignment 
  cost(number of complaints raised).
  
* Initial State : We considered the initial state to be the teams formed according to the given preference listed by 
  the students after deleting the 'zzz' values from the list.
  
* Successor States (Function) : Our successor function will return assigned teams by randomly choosing students from the 
  previously generated list and creates a successor teams.
  
* Goal State : Our goal is to form teams such that the assigned cost will be as minimum as possible.
  
* Heuristic h(s) : the heuristic in this case is the calculation of the total assignment cost(number of complaints raised)
  considering the following scenarios 
  * If there is a difference between the group size that a student requested and the group size that the student got 
    placed in then a complaint is raised.
  * If a student is not assigned to a team as requested in his preference list then a complaint is raised for each 
    different team member assigned to him. 
  * If a student is assigned to a group from their non-preference list then two complaint emails are raised.

#### Overview of the solution (assign.py):
* The solver function takes input file consisting of a list of student data with their preference,non-preference team 
  members and team size which is stored into a default dictionary.
  
* We used priority queue to implement the search algorithm (A* search) with heuristic as the assigned cost value of the 
  teams formed and the successor function will generate alternative possible teams given the current formed teams.
  
* The fringe will pop the teams having low cost(high priority) and check for it being a is_goal state function and 
  yield the results.
  
* The calculate_assigned_cost method will return the total cost value of the assigned teams based on the conditions 
  defined in the above heuristic function.
  
* Valid state function will return a first initial state for appending into the fringe.

* Is_goal method will validate whether all the students are assigned into teams or not.

* The yield will provide outputs whenever it will find minimum assigned cost than previous assigned cost generated until
  the time frame ends.
