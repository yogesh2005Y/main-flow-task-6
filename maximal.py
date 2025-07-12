def maximal_rectangle(matrix):
    if not matrix: return 0
    max_area = 0
    dp = [0] * len(matrix[0])
    
    for row in matrix:
        for i in range(len(row)):
            dp[i] = dp[i] + 1 if row[i] == '1' else 0
        max_area = max(max_area, largest_rectangle_area(dp))
    return max_area

def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            H = heights[stack.pop()]
            W = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, H * W)
        stack.append(i)
    return 

def maximalRectangle(matrix):
    if not matrix:
        return 0
        max_area=0
        dp = [0] * len(matrix[0])

A = list(map(int, input("Enter row A: ").split()))
B = list(map(int, input("Enter row B: ").split()))
C = list(map(int, input("Enter row C: ").split()))
print("Enter number of rows in binary matrix")