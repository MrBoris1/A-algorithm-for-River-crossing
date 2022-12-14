from copy import deepcopy

POSSIBLE_ACTIONS = [[1,1,0,0,0,0,0,0], [1,0,1,0,0,0,0,0],[1,0,0,1,0,0,0,0], [0,1,0,0,1,0,0,0],[0,1,0,0,0,1,0,0], [0,0,1,0,0,0,1,0],[0,0,0,1,0,0,1,0],[0,0,0,0,1,0,1,0], [0,0,0,0,0,1,1,0],[0,0,0,0,0,0,1,1],[1,0,0,0,0,0,0,0], [0,1,0,0,0,0,0,0], [0,0,0,0,0,0,1,0]]


class State():

    def __init__(self, left, boat, right,h,g):
        self.left = left;
        self.boat = boat;
        self.right = right;
        self.prev = None
        self.h=h
        self.g=g

    def get_right(self):
        return self.right

    def get_h(self):
        return self.h

    def __str__(self):
        return ("({},{},{},{},{},{},{},{}) - ({},{},{},{},{},{},{},{}) - {}".format(self.left[0], self.left[1],self.left[2],self.left[3],self.left[4],self.left[5],self.left[6],self.left[7], self.right[0], self.right[1],
                                                            self.right[2],self.right[3],self.right[4],self.right[5],self.right[6],self.right[7],self.boat))

    def isValidState(self):

        if (self.left[0]==1 and self.left[1]==0 and (self.left[4]>0 or self.left[5]>0)) or (self.right[0]==1 and self.right[1]==0 and (self.right[4]>0 or self.right[5]>0)):
            return False
        if (self.left[1]==1 and self.left[0]==0 and (self.left[2]>0 or self.left[3]>0)) or (self.right[1]==1 and self.right[0]==0 and (self.right[2]>0 or self.right[3]>0)):
            return False
        if (self.left[-1]==1 and self.left[6]==0 and (self.left[3]>0 or self.left[2]>0 or self.left[1]>0 or self.left[0]>0 or self.left[4]>0 or self.left[5]>0 )) or \
                (self.right[-1]==1 and self.right[6]==0 and (self.right[3]>0 or self.right[2]>0 or self.right[1]>0 or self.right[0]>0 or self.right[4]>0 or self.right[5]>0)):
            return False
        if self.left[-1]>1 or self.right[-1]>1 or self.left[0]>1 or self.right[0]>1 or self.left[1]>1 or self.right[1]>1 or self.left[2]>1 \
                or self.right[2]>1 or self.left[3]>1 or self.right[3]>1 or self.left[4]>1 or self.right[4]>1 or self.right[5]>1 or self.left[5]>1 or self.right[6]>1 or self.left[6]>1 :
            return False
        return True

    def __eq__(self, other):
        return (self.left[0] == other.left[0] and self.left[1] == other.left[1] and self.right[0] == other.right[0] and
                self.right[1] == other.right[1] and self.boat == other.boat and self.left[2] == other.left[2] and self.left[3] == other.left[3] and self.left[4] == other.left[4] and self.left[5] == other.left[5]
                and self.right[2] == other.right[2] and self.right[3] == other.right[3] and self.right[4] == other.right[4] and self.right[5] == other.right[5] and self.right[6] == other.right[6] and self.right[7] == other.right[7])

    def __hash__(self):
        return hash((self.left[0], self.left[1], self.boat, self.right[0], self.right[1]))

    def isGoalState(self):
        return (self.left[0] == 0 and self.left[1] == 0 and self.left[2] == 0 and self.left[3] == 0 and self.left[4] == 0 and self.left[5] == 0 and self.left[6] == 0 and self.left[7] == 0)

def nextStates(current):
    nodes = []

    for action in POSSIBLE_ACTIONS:

        nextState = deepcopy(current)
        nextState.prev = current

        # boat will be on the opposite side
        nextState.boat = 1 - current.boat

        # Moving from left to right
        if (current.boat == 0):
            if action == [1, 1, 0, 0, 0, 0, 0, 0]:
                nextState.right[0] += action[0]
                nextState.right[1] += action[1]
                nextState.left[0] -= action[0]
                nextState.left[1] -= action[1]
            if action == [1,0,1,0,0,0,0,0]:
                nextState.right[0] += action[0]
                nextState.right[2] += action[2]
                nextState.left[0] -= action[0]
                nextState.left[2] -= action[2]
            if action == [1,0,0,1,0,0,0,0]:
                nextState.right[0] += action[0]
                nextState.right[3] += action[3]
                nextState.left[0] -= action[0]
                nextState.left[3] -= action[3]
            if action == [0,1,0,0,1,0,0,0]:
                nextState.right[1] += action[1]
                nextState.right[4] += action[4]
                nextState.left[1] -= action[1]
                nextState.left[4] -= action[4]
            if action == [0,1,0,0,0,1,0,0]:
                nextState.right[1] += action[1]
                nextState.right[5] += action[5]
                nextState.left[1] -= action[1]
                nextState.left[5] -= action[5]
            if action ==  [0,0,1,0,0,0,1,0]:
                nextState.right[2] += action[2]
                nextState.right[6] += action[6]
                nextState.left[2] -= action[2]
                nextState.left[6] -= action[6]
            if action ==  [0,0,0,1,0,0,1,0]:
                nextState.right[3] += action[3]
                nextState.right[6] += action[6]
                nextState.left[3] -= action[3]
                nextState.left[6] -= action[6]
            if action ==  [0,0,0,0,1,0,1,0]:
                nextState.right[4] += action[4]
                nextState.right[6] += action[6]
                nextState.left[4] -= action[4]
                nextState.left[6] -= action[6]
            if action == [0, 0, 0, 0, 0, 1, 1, 0]:
                nextState.right[5] += action[5]
                nextState.right[6] += action[6]
                nextState.left[5] -= action[5]
                nextState.left[6] -= action[6]
            if action == [0, 0, 0, 0,0,0, 1, 1]:
                nextState.right[6] += action[6]
                nextState.right[-1] += action[-1]
                nextState.left[6] -= action[6]
                nextState.left[-1] -= action[-1]
            if action == [1, 0, 0, 0, 0, 0,0,0]:
                nextState.right[0] += action[0]
                nextState.left[0] -= action[0]
            if action == [0, 1, 0, 0, 0, 0,0,0]:
                nextState.right[1] += action[1]
                nextState.left[1] -= action[1]
            if action == [0, 0, 0, 0,0,0, 1, 0]:
                nextState.right[6] += action[6]
                nextState.left[6] -= action[6]

        # Moving from right to left
        elif (current.boat == 1):
            if action == [1, 1, 0, 0, 0, 0, 0, 0]:
                nextState.left[0] += action[0]
                nextState.left[1] += action[1]
                nextState.right[0] -= action[0]
                nextState.right[1] -= action[1]
            if action == [1, 0, 1, 0, 0, 0, 0, 0]:
                nextState.left[0] += action[0]
                nextState.left[2] += action[2]
                nextState.right[0] -= action[0]
                nextState.right[2] -= action[2]
            if action == [1, 0, 0, 1, 0, 0, 0, 0]:
                nextState.left[0] += action[0]
                nextState.left[3] += action[3]
                nextState.right[0] -= action[0]
                nextState.right[3] -= action[3]
            if action == [0, 1, 0, 0, 1, 0, 0, 0]:
                nextState.left[1] += action[1]
                nextState.left[4] += action[4]
                nextState.right[1] -= action[1]
                nextState.right[4] -= action[4]
            if action == [0, 1, 0, 0, 0, 1, 0, 0]:
                nextState.left[1] += action[1]
                nextState.left[5] += action[5]
                nextState.right[1] -= action[1]
                nextState.right[5] -= action[5]
            if action == [0, 0, 1, 0, 0, 0, 1, 0]:
                nextState.left[2] += action[2]
                nextState.left[6] += action[6]
                nextState.right[2] -= action[2]
                nextState.right[6] -= action[6]
            if action == [0, 0, 0, 1, 0, 0, 1, 0]:
                nextState.left[3] += action[3]
                nextState.left[6] += action[6]
                nextState.right[3] -= action[3]
                nextState.right[6] -= action[6]
            if action == [0, 0, 0, 0, 1, 0, 1, 0]:
                nextState.left[4] += action[4]
                nextState.left[6] += action[6]
                nextState.right[4] -= action[4]
                nextState.right[6] -= action[6]
            if action == [0, 0, 0, 0, 0, 1, 1, 0]:
                nextState.left[5] += action[5]
                nextState.left[6] += action[6]
                nextState.right[5] -= action[5]
                nextState.right[6] -= action[6]
            if action == [0, 0, 0, 0, 0, 0, 1, 1]:
                nextState.left[6] += action[6]
                nextState.left[-1] += action[-1]
                nextState.right[6] -= action[6]
                nextState.right[-1] -= action[-1]
            if action == [1, 0, 0, 0, 0, 0, 0, 0]:
                nextState.left[0] += action[0]
                nextState.right[0] -= action[0]
            if action == [0, 1, 0, 0, 0, 0, 0, 0]:
                nextState.left[1] += action[1]
                nextState.right[1] -= action[1]
            if action == [0, 0, 0, 0, 0, 0, 1, 0]:
                nextState.left[6] += action[6]
                nextState.right[6] -= action[6]
        if nextState.isValidState():
            nodes.append(nextState)
    return nodes

def manhattan(h, child):
    total=0
    for i in child:
        total+=i
    return h-total

def current_move(lst):
    return len(lst)+1

def find_min(set,set2,lst=[],total=0):
    for i in set:
        total=manhattan(i.get_h(),i.get_right())+current_move(set2)
        lst.append(total)
    x=min(lst)
    for o in range(len(lst)):
        if lst[o] == x:
            return set[o]

def total(h,child,lst,total=0):
    total=current_move(lst)+manhattan(h,child)
    return total

def aStar(start,t,o):
    openset = list()
    closedset = set()
    current = start
    openset.append(current)
    while openset:
        # Find the item in the open set with the lowest G + H score
        current = find_min(openset,closedset)
        if current.isGoalState():
            return current
        openset.remove(current)
        closedset.add(current)
        for node in nextStates(current):
            if node in closedset:
                continue
            if node in openset:
                t+=1
                new_g = manhattan(node.get_h(),node.get_right()) + current_move(closedset)
                if node.G > new_g:
                    node.G = new_g
                    node.parent = current
            else:
                t+=1
                node.G = current_move(closedset) + 1
                node.H = manhattan(node.get_h(),node.get_right())
                # Set the parent to our current item
                node.parent = current
                openset.append(node)

def main():
    initial_state = State([1,1,1,1,1,1,1,1], 0, [0,0,0,0,0,0,0,0],8,0)
    state1=aStar(initial_state,0,0)

    # build path for A*
    path = []
    while state1:
        path.append(state1)
        state1 = state1.prev

    # reverse path
    path = path[::-1]

    # print state change
    for i in path:
        print(i)
    print("The order of the tuples are (M,F,D1,D2,S1,S2,P,T)")
    print('Everyone succesfully crossed!!!')

if __name__ == "__main__":
    main()