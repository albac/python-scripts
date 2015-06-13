#Soduko validator by albac

def check_duplicates(soduko_set):
    return len(soduko_set) == len(set(soduko_set))
def check_horizontal(matrix):
    horizontal=[]
    temp={}
    for i in range(0,9):
        temp = matrix[i]
        for a in temp:
            horizontal.append(temp[a])
        #print horizontal
        if not check_duplicates(horizontal):
            return False
        horizontal=[]
        temp={}
    return True

def check_vertical(matrix):
    vertical=[]
    temp={}
    for a in range(0,9):
        for x in matrix:
            temp=matrix[x]
            #print temp[a]
            vertical.append(temp[a])
        #print vertical
        if not check_duplicates(vertical):
            return False
        vertical=[]
        temp={}
    return True

def get_box(i,j,x,y,matrix):
    box=[]
    temp={}
    for a in range(i,j):
        temp=matrix[a]
        for b in range(x,y):
            box.append(temp[b])
    #print box
    return box


def check_box(matrix):
    if not check_duplicates(get_box(0,3,0,3,matrix)):
        return False
    if not check_duplicates(get_box(0,3,3,6,matrix)):
        return False
    if not check_duplicates(get_box(0,3,6,9,matrix)):
        return False
    if not check_duplicates(get_box(3,6,0,3,matrix)):
        return False
    if not check_duplicates(get_box(3,6,3,6,matrix)):
        return False
    if not check_duplicates(get_box(3,6,6,9,matrix)):
        return False
    if not check_duplicates(get_box(6,9,0,3,matrix)):
        return False
    if not check_duplicates(get_box(6,9,3,6,matrix)):
        return False
    if not check_duplicates(get_box(6,9,6,9,matrix)):
        return False
    return True

def get_matrix(grid):
    grid_array=list(grid)
    temp={}
    matrix={}
    c=0
    for i in range(0,9):
        for j in range(0,9):
            x = j + c
            temp[j] = grid_array[x]
        matrix[i] = temp
        temp={}
        c = c + 9
    return matrix

def is_valid_solution(grid):
    if not grid.isdigit():
        print "Is not digit"
        return False
    initial_matrix=get_matrix(grid)
    if not check_horizontal(initial_matrix):
        return False
    if not check_vertical(initial_matrix):
        return False
    if not check_box(initial_matrix):
        return False
    return True

#grid="124567389213456789456123789134567289213456789456123789134567289213456789456123789"
grid="835416927296857431417293658569134782123678549748529163652781394981345276374962815"

if is_valid_solution(grid):
    print "Is valid"
else:
    print "No valid"

