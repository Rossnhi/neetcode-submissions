class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        cars = sorted(list(zip(position, speed)), reverse = True)
        for car in cars:
            if len(fleets) == 0:
                fleets.append(car)
            if (target - fleets[-1][0])/fleets[-1][1] < (target - car[0])/car[1]:
                fleets.append(car)
        return len(fleets)