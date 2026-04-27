class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)), reverse = True)
        fleets = []
        for car in cars:
            if len(fleets) == 0 or (target - car[0])/car[1] > fleets[-1]:
                fleets.append((target - car[0])/car[1])
        return len(fleets)