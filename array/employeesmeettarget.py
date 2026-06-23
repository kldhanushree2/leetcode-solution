"""You are given a 0-indexed integer array hours, where hours[i] represents the number of hours the ith employee worked in a week. A company wants to reward its employees based on their working hours."""
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        c=0
        for i in hours:
            if(i>=target):
                c+=1;
        return c