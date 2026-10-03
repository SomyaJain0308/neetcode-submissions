class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element == ".":
                    continue

                row = f"{element} in row {i}"
                column = f"{element} in column {j}"
                box = f"{element} in position ({i // 3}, {j // 3})"

                if (row in seen or column in seen or box in seen):
                    return False
                
                seen.add(row)
                seen.add(column)
                seen.add(box)

        return True