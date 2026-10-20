class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:       
        rows ={}
        cols = {}
        boxes = {}
        for r in range(9):
            for c in range(9):
                digit=board[r][c]
                box=(r//3, c//3)
                row_set = rows.setdefault(r, set())
                col_set = cols.setdefault(c, set())
                box_set = boxes.setdefault(box, set())

                if digit == ".":
                    continue

                if digit in row_set or digit in col_set or digit in box_set:
                    return False

                else:
                    row_set.add(digit)
                    col_set.add(digit)
                    box_set.add(digit)
        return True