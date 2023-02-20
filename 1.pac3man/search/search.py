# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    # 0 - location, 1 - path, 2 - cost
    stack = util.Stack()  # frontiera
    visited = []  # explorat
    current = (problem.getStartState(), [])  # nod curent (start)
    stack.push(current)

    while not stack.isEmpty():  # cat timp stiva nu e goala
        current = stack.pop()  # dam jos de pe stiva nodul curent

        if problem.isGoalState(current[0]):  # daca indeplinim misiunea, returnam path-ul
            return current[1]

        if current[0] not in visited:
            visited.append(current[0])  # vizitam
            for successor in problem.getSuccessors(current[0]):  # pentru fiecare miscare legala
                if successor[0] not in visited:  # daca pozitie legala nu e vizitata
                    path = current[1] + [successor[1]]
                    stack.push([successor[0], path])  # incarcam pe stiva


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # 0 - location, 1 - path, 2 - cost
    queue = util.Queue()  # frontiera
    visited = []  # explorat
    current = (problem.getStartState(), [])  # nod curent (start)
    queue.push(current)

    while not queue.isEmpty():  # cat timp stiva nu e goala
        current = queue.pop()  # dam jos de pe stiva nodul curent

        if problem.isGoalState(current[0]):  # daca indeplinim misiunea, returnam path-ul
            return current[1]

        if current[0] not in visited:
            visited.append(current[0])  # vizitam
            for successor in problem.getSuccessors(current[0]):  # pentru fiecare miscare legala
                if successor[0] not in visited:  # daca pozitie legala nu e vizitata
                    path = current[1] + [successor[1]]
                    queue.push([successor[0], path])  # incarcam pe stiva


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # 0 - location, 1 - path, 2 - cost
    queue = util.PriorityQueue()  # frontiera
    visited = []  # explorat
    current = (problem.getStartState(), [], 0)  # nod curent (start)
    queue.push(current, 0)

    while not queue.isEmpty():  # cat timp stiva nu e goala
        current = queue.pop()  # dam jos de pe stiva nodul curent

        if problem.isGoalState(current[0]):  # daca indeplinim misiunea, returnam path-ul
            return current[1]

        if current[0] not in visited:
            visited.append(current[0])  # vizitam
            for successor in problem.getSuccessors(current[0]):  # pentru fiecare miscare legala
                if successor[0] not in visited:  # daca pozitie legala nu e vizitata
                    path = current[1] + [successor[1]]
                    cost = current[2] + successor[2]
                    queue.push((successor[0], path, cost), cost)  # incarcam pe stiva


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(position, problem, info={}):
    "The Manhattan distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.goal
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])


def euclideanHeuristic(position, problem, info={}):
    "The Euclidean distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.goal
    return ((xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2) ** 0.5


def chebyshevHeuristic(position, problem, info={}):
    "The Chebyshev distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.goal
    return max(abs(xy1[0] - xy2[0]), abs(xy1[1] - xy2[1]))


def reverseChebyshevHeuristic(position, problem, info={}):
    "The Reverse Chebyshev distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.goal
    return min(abs(xy1[0] - xy2[0]), abs(xy1[1] - xy2[1]))


def aStarSearch(problem, heuristic=nullHeuristic):  # cu ponderi
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # 0 - location, 1 - path, 2 - cost
    queue = util.PriorityQueue()  # frontiera
    visited = []  # explorat
    current = (problem.getStartState(), [], 0)  # nod curent (start)
    queue.push(current, 0)

    while not queue.isEmpty():  # cat timp stiva nu e goala
        current = queue.pop()  # dam jos de pe stiva nodul curent

        if problem.isGoalState(current[0]):  # daca indeplinim misiunea, returnam path-ul
            return current[1]

        if current[0] not in visited:
            visited.append(current[0])  # vizitam
            for successor in problem.getSuccessors(current[0]):  # pentru fiecare miscare legala
                if successor[0] not in visited:  # daca pozitie legala nu e vizitata
                    path = current[1] + [successor[1]]
                    cost = current[2] + successor[2]
                    totalCost = 0.3 * cost + 0.7 * heuristic(successor[0], problem)
                    queue.push((successor[0], path, cost), totalCost)  # incarcam pe stiva


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
