# https://leetcode.com/problems/valid-sudoku/


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Let's consider the sub-boxes to be labeled 1 thru 9
        sub_boxes_seen = [set() for _ in range(9)]
        # Same for rows and columns
        rows_seen = [set() for _ in range(9)]
        cols_seen = [set() for _ in range(9)]
        for row_i, row in enumerate(board):
            for col_j, num in enumerate(row):
                # Skip non-numbers
                if num == ".":
                    continue
                # Add the current number to the row/col/sub-box:
                sub_box_index = col_j // 3 + 3 * (row_i // 3)
                if any(num in s for s in [rows_seen[row_i], cols_seen[col_j], sub_boxes_seen[sub_box_index]]):
                    return False
                rows_seen[row_i].add(num)
                cols_seen[col_j].add(num)
                sub_boxes_seen[sub_box_index].add(num)
        return True
