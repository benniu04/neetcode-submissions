class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed_courses = 0

        while queue:
            curr_prereq = queue.popleft()
            completed_courses += 1

            for dependent_course in adj[curr_prereq]:
                in_degree[dependent_course] -= 1
                if in_degree[dependent_course] == 0:
                    queue.append(dependent_course)
        
        return completed_courses == numCourses