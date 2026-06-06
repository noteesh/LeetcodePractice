class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        stack = []
        ret = 0

        for p, s in cars:
            if len(stack) == 0:
                stack.append((target - p) / s)
                ret += 1
                continue
            
            prevTime = stack[-1]
            timeToFinish = (target - p) / s
            if timeToFinish <= prevTime:
                continue
            else:
                stack.append(timeToFinish)
                ret += 1

        return ret
