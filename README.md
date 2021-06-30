
### CHOOSING TEAMS
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
