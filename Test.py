class SportsWinBetting:
    def __init__(self):
        self.teams = {}
        self.bets = []
 
    def add_team(self, team_name):
        # Add a new team to the system
        self.teams[team_name] = {
            'wins': 0,
            'losses': 0
        }
 
     def place_bet(self, team_name, amount):
        # Place a bet on a team
        self.bets.append((team_name, amount))
 
    def resolve_game(self, winning_team):
        # Update win/loss records for teams and settle bets
        for team_name in self.teams:
            if team_name == winning_team:
                self.teams[team_name]['wins'] += 1
            else:
                self.teams[team_name]['losses'] += 1
 
       
 
