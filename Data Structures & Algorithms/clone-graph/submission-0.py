"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldToNew = {}

        def bfs(node):
            oldToNew[node] = Node(node.val)
            q = collections.deque([node])

            while q:
                curr = q.popleft()
                
                for neighbor in curr.neighbors:
                    # if node not in hashmap
                    if neighbor not in oldToNew:
                        oldToNew[neighbor] = Node(neighbor.val)
                        q.append(neighbor)

                    # connect cloned curr to cloned neighbor
                    oldToNew[curr].neighbors.append(oldToNew[neighbor])
            
        bfs(node)

        return oldToNew[node]