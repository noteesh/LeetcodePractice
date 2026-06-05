class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        rows = [set() for i in range(N)]
        columns = [set() for i in range(N)]
        boxes = [set() for i in range(N)]

        for i, n in enumerate(board):
            for j, m in enumerate(board[i]):
                if m == ".":
                    continue
                
                # rows checking
                if m in rows[i]:
                    return False
                else:
                    rows[i].add(m)
                
                # columns checking
                if m in columns[j]:
                    return False
                else:
                    columns[j].add(m)

                # boxes checking
                if m in boxes[(i // 3) * 3 + (j // 3)]:
                    return False
                else:
                    boxes[(i // 3) * 3 + (j // 3)].add(m)
        
        return True