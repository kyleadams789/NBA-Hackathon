from model import ActionType, Event, Game, PlayerGame
import csv


def get_event_types():
    '''Returns the list of Event Types--not necessary'''
    event_types = {}
    with open('Event_Codes.txt') as txt_file:
        reader = csv.reader(txt_file, delimiter='\t')
        for index, row in enumerate(reader):
            if index == 0:
                continue
            if row[0] not in event_types:
                event_types[row[0]] = Event(row[0], row[2])
            event_types[row[0]].add_action_type(ActionType(row[1], row[3]))
    return event_types


def get_games():
    '''Returns the list of Game Lineups'''
    games = {}
    with open('Game_Lineup.txt') as txt_file:
        reader = csv.reader(txt_file, delimiter='\t')
        for index, row in enumerate(reader):
            if index == 0:
                continue
            if row[0] not in games:
                games[row[0]] = Game(row[0])
            if row[1] not in games[row[0]].lineups:
                games[row[0]].add_period(row[1])
            games[row[0]].update_lineup(row[1], row[2], row[3])
    return games


def main():
    '''Main program'''
    new_game = True
    players_in_game = []
    players_on_court = []
    player_games = []
    # Load games
    games = get_games()

    with open('Play_by_Play.txt') as txt_file:
        reader = csv.reader(txt_file, delimiter='\t')
        for index, row in enumerate(reader):
            game_id = row[0]
            event_msg_type = row[2]
            period = row[3]
            points = row[7]
            person1 = row[11]
            person2 = row[12]

            if index == 0:
                continue

            if new_game: # Load Players in Game
                players_in_game = [PlayerGame(game_id, player.id) for player in games[game_id].lineups['0'].players]
                print(players_in_game)
                new_game = False

            if event_msg_type == '12': # Start Period
                # Need to update to search players_in_game to access the PlayerGame objects
                # players_on_court = games[game_id].lineups[period].players
                print(players_on_court)

            elif event_msg_type == '16': # End Period
                # Finalize each player's off/def rating and save to list
                new_game = True

            if index == 500:
                break
    print('done')


if __name__ == '__main__':
    main()
