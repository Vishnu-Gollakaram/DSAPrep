class Solution:
    def mincostTickets(self, days: List[int], cost: List[int]) -> int:
        n = len(days)
        memo = {}  # Dictionary to store the results of subproblems

        def min_cost(day_ind, rem_ticket_days):
            if day_ind == n:  # If all days are covered, return 0
                return 0
            if (day_ind, rem_ticket_days) in memo:  # Check if the subproblem is already solved
                return memo[(day_ind, rem_ticket_days)]

            if days[day_ind] <= rem_ticket_days:
                # If the current day is covered by the remaining ticket, skip to the next day
                memo[(day_ind, rem_ticket_days)] = min_cost(day_ind + 1, rem_ticket_days)
            else:
                # Otherwise, calculate the cost by considering 1-day, 7-day, and 30-day passes
                memo[(day_ind, rem_ticket_days)] = min(
                    cost[0] + min_cost(day_ind + 1, days[day_ind]),          # 1-day pass
                    cost[1] + min_cost(day_ind + 1, days[day_ind] + 6),     # 7-day pass
                    cost[2] + min_cost(day_ind + 1, days[day_ind] + 29)     # 30-day pass
                )

            return memo[(day_ind, rem_ticket_days)]  # Return the stored result

        return min_cost(0, 0)  # Start from day 0 with no remaining ticket days
