import pacman
import autograder

"""
run.py runs things that look like command-line arguments
for Berkeley Python. Leave the 'python pacman.py' part
at the beginning, just like running from the command line.

You should comment out all lines in the file except the one
you wan to run!
"""

# pacman.main('python pacman.py --layout tinyMaze --pacman GoWestAgent')
# pacman.main('python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch')
# pacman.main('python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs')
# pacman.main('python pacman.py -l smallMaze -p SearchAgent -a fn=dfs')


# autograder.run('python autograder.py')
# autograder.run('python autograder -q q5')
# autograder.run('python autograder.py -t test_cases/q2/graph_bfs_vs_dfs')

# pacman.main('python pacman.py -l trickySearch -p AStarFoodSearchAgent')
# pacman.main('python pacman.py -l bigCorners -z .5 -p SearchAgent -a fn=astar,heuristic=chebyshevHeuristic')
# pacman.main('python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic')

pacman.main('python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem')