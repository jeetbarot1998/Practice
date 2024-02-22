class IslandProblem(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return
        t_rows = len(grid)
        t_col = len(grid[0])
        islands = 0
        visited = set()

        def bfs(r, c):
            q = []  # make a queue
            q.append((r, c))  # add the present r,c to th queue
            visited.add((r, c))  # mark the present r,c as visited
            #  Traverse the adjacent now
            while q:
                present_r, present_c = q.pop(0)  # only this changes in BFS an DFS
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dir_r, dir_c in directions:
                    new_r_to_check, new_c_to_check = present_r + dir_r, present_c + dir_c
                    if ((new_r_to_check in range(t_rows)) and  # check if not going out of grid
                            (new_c_to_check in range(t_col)) and  # check if not going out of grid
                            grid[new_r_to_check][new_c_to_check] == "1" and  # check if the relevant direction is "1"
                            (present_r, present_c) not in visited):  # check if the adjacent is not visited already
                        visited.add((present_r, present_c))  # add to the queue
                        q.append((present_r, present_c))  # add to the visited

        def dfs(r, c):
            q = []  # make a queue
            q.append((r, c))  # add the present r,c to th queue
            visited.add((r, c))  # mark the present r,c as visited
            #  Traverse the adjacent now
            while q:
                present_r, present_c = q.pop()  # only this changes in BFS an DFS
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dir_r, dir_c in directions:
                    new_r_to_check, new_c_to_check = present_r + dir_r, present_c + dir_c
                    if ((new_r_to_check in range(t_rows)) and  # check if not going out of grid
                            (new_c_to_check in range(t_col)) and  # check if not going out of grid
                            grid[new_r_to_check][new_c_to_check] == "1" and  # check if the relevant direction is "1"
                            (present_r, present_c) not in visited):  # check if the adjacent is not visited already
                        visited.add((present_r, present_c))  # add to the queue
                        q.append((present_r, present_c))  # add to the visited

        for each_row in range(t_rows):
            for each_col in range(t_col):
                if (grid[each_row][each_col] == "1" and grid[each_row][each_col] not in visited):
                    bfs(each_row, each_col)
                    islands += 1
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
s = IslandProblem()
print(s.numIslands(grid))
