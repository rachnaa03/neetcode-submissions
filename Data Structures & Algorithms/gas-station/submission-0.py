class Solution:
    def canCompleteCircuit(self, gas, cost):
        total = 0
        fuel = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]

            total += diff
            fuel += diff

            if fuel < 0:
                start = i + 1
                fuel = 0

        if total >= 0:
            return start

        return -1