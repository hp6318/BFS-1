'''
BFS : Topological sort
Find the independent courses that are not dependent on any other courses. They become 
the starting root nodes of our traversal. Maintain 
    - dependency_list =  this will be populated with how many dependencies each course has
    - adjacency_map = {node - [neighbors]} - neighbors are courses which depend on this node
Start BFS, pop courses from BFS, reduce the neighbors' dependency. if any of the neighbor's
dependency have reduced to 0, this course can be taken and hence add to the BFS queue.
Time Complexity: O(V+E) , actually O(max(V,E)), where V = vertexes, E = Edges
Space Complexity: O(V+E)

'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependency = [0]*numCourses # this will be populated with how many dependencies each course has
        adjacency_map = {} # {node - [neighbors]} - neighbors are courses which depend on this node

        for edges in prerequisites:
            children, parent = edges
            dependency[children]+=1
            adjacency_map[parent] = adjacency_map.get(parent,[])
            adjacency_map[parent].append(children)

        # initiate the BFS queue
        bfs_queue = deque()

        courses_taken = 0 # track how many courses can be taken 

        # get the independent course
        for i in range(len(dependency)):
            if dependency[i]==0:
                bfs_queue.append(i)
                courses_taken+=1
        
        if courses_taken==numCourses: # Edge case: When all are independent courses, no prerequisites
            return True


        while (len(bfs_queue)!=0):
            parent = bfs_queue.popleft()

            if parent not in adjacency_map:
                continue 
            for child in adjacency_map[parent]:
                dependency[child]-=1 # since parent course has been taken, reduce dependency required for its child
                if dependency[child]==0: # all pre-requisistes done,
                    bfs_queue.append(child) # take this course
                    courses_taken+=1
                    if courses_taken==numCourses:
                        # all courses taken
                        return True

        return False
        