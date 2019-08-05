from model import ActionType, Event, Game, PlayerGame, Team

playersOnCourt = [None] * 10
validPlayers = [None] * 10
Event_Msg_Type = 0
Action_Type = 0
offensiveTeam = None
defensiveTeam = None
off_pts = 0
def_pts = 0
off_poss = 0
def_poss = 0
option1 = 0
option2 = 0
option3 = 0
Person1 = None
Person2 = None
defensiveRebound = False


def subOnCourtPlayers(Person1, Person2, playersOnCourt): 
    '''change which players are physically on the court at a given moment'''
    playersOnCourt = [p.replace(Person1, Person2) for p in playersOnCourt]
    return(playersOnCourt)

# def lockPlayersIn(playersOnCourt):
#     '''find which players were on court for previous play and keep them in game until next play comes'''

#     overturned_event = Event.objects.all().last()
#     overturned_event.delete()

#     return(off_players, def_players)

def updateValidPlayers():
    '''updates which players will be receiving updated ratings'''
    validPlayers == playersOnCourt 

def countPoints(option1, option2, option3):
    '''show how many points should be added to off/def_ptss for players on court'''
    points = option1 + option2 + option3 
    return(points)

def revert(off_players, def_players, points=0):
    '''revert call on previous play if replay overturns call'''
    ##Use this method to revert to state before the replay, then you will have to create the event as ruled after overturn
    overturned_event = Event.objects.all().last()
    overturned_event.delete()

    for player in off_player:
        player.off_pts -= 1

    for player in def_player:
        player.def_pts -= 1

    return(off_players, def_players)

#because there are lots of non-FT events, updating players on anything but a FT event can help that
#should we not update on substitutions/technicals/ejections either (because the game could still be paused?) 
# (but does it matter if the game is still paused if there will be NO POINTS/POSSESSION COUNTS)
if Event_Msg_Type !== 3:
    updateValidPlayers()

if Event_Msg_Type == 1: #bucket
    if offensiveTeam:
        off_pts += countPoints(option1, option2, option3)
        off_poss += 1
    if defensiveTeam:
        def_pts += countPoints(option1, option2, option3)
        def_poss += 1

elif Event_Msg_Type == 3: #FT shot
    #each play can be associated with 10 validPlayers
    #revert back to the previous play's players and lock them in
    #we could keep a temporary list of onCourtPlayers that was 1 change old at all times for cases like this
    if offensiveTeam:
        off_pts += countPoints(option1, option2, option3)
        off_poss += 1
    if defensiveTeam:
        def_pts += countPoints(option1, option2, option3)
        def_poss += 1
    updateValidPlayers() #after the FTs, then update the 10 players on the court

elif Event_Msg_Type == 4: #rebound
    if defensiveRebound:
        def_poss += 1
        off_poss += 1
    
elif Event_Msg_Type == 5: #Turnover
    if offensiveTeam:
        off_poss += 1
    if defensiveTeam:
        def_poss += 1
    
elif Event_Msg_Type == 6: #foul
    #there is already a TO for offensive foul
    #
    pass

elif Event_Msg_Type == 8: #sub
    Person1 #these come from play-by-play
    Person2 
    subOnCourtPlayers(Person1, Person2, playersOnCourt)

elif Event_Msg_Type == 12: #start period
    #todo - insert logic from Michael to find which 10 players are on the court at the beginning of each quarter
    pass

elif Event_Msg_Type == 18: #instant replay
    #if Action_Type == 1
        #look back at last call and reverse it
        #
        #if the last call changed possession, then revert possession and decrement off_poss/def_poss counts
    pass