import util
class SearchProblem:
    def getStartState(self):
        
        util.raiseNotDefined()

    def isGoalState(self, state):
        
        util.raiseNotDefined()

    def getSuccessors(self, state):
        
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        
        util.raiseNotDefined()

def depthFirstSearch(problem):    
    from util import Stack
    open_list = Stack()

    visited_list = []
    path = []

    start_position = problem.getStartState()

    open_list.push((start_position, path))

    while not open_list.isEmpty():

        current_node = open_list.pop()
        position = current_node[0]
        path = current_node[1]

        if position not in visited_list:
            visited_list.append(position)

        if problem.isGoalState(position):
            return path

        successors = problem.getSuccessors(position)

        for item in successors:
            if item[0] not in visited_list:

                new_position = item[0]
                new_path = path + [item[1]]
                open_list.push((new_position, new_path, item[2]))

    util.raiseNotDefined()


def uniformCostSearch(problem):

    from util import PriorityQueue

    open_list = PriorityQueue()

    visited_list = []
    path = []
    priority = 0

    start_position = problem.getStartState()

    open_list.push((start_position, path), priority)

    while not open_list.isEmpty():

        current_node = open_list.pop()
        position = current_node[0]
        path = current_node[1]

        if position not in visited_list:
            visited_list.append(position)

        if problem.isGoalState(position):
            return path

        successors = problem.getSuccessors(position)

        def getPriorityOfNode(priority_queue, node):
            for item in priority_queue.heap:
                if item[2][0] == node:
                    return problem.getCostOfActions(item[2][1])

        for item in successors:
            if item[0] not in visited_list and (item[0] not in (node[2][0] for node in open_list.heap)):
                new_path = path + [item[1]]
                new_priority = problem.getCostOfActions(new_path)
                open_list.push((item[0], new_path), new_priority)

            elif item[0] not in visited_list and (item[0] in (node[2][0] for node in open_list.heap)):
                old_priority = getPriorityOfNode(open_list, item[0])
                new_priority = problem.getCostOfActions(new_path)

                if old_priority > new_priority:
                    new_path = path + [item[1]]
                    open_list.update((item[0], new_path), new_priority)

    util.raiseNotDefined()

# Abbreviations

dfs= depthFirstSearch
ucs = uniformCostSearch