#Connected Cell in a Grid
m = input()
n = input()
matrix = []
used = [[0 for _ in xrange(n)] for _ in xrange(m)]
for i in xrange(m):
    temp = map(int, raw_input().strip().split())
    matrix.append(temp)

Maxregion = 0

Dir = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]

def DFS( matrix, i, j, m, n ):
    
    num = 1
    for k in Dir:
        x = i + k[0]
        y = j + k[1]
        if x >= 0 and x < m and y >= 0 and y < n and used[x][y] == 0 and matrix[x][y] == 1:
            used[x][y] = 1
            num += DFS(matrix, x, y, m, n)
    return num
    
for i in xrange(m):
    for j in xrange(n):
        if matrix[i][j] == 1 and used[i][j] == 0:
            used[i][j] = 1
            temp = DFS(matrix, i, j, m, n)
            if temp > Maxregion:
                Maxregion = temp
print Maxregion
