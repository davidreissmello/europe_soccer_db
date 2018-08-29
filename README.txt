David Reiss-Mello

European soccer database in PostreSQL with web front end in Python using Flask

Description of implemented features:
1)
Task :"Searching a player’s name to find out on what teams (international, domestic, etc) he plays on and how many matches (and tournaments -- which is linked with the team info not player info) he has won on each team."

Implemetation: For this feature, click "view all players" link and type in the name of the player you would like to search for. This will tell you some of the player's stats along with the team they play on. Due to my ex-partner's lack of awareness of the strucuture of the database, the second part of this functionality is not possible. However, I created a rating system for each team based on the player's overall rating. From the index, you can click on the "search all teams" link, and filter the teams by league. This will give you a table with the league's team sorted by average overall team rating, indicating which team is most likely to win a tournament.

2)
Task: "Searching a team to find out the predominant physical characteristics of the players on that team."

Implementation: Click on "search all teams", then click on "click here to search for team's roster." On this page, just input the name of the team you would like to see, and the table will display all the teams players along with key details about each player.

3)
Task: "finding teams with similar playstyle based on their favorite team"

Implementation: Click on "search all teams," and input the name of your favoite team. The table will display information of teams with a rating .5 higher or .5 lower than the searched team.

4)
New Task: Predict who will win a match.

Implementation: To do this, go to "Predict a score between two teams" and enter the home team and the away team. This query will calculate the difference in goals when the home team plays at home and hte difference in goals when the away team plays away, thus controlling for home vs away biases. The value will be an indicator of how much each team is likely to win by. The team with the highest value is likelier to win.


2 most interesting pages:
1) Similar teams operation:
SQL Query:
SELECT P.team_id, team_long_name, team_short_name, League.league_id, league_name, country_id, avg(overall_rating) AS team_rating
FROM Players P
JOIN Teams
ON P.team_id = Teams.team_id
JOIN Team_League
ON Teams.team_id = Team_League.team_id
JOIN League
ON League.league_id = Team_League.league_id
GROUP BY P.team_id, team_long_name, team_short_name, League.league_id, league_name, country_id
HAVING avg(overall_rating) >= ((SELECT AVG(overall_rating)
	FROM Players P
	JOIN Teams ON P.team_id = Teams.team_id
	WHERE team_long_name LIKE '%Chelsea%') - 0.5) AND avg(overall_rating) <= ((SELECT AVG(overall_rating)
	FROM Players P
	JOIN Teams ON P.team_id = Teams.team_id
	WHERE team_long_name LIKE '%Chelsea%') + 0.5
LIMIT 20
;

Explanation: For display purposes, I combine the players, teams, team_league, and league tables. Then I group by team and calculate the average overall rating of the players on that team. If the overall team rating is within a 1 point range, then display that team.

2)
SELECT Teams.team_long_name, (SUM(home_team_goals) - SUM(away_team_goals))/COUNT(*) AS difference
FROM Matches
JOIN Teams
ON Teams.team_id = Matches.home_team_id
WHERE team_long_name LIKE 'Hull City'
GROUP BY team_long_name
UNION
SELECT Teams.team_long_name, (SUM(away_team_goals) - SUM(home_team_goals))/COUNT(*) AS difference
FROM Matches
JOIN Teams
ON Teams.team_id = Matches.home_team_id
WHERE team_long_name LIKE 'Liverpool'
GROUP BY team_long_name;

Explanation: In the first half of the query, I took the sum of all the goals the home team has score while playing at home minus the sum of all the goals score on them when they have played at home. Then I divided it by the count to find the average number of goals they win or lose by. Then simply chose the team that corresponds to the home team indicated by the user. For the away team, do the same thing as for the home team but invert the home_team_goals and away_team goals. Then, take a union of those queries.



Note: used sorttable.js to add some basic functionality: you can click the column headers of the table to sort the table. Here is the link to the documentation:
 https://www.kryogenix.org/code/browser/sorttable/sorttable.js
