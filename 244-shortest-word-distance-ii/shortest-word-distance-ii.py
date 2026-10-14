class WordDistance:

    def __init__(self, wordsDict: list[str]):
        self.locations = defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.locations[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        l1, l2 = self.locations[word1], self.locations[word2]

        p1, p2 = 0, 0
        diff = float('inf')

        while p1 < len(l1) and p2 < len(l2):
            diff = min(diff, abs(l1[p1] - l2[p2]))
            if l1[p1] < l2[p2]:
                p1 += 1
            else:
                p2 += 1
        return diff


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)