from collections import deque
from typing import Dict, List
def bfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph.get(node, []))
    return visited
  
if __name__ == "__main__":
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6],
        4: [],
        5: [6],
        6: []
    }
    print(bfs(graph, 1))
