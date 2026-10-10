class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        time = []

        for i in range(len(position)):
            time.append((position[i], ((target - position[i]) / speed[i])))

        sortedTime = sorted(time)
        print(sortedTime)
        ret = 0
        curTime = 0
        while sortedTime:
            curTime = sortedTime.pop()[1]
            ret += 1
            while sortedTime and sortedTime[-1][1] <= curTime:
                sortedTime.pop()
        
        return ret


        '''
        curTime = 3
        time = [2,1]
        ret = 1
        '''