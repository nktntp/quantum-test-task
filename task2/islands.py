from typing import List


def number_of_islands(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    visited = [[False] * n for _ in range(m)]
    number_of_islands = 0

    def dfs(i: int, j: int):
        if not (0<=i<m and 0<=j<n) or visited[i][j] is True:
            return
            
        visited[i][j] = True
        if matrix[i][j] == 0:
            return
            
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    for i in range(m):
        for j in range(n):
            if visited[i][j] is False:
                dfs(i, j)
                if matrix[i][j] == 1:
                    number_of_islands += 1
    return number_of_islands


def input_data():
    m, n = list(map(int, input().split()))
    matrix = []
    for i in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)
    return m, n, matrix


if __name__ == "__main__":
    m, n, matrix = input_data()
    result = number_of_islands(matrix)
    print(f"Number of islands: {result}")
    