# https://leetcode.com/problems/valid-sudoku/


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Bitmasks for digits seen in each row, column, and 3x3 sub-box
        row_masks = [0] * 9
        col_masks = [0] * 9
        box_masks = [0] * 9

        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if cell == ".":
                    continue  # Skip empty cells

                # Map digit '1'-'9' → bit positions 0-8
                digit_bit = 1 << (ord(cell) - ord("1"))
                # Identify which 3x3 sub-box this cell belongs to
                box_index = (row // 3) * 3 + (col // 3)

                # If digit already seen in the row, column, or sub-box → invalid
                if row_masks[row] & digit_bit or col_masks[col] & digit_bit or box_masks[box_index] & digit_bit:
                    return False

                # Mark digit as seen in this row, column, and sub-box
                row_masks[row] |= digit_bit
                col_masks[col] |= digit_bit
                box_masks[box_index] |= digit_bit
        return True
