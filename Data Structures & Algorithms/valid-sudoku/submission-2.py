class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()

        for r in range(9):
            for c in range(9):
                num=board[r][c]
                if num==".":
                    continue
                box_id=(r//3, c//3)

                row_tag = f"{num}_row_{r}"
                col_tag = f"{num}_col_{c}"
                box_tag = f"{num}_box_{r//3}_{c//3}"
                if row_tag in seen or col_tag in seen or box_tag in seen:
                    return False

                seen.add(row_tag)
                seen.add(col_tag)
                seen.add(box_tag)
        return True