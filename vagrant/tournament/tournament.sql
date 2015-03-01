-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

\c tournament;

CREATE TABLE player (
  id serial PRIMARY KEY,
  name text
);

CREATE TABLE match (
  winner int references player(id),
  loser int references player(id),
  PRIMARY KEY(winner, loser)
);

CREATE VIEW standing AS
SELECT p.id as id, p.name as name, sum(case when p.id=m.winner then 1 else 0 end) as wins, count(m.winner) as matches
FROM player p
LEFT JOIN match m
ON p.id=m.winner OR p.id=m.loser
GROUP BY p.id;


CREATE VIEW bye AS
SELECT player.id as id, (case when player.id=match.winner then true else false end) as has_bye
FROM player
LEFT JOIN match
ON player.id=match.winner AND player.id=match.loser;