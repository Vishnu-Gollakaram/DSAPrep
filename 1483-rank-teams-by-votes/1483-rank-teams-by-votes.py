from typing import List

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if not votes:
            return ""
        
        num_teams = len(votes[0])
        team_rankings = {team: [0] * num_teams for team in votes[0]}
        
        # Count votes for each team at each rank position
        for vote in votes:
            for rank, team in enumerate(vote):
                team_rankings[team][rank] -= 1  # Use negative for easier sorting
        
        # Sort teams based on rankings, tie-break alphabetically
        sorted_teams = sorted(votes[0], key=lambda team: (team_rankings[team], team))
        
        return "".join(sorted_teams)