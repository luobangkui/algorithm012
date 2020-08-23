from typing import List
#和单词搜索一样的目标，双向bfs
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not start or not end or not bank or end not in bank:
            return -1
        trans = {'A': 'CGT', 'C': 'AGT', 'G': 'CAT', 'T': 'ACG'}
        length = len(start)
        bq, eq = {start}, {end}
        bank = set(bank)
        dis = 0
        while bq and eq:
            nq = set()
            dis += 1
            for x in bq:
                for y in [x[:i] + c + x[i+1:] for i in range(length) for c in trans[x[i]]]:
                    if y in eq:
                        return dis
                    if y in bank:
                        bank.remove(y)
                        nq.add(y)
            bq = nq
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1