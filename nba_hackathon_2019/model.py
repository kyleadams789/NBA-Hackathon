class Event:
    '''The type of basketball play'''
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.action_types = []

    def add_action_type(self, ActionType):
        self.action_types.append(ActionType)


class ActionType:
    '''A sub-category of an Event'''
    def __init__(self, action_type, description):
        self.action_type = action_type
        self.description = description


class Game:
    '''A game of basketball'''
    def __init__(self, game_id):
        self.game_id = game_id
        self.lineups = {}

    def add_period(self, period):
        self.lineups[period] = Lineup(period)

    def update_lineup(self, period, player_id, team_id):
        self.lineups[period].add_player(player_id, team_id)

    def get_lineup(self, period):
        return self.lineups[period]


class Lineup:
    '''List of players that are on the court at a given period start'''
    def __init__(self, period):
        self.period = period
        self.players = []

    def add_player(self, player_id, team_id):
        self.players.append(Player(player_id, team_id))


class Player:
    '''A basketball player'''
    def __init__(self, player_id, team_id):
        self.id = player_id
        self.team_id = team_id


class PlayerGame:
    '''A combination of player and game--used for output format'''
    def __init__(self, game_id, player_id):
        self.game_id = game_id
        self.player_id = player_id
        self.off_pts = 0.0
        self.def_pts = 0.0
        self.off_poss = 0
        self.def_poss = 0
        self.off_rtg = 0.0
        self.def_rtg = 0.0

    def calc_rtg(self):
        '''Calculate the offensive and defensive rating'''
        self.off_rtg = self.off_pts / (self.off_poss/100)
        self.def_rtg = self.def_pts / (self.def_poss/100)

    def update_off(self, points):
        '''Add the given point value to the running offensive rating count'''
        self.off_pts += points

    def update_def(self, points):
        '''Add the given point value to the running offensive rating count'''
        self.def_pts += points

    def update_poss(self, offense=False):
        '''Increments the possession count. Offensive possession by default'''
        if offense:
            self.off_poss += 1
        else:
            self.def_poss += 1
