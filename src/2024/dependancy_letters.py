def find_order():
    lookup = {
        "A": [], # 1
        "B": [], # 1
        "C": ["A"], # 2
        "D": ["A", "B"], # 2
        "E": ["C", "D", "F"], # 3
        "F": ["B"] # 2
    }
    lst=[]
    visited = []
    from collections import deque
    queue = deque()
    for course, prereq in lookup.items():
        print(course, prereq)
        for child in prereq:
            if child not in visited:
                queue.append(child)

    def bfs():
        return
    
    
    return lst

find_order()
"""
A, B, C

    A   B   C   D   E   F
    B
"""

