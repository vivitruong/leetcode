# You are given a 0-indexed 8 x 8 grid board, where board[r][c] represents the cell (r, c) on a game board. On the board, free cells are represented by '.', white cells are represented by 'W', and black cells are represented by 'B'.

# Each move in this game consists of choosing a free cell and changing it to the color you are playing as (either white or black). However, a move is only legal if, after changing it, the cell becomes the endpoint of a good line (horizontal, vertical, or diagonal).

# A good line is a line of three or more cells (including the endpoints) where the endpoints of the line are one color, and the remaining cells in the middle are the opposite color (no cells in the line are free). You can find examples for good lines in the figure below:


# Input: board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]], rMove = 4, cMove = 3, color = "B"
# Output: true
# Explanation: '.', 'W', and 'B' are represented by the colors blue, white, and black respectively, and cell (rMove, cMove) is marked with an 'X'.
# The two good lines with the chosen cell as an endpoint are annotated above with the red rectangles.


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        """
        1. length should be at least 3 cells
        2. should start at endpoint.
        3. endpoints 1 color, inner inverted color
        """
        inverted_color = 'B' if color == 'W' else 'W'
        for dr,dc in (1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1):
            nr = rMove + dr # set new_row to the first inverted_color pos
            nc = cMove + dc # set new_col to the first inverted_color pos
            count = 1
            while 8 > nr >= 0 <= nc < 8 and board[nr][nc] == inverted_color: # go until you find first non inverted_color (or border)
                nr += dr
                nc += dc
                count += 1
            if 8 > nr >= 0 <= nc < 8 and board[nr][nc] == color and count >= 2: # 1st cell is endpoint, thus 1, 2nd - inverted, and this line checks the 3rd point
                return True
        return False
