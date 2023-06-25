ROW = 5
COL = 4
def diagonalOrder(matrix):
	for line in range(1, (ROW + COL)):
		start_col = max(0, line - ROW)
		count = min(line, (COL - start_col), ROW)

		for j in range(0, count):
			print(matrix[min(ROW, line) - j - 1][start_col + j], end="\t")
		print()

M = [[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
	[13, 14, 15, 16],
	[17, 18, 19, 20]]
diagonalOrder(M)

