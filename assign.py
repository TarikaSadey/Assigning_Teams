#!/usr/local/bin/python3
# assign.py : Assign people to teams
#
# Code by: bkmaturi-josatiru-tsadey
#
# Based on skeleton code by R. Shah and D. Crandall, January 2021
#

import sys
from time import *
import numpy as np
import random
import copy
from queue import PriorityQueue
from pandas._libs.internals import defaultdict


# To calculate cost of each assigned team based on validation
def calculate_assigned_cost(group_listed, data):
    user_cost = 0
    g_cost = 0
    t_cost = 0

    # To find cost of teams formed
    for user in group_listed:
        pref1 = data[user][0]
        grp_length = data[user][1]
        npref1 = data[user][2]
        # Preference list validation
        for pref in pref1:
            if (pref not in group_listed) and (pref != 'zzz'):
                user_cost += 1
        # Team length validation
        if grp_length != len(group_listed):
            user_cost += 1
        # Non_preference group members validation
        for npref in npref1:
            if npref in group_listed:
                user_cost += 2
        g_cost += user_cost
    t_cost += g_cost
    return t_cost


# To find initial valid state from the preference group list
def valid_state(data):
    # Assign cost for each team and add into the dictionary
    for user in data:
        pref = data[user][0]
        group = [ele for ele in pref if ele != 'zzz']
        data[user][3] = calculate_assigned_cost(group, data)

    available_users = []
    # Users available to assign to groups
    for i in data:
        available_users.append(i)
    # Sort dictionary based on cost variable
    data_update = {k: v for k, v in sorted(data.items(), key=lambda item: item[1][3])}
    start_state = []

    # Assigning teams based on available list of users and do not have any conflict
    for user1 in data_update:
        for group1 in data_update[user1][0]:
            list(group1).sort()
            if all(member in available_users for member in group1):
                for members in group1:
                    if members in available_users:
                        available_users.remove(members)
                start_state.append(group1)

    # Append remaining list of users in groups of three
    tmp_list = [available_users[x:x + 3] for x in range(0, len(available_users), 3)]
    for group2 in tmp_list:
        start_state.append(group2)

    return start_state


# Generate successor states from the given state
def successor(state, data):
    user_list = []
    for user in data:
        user_list.append(user)
    # Select user randomly to form random teams
    user = random.choice(user_list)
    next_team = []

    # Form teams by not exceeding the limit of group length 3
    for i in range(len(state)):
        state_1 = copy.deepcopy(state)
        flag = 'N'
        list = []

        for j in range(len(state_1)):
            list.append([j, state_1[j]])

        for k in range(len(list)):
            j = list[k][0]
            team = list[k][1]

            if user in team:
                team.remove(user)
                if len(team) == 0:
                    state_1.remove(team)
                if i == j:
                    state_1.append([user])
                    flag = 'Y'
                    break
            elif len(team) <= 2 and i == j:
                team.append(user)
                flag = 'Y'
        if flag == 'Y':
            next_team.append(state_1)
    return next_team


# To check whether the goal state has been reached and whether all the users are assigned to groups
def is_goal(state, user_list):
    assigned_users = []
    for groups in state:
        for user in groups:
            assigned_users.append(user)

    for user in user_list:
        if user not in assigned_users:
            return False
    return True

    """
    1. This function should take the name of a .txt input file in the format indicated in the assignment.
    2. It should return a dictionary with the following keys:
        - "assigned-groups" : a list of groups assigned by the program, each consisting of usernames separated by hyphens
        - "total-cost" : total cost (number of complaints) in the group assignment
    3. Do not add any extra parameters to the solver() function, or it will break our grading and testing code.
    4. Please do not use any global variables, as it may cause the testing code to fail.
    5. To handle the fact that some problems may take longer than others, and you don't know ahead of time how
       much time it will take to find the best solution, you can compute a series of solutions and then
       call "yield" to return that preliminary solution. Your program can continue yielding multiple times;
       our test program will take the last answer you 'yielded' once time expired.
    """


def solver(input_file):
    # Read file into a default dictionary
    file = open(input_file, "r")
    data = defaultdict(list)
    user_list = []
    cost = 0
    new_cost = 0
    for line in file:
        if line != "\n":
            ele = line.strip().split(" ")
            user = ele[0]
            group_size = len(ele[1].split('-'))
            pref = ele[1].split('-')
            npref = ele[2].split(',')
            data[user].append(pref)
            data[user].append(group_size)
            data[user].append(npref)
            data[user].append(cost)
            if user not in user_list:
                user_list.append(user)

    # Calculate initial cost
    for state in valid_state(data):
        new_cost1 = calculate_assigned_cost(state, data)
        new_cost += new_cost1

    # Form successor states for initial state
    successor_states = successor(valid_state(data), data)

    minimum_cost = float("inf")
    #time_break = time() + 120
    
    # Pop successor states from the fringe based on priority(assigned_cost) and yield their result if goal state is 
    # reached
    while True:
        old_cost = new_cost + 1
        fringe = PriorityQueue()
        g = 0

        while new_cost < old_cost:
            old_cost = new_cost
            cost_new1 = 0
            for states in successor_states:
                for state in states:
                    cost_new = calculate_assigned_cost(state, data)
                    cost_new1 += cost_new
                fringe.put((cost_new1 + g, states))

            g += 0
            a = fringe.get()
            new_cost = a[0]
            min_cost_state = a[1]

            successor_states = successor(min_cost_state, data)

            # yeild result of lower assigned cost teams and provide output
            if new_cost < minimum_cost:
                best_group = ["-".join(i) for i in min_cost_state]
                minimum_cost = new_cost
                yield ({"assigned-groups": best_group,
                        "total-cost": minimum_cost})

        #if time_break < time():
        #    break


if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected an input filename"))

    for result in solver(sys.argv[1]):
        print("----- Latest solution:\n" + "\n".join(result["assigned-groups"]))
        print("\nAssignment cost: %d \n" % result["total-cost"])
    
