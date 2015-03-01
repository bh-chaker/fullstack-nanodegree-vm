#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import math


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        return psycopg2.connect("dbname=tournament")
    except:
        print("Error inside 'connect' function.")
        raise SystemExit

def execute(query, params=(), commit=False):
    """Execute a SQL query.  Returns the query result if 'commit' is False."""
    pg = connect()
    c = pg.cursor()
    c.execute(query, params)
    rows = []
    if (commit):
        pg.commit()
    else:
        rows = c.fetchall();
    pg.close()
    return rows

def deleteMatches():
    """Remove all the match records from the database."""
    try:
        execute(query="DELETE FROM match;", commit=True)
    except:
        print("Error inside 'deleteMatches' function.")
        raise SystemExit


def deletePlayers():
    """Remove all the player records from the database."""
    try:
        execute(query="DELETE FROM player;", commit=True)
    except:
        print("Error inside 'deletePlayers' function.")
        raise SystemExit


def countPlayers():
    """Returns the number of players currently registered."""
    try:
        rows = execute(query="SELECT COUNT(id) FROM player;")
        return rows[0][0]
    except:
        print("Error inside 'countPlayers' function.")
        raise SystemExit

def countMatches():
    """Returns the number of matches currently registered."""
    try:
        rows = execute(query="SELECT COUNT(*) FROM match;")
        return rows[0][0]
    except:
        print("Error inside 'countMatches' function.")
        raise SystemExit

def playersHaveBye():
    """Returns booleans that are True when players received a 'bye'.

    The result is a dictionary: id => boolean
    """
    try:
        rows = execute(query="SELECT * FROM bye;")
        result = {}
        for row in rows:
            result[row[0]] = row[1]
        return result
    except:
        print("Error inside 'playersHaveBye' function.")
        raise SystemExit


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    try:
        execute(query="INSERT INTO player (name) VALUES (%s);", params=(name,), commit=True)
    except:
        print("Error inside 'registerPlayer' function.")
        raise SystemExit


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    try:
        return execute(query="SELECT id, name, wins, matches FROM standing ORDER BY wins DESC, matches DESC;")
    except Exception as e:
        print("Error inside 'playerStandings' function.")
        raise SystemExit


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    try:
        execute(query="INSERT INTO match (winner, loser) VALUES (%s, %s);", params=(winner, loser, ), commit=True)
    except psycopg2.IntegrityError as e:
        if e.pgcode=='23505':
            pass
        else:
            print("FOREIGN KEY constraint violation in 'reportMatch' function.")
            raise SystemExit
    except:
        print("Error inside 'reportMatch' function.")
        raise SystemExit

def matchPlayed(id1, id2):
    """Returns True when player with id1 already faced player with id2."""
    try:
        q = "SELECT true FROM match WHERE (match.winner=%s AND match.loser=%s) OR (match.winner=%s AND match.loser=%s)"
        rows = execute(query="SELECT EXISTS("+q+");", params=(id1, id2, id2, id1, ))
        return rows[0][0]
    except:
        print("Error inside 'countPlayers' function.")
        raise SystemExit

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()

    # Maximum number of matches each player should play
    maxRounds = int(math.ceil(math.log(len(standings), 2)))
    pairings = []

    # Check for odd players' number.
    # Then, assign a 'bye' to lowest player that did not receive one.
    if len(standings)%2==1:
        bye = playersHaveBye()
        for i in reversed(range(0, len(standings))):
            if not bye[standings[i][0]]:
                # A bye will be saved as a match with a single player
                pairings.append((standings[i][0],
                                 standings[i][1],
                                 standings[i][0],
                                 standings[i][1],
                                ))
                # Remove the player that received a 'bye'
                standings.pop(i)
                break

    i = 0
    while i < len(standings)-1:
        if standings[i][3]==maxRounds:
            i+=1
            continue

        # Look for the closest player that did not have a match with player at i
        j = i+1
        while j<len(standings) and matchPlayed(standings[i][0], standings[j][0]):
            j+=1

        # If we didn't find an opponent, we skip this player for this round
        # This only happens for odd number of players
        if j==len(standings):
            i+=1
            continue

        # If we found an opponent, we swap it to position i+1 (only if necessary)
        if j!=i+1:
            standings[i+1], standings[j] = standings[j], standings[i+1]

        # Pair the player at position i with player at position i+1
        pairings.append((standings[i][0],
                         standings[i][1],
                         standings[i+1][0],
                         standings[i+1][1],
                        ))

        # Advance to next couple
        i+=2
    return pairings


