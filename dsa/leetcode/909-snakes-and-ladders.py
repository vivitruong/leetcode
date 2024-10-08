# You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

# You start on square 1 of the board. In each move, starting from square curr, do the following:

# Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
# This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
# If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
# The game ends when you reach the square n2.
# A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

# Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

# For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
# Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()

        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c
            return [r, c]

        q = deque()
        q.append([1, 0])  # [square, moves]
        visit = set()
        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == length * length:
                    return moves + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1



        #java

    #     class Solution {
    # public int snakesAndLadders(int[][] board) {
    #     int n = board.length;

    #     reverseBoard(board);

    #     boolean[] visited = new boolean[n*n+1];
    #     Queue<int[]> q = new LinkedList<>();
    #     q.offer(new int[]{1, 0});
    #     visited[1] = true;

    #     while(!q.isEmpty()) {
    #         int[] curr = q.poll();
    #         for(int j=1; j<=6; j++) {
    #             int next = curr[0] + j;
    #             int[] coor = squareToCoor(next, n);
    #             if(board[coor[0]][coor[1]] != -1) {
    #                 next = board[coor[0]][coor[1]];
    #             }
    #             if(next == n*n) {
    #                 return curr[1] + 1;
    #             }
    #             if(!visited[next]) {
    #                 visited[next] = true;
    #                 q.offer(new int[]{next, curr[1] + 1});
    #             }
    #         }
    #     }

    #     return -1;
    # }
