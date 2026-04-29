class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[position[_], speed[_]] for _ in range(len(position))]
        cars = sorted(cars)
        fleets = []
        for i in range(len(cars)):
            while len(fleets) > 0 and fleets[-1] <= (target - cars[i][0])/cars[i][1]:
                fleets.pop()
            fleets.append((target - cars[i][0])/cars[i][1])
        return len(fleets)