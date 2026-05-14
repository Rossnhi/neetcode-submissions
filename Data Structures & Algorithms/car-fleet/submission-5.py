class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([[position[i], speed[i]] for i in range(len(position))])
        fleets = []
        for car in cars:
            time = (target - car[0])/car[1]
            while len(fleets) and fleets[-1] <= time:
                fleets.pop()
            fleets.append(time)
        return len(fleets)