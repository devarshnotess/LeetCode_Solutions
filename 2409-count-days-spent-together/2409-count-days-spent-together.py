class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # we need to count how many days they are spending together
        days_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        prefixsum = [0]
        for date in days_of_months:
            prefixsum.append(prefixsum[-1] + date)

        aAD = self.CDOY(arriveAlice, prefixsum)
        lAD = self.CDOY(leaveAlice, prefixsum)
        aBd = self.CDOY(arriveBob, prefixsum)
        lBd = self.CDOY(leaveBob, prefixsum)

        return max(
            0, min(lAD, lBd) - max(aAD, aBd) + 1,
        )
        
    def CDOY(self, day: str, prefixsum: List[int]) -> int:
        month = int(day[:2])
        date = int( day[3:])
        return prefixsum[month - 1] + date


