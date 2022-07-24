from typing import List
from test_cases import test_cases

class Project:
    def __init__(self, index: int, value: int) -> None:
        self.index = index
        self.value = value
        self.required_project = None

def sort_project(projects: List[Project]):
    # Outer loop to traverse on len(projects) 
    for i in range(1, len(projects)): 

        prj = projects[i] 

        # Move elements of projects[0 to i-1],
        # which are smaller to one position
        # ahead of their current position 
        j = i - 1 
        
        while j >= 0 and prj.value > projects[j].value: 
            projects[j + 1] = projects[j] 
            j -= 1 
                
        projects[j + 1] = prj 
            
    return projects 

def do_project(project: Project, sum_value: int, count: int):
    if project.required_project == None:
        sum_value += project.value
        count += 1
        print('sum: ', sum_value)
        print('count: ', count)
    else:
        sum_value, count = do_project(project.required_project, sum_value, count)
        if count < 2:
            sum_value += project.value
            count += 1
            print('sum: ', sum_value)
            print('count: ', count)

    return sum_value, count

def solution(V, A, B):
    projects = [Project(index, value) for index, value in enumerate(V)]

    # Update the required projects
    for req in range(len(B)):
        projects[B[req]].required_project = projects[A[req]]

    sort_project(projects)
    print('sorted projects: ', [prj.__dict__ for prj in projects])

    sum_value = 0
    count = 0
    for prj in projects:
        sum_value, count = do_project(prj, sum_value, count)
        if count == 2:
            break
    
    return sum_value

if __name__ == '__main__':
    for test_case in test_cases:
        print('test case: ', test_case, '\nsolution: ', solution(*test_case))