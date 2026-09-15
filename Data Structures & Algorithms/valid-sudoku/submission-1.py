from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue

                box_id = (i // 3, j // 3)

                row_key = ("row", i, val)
                col_key = ("col", j, val)
                box_key = ("box", box_id, val)

                if row_key in seen or col_key in seen or box_key in seen:
                    return False

                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        return True