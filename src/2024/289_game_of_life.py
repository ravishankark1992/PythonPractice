from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        next_board = [[0 for i in range(rows-1)] for j in range(cols-1)]
        print("rows, cols",rows, cols)
        def count_neighbor(i,j):
            total = 0
            if valid_neighbor(i+1,j):
                total+=board[i+1][j]
            if valid_neighbor(i-1,j):
                total+=board[i-1][j]
            
            if valid_neighbor(i,j+1):
                total+=board[i][j+1]
            if valid_neighbor(i,j-1):
                total+=board[i][j-1]

            if valid_neighbor(i+1,j+1):
                total+=board[i+1][j+1]
            if valid_neighbor(i-1,j+1):
                total+=board[i-1][j+1]
            
            if valid_neighbor(i+1,j-1):
                total+=board[i+1][j-1]
            if valid_neighbor(i-1,j-1):
                total+=board[i-1][j-1]
            print(i,j,total)
            return total
        
        def valid_neighbor(i,j):
            if 0<=i and i<rows and 0<=j and j <cols:
                print("valid",i,j) 
                return True
            return False
        for i in range(rows):
            for j in range(cols):
                if board[i][j]==1:
                    if 2<count_neighbor(i,j)<=3:
                        next_board[i][j] = board[i][j]
                    else:
                        next_board[i][j]=0
                else:
                    if count_neighbor(i,j)==3:
                        next_board[i][j] = 1
                    else:
                        next_board[i][j] = 0

                
        

"""
2< live >3 - 0
2,3 -> do nothing
if 0,  3 neigh -> 1


"""
x=Solution()
board=[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
#board = [[1,1],[1,0]]
x.gameOfLife(board)

"""
2< live >3 - 0
2,3 -> do nothing
if 0,  3 neigh -> 1


"""