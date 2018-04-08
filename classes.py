def user_selects_view(cursor):
  table = []
  user_id = []
  user_name = []
  team_id = []
  team_long_name = []
  team_short_name = []

  for line in cursor:
    user_id.append(line['user_id'])
    user_name.append(line['user_name'])
    team_id.append(line['team_id'])
    team_long_name.append(line['team_long_name'])
    team_short_name.append(line['team_short_name'])

  for key in range(len(user_id)):
    entry = dict(user_id=user_id[key], user_name=user_name[key], team_id=team_id[key], team_long_name=team_long_name[key], team_short_name=team_short_name[key])
    table.append(entry)

  return table


def player_view(cursor):
  table = []
  player_id = []
  player_name = []
  player_dob = []
  height = []
  weight = []
  overall_rating = []
  potential = []
  team_id = []

  for line in cursor:
    player_id.append(line['player_id'])
    player_name.append(line['player_name'])
    player_dob.append(line['player_dob'])
    height.append(line['height'])
    weight.append(line['weight'])
    overall_rating.append(line['overall_rating'])
    potential.append(line['potential'])
    team_id.append(line['team_id'])

  for key in range(len(player_id)):
    entry = dict(player_id=player_id[key], player_name=player_name[key], player_dob=player_dob[key], height=height[key], weight=weight[key], overall_rating=overall_rating[key], potential=potential[key], team_id=team_id[key])
    table.append(entry)

  return table    

def goal_keeper_view(cursor):
  table = []
  player_id = []
  player_name = []
  player_dob = []
  height = []
  weight = []
  overall_rating = []
  potential = []
  team_id = []
  gk_diving_rating = []
  gk_reflexes_rating = []

  for line in cursor:
    player_id.append(line['player_id'])
    player_name.append(line['player_name'])
    player_dob.append(line['player_dob'])
    height.append(line['height']) 
    weight.append(line['weight']) 
    overall_rating.append(line['overall_rating']) 
    potential.append(line['potential']) 
    team_id.append(line['team_id']) 
    gk_diving_rating.append(line['gk_diving_rating'])
    gk_reflexes_rating.append(line['gk_reflexes_rating'])

  for key in range(len(player_id)):
    entry = dict(player_id=player_id[key], player_name=player_name[key], player_dob=player_dob[key], height=height[key], weight=weight[key], overall_rating=overall_rating[key], potential=potential[key], team_id=team_id[key], gk_diving_rating=gk_diving_rating[key], gk_reflexes_rating=gk_reflexes_rating[key])
    table.append(entry)

  return table



def defender_view(cursor):
  table = []
  player_id = []
  player_name = []
  player_dob = []
  height = []
  weight = []
  overall_rating = []
  potential = []
  team_id = []
  aggression_rating = []
  marking_rating = []

  for line in cursor:
    player_id.append(line['player_id'])
    player_name.append(line['player_name'])
    player_dob.append(line['player_dob'])
    height.append(line['height']) 
    weight.append(line['weight']) 
    overall_rating.append(line['overall_rating']) 
    potential.append(line['potential']) 
    team_id.append(line['team_id']) 
    aggression_rating.append(line['aggression_rating'])
    marking_rating.append(line['marking_rating'])    

  for key in range(len(player_id)):
    entry = dict(player_id=player_id[key], aggression_rating=aggression_rating[key], marking_rating=marking_rating[key], player_name=player_name[key], player_dob=player_dob[key], height=height[key], weight=weight[key], overall_rating=overall_rating[key], potential=potential[key], team_id=team_id[key])
    table.append(entry)

  return table

def midfielder_view(cursor):
  table = []
  player_id = []
  player_name = []
  player_dob = []
  height = []
  weight = []
  overall_rating = []
  potential = []
  team_id = []
  preferred_foot = []
  crossing_rating = []

  for line in cursor:
    player_id.append(line['player_id'])
    player_name.append(line['player_name'])
    player_dob.append(line['player_dob'])
    height.append(line['height']) 
    weight.append(line['weight']) 
    overall_rating.append(line['overall_rating']) 
    potential.append(line['potential']) 
    team_id.append(line['team_id']) 
    preferred_foot.append(line['preferred_foot'])
    crossing_rating.append(line['crossing_rating'])

  for key in range(len(player_id)):
    entry = dict(player_id=player_id[key], preferred_foot= preferred_foot[key], crossing_rating=crossing_rating[key], player_name=player_name[key], player_dob=player_dob[key], height=height[key], weight=weight[key], overall_rating=overall_rating[key], potential=potential[key], team_id=team_id[key])
    table.append(entry)

  return table


def forward_view(cursor):
  table = []
  player_id = []
  player_name = []
  player_dob = []
  height = []
  weight = []
  overall_rating = []
  potential = []
  team_id = []
  sprint_speed_rating = []
  shot_power_rating = []

  for line in cursor:
    player_id.append(line['player_id'])
    player_name.append(line['player_name'])
    player_dob.append(line['player_dob'])
    height.append(line['height']) 
    weight.append(line['weight']) 
    overall_rating.append(line['overall_rating']) 
    potential.append(line['potential']) 
    team_id.append(line['team_id']) 
    sprint_speed_rating.append(line['sprint_speed_rating']) 
    shot_power_rating.append(line['shot_power_rating'])

  for key in range(len(player_id)):
    entry = dict(player_id=player_id[key], sprint_speed_rating=sprint_speed_rating[key], shot_power_rating=shot_power_rating[key], player_name=player_name[key], player_dob=player_dob[key], height=height[key], weight=weight[key], overall_rating=overall_rating[key], potential=potential[key], team_id=team_id[key])
    table.append(entry)

  return table


#possible problem with team_id
def user_players_view(cursor):
  table = []
  player_id = []
  player_name = []
  player_dob = []
  height = []
  weight = []
  overall_rating = []
  potential = []
  team_id = []
  user_id = []
  user_name = []

  for line in cursor:
    player_id.append(line['player_id'])
    player_name.append(line['player_name'])
    player_dob.append(line['player_dob'])
    height.append(line['height']) 
    weight.append(line['weight']) 
    overall_rating.append(line['overall_rating']) 
    potential.append(line['potential']) 
    team_id.append(line['team_id']) 
    user_id.append(line['user_id'])
    user_name.append(line['user_name'])

  for key in range(len(player_id)):
    entry = dict(player_id=player_id[key], user_id=user_id[key], user_name=user_name[key], player_name=player_name[key], player_dob=player_dob[key], height=height[key], weight=weight[key], overall_rating=overall_rating[key], potential=potential[key], team_id=team_id[key])
    table.append(entry)

  return table


def team_view(cursor):
  table = []
  team_id = []
  team_long_name = []
  team_short_name = []

  for line in cursor:
    team_id.append(line['team_id'])
    team_long_name.append(line['team_long_name'])
    team_short_name.append(line['team_short_name'])
 
  for key in range(len(team_id)):
    entry = dict(team_id = team_id[key], team_long_name=team_long_name[key], team_short_name = team_short_name[key])
    table.append(entry)

  return table


def team_roster_view(cursor):
  table = []
  player_id = []
  player_name = []
  player_dob = []
  height = []
  weight = []
  overall_rating = []
  potential = []
  team_id = []
  team_long_name = []
  team_short_name = []

  for line in cursor:
    player_id.append(line['player_id'])
    player_name.append(line['player_name'])
    player_dob.append(line['player_dob'])
    height.append(line['height']) 
    weight.append(line['weight']) 
    overall_rating.append(line['overall_rating']) 
    potential.append(line['potential']) 
    team_id.append(line['team_id']) 
    team_long_name.append(line['team_long_name'])
    team_short_name.append(line['team_short_name'])

  for key in range(len(player_id)):
    entry = dict(team_long_name=team_long_name[key], team_short_name = team_short_name[key], player_id=player_id[key], player_name=player_name[key], player_dob=player_dob[key], height=height[key], weight=weight[key], overall_rating=overall_rating[key], potential=potential[key], team_id=team_id[key])
    table.append(entry)

  return table


def league_view(cursor):
  table = []
  league_id = []
  coutry_id = []
  league_name = []
  country_name = []

  for line in cursor:
    league_id.append(line['league_id'])
    country_id.append(line['country_id'])
    league_name.append(line['league_name'])
    country_name.append(line['country_name'])

  for key in range(len(league_id)):
    entry = dict(league_id=league_id[key], country_id=country_id[key], league_name=league_name[key], country_name=country_name[key])
    table.append(entry)

  return table 


def team_league_view(cursor):
  table = []
  team_id = []
  team_long_name = []
  team_short_name = []
  league_id = []
  coutry_id = []
  league_name = []
  country_name = []

  for line in cursor: 
    team_id.append(line['team_id'])
    team_long_name.append(line['team_long_name'])
    team_short_name.append(line['team_short_name'])
    league_id.append(line['league_id'])
    country_id.append(line['country_id'])
    league_name.append(line['league_name'])
    country_name.append(line['country_name'])
  
  for key in range(len(team_id)):
    entry = dict(team_id = team_id[key], team_long_name=team_long_name[key], team_short_name = team_short_name[key], league_id=league_id[key], country_id=country_id[key], league_name=league_name[key], country_name=country_name[key])
    table.append(entry)

  return table

def country_view(cursor):
  table = []
  country_id = []
  country_name = []

  for line in cursor:
    country_id.append(line['country_id'])
    country_name.append(line['country_name'])

  for key in range(len(country_id)):
    entry = dict(country_id=country_id[key], country_name=country_name[key])
    table.append(entry)

  return table 


def matches_view(cursor):
  table = []
  season = []
  stage = []
  match_date = []
  home_team_id = []
  away_team_id = []
  home_team_goals = []
  away_team_goals = []

  for line in cursor:
    season.append(line['season'])
    stage.append(line['stage'])
    match_date.append(line['match_date'])
    home_team_id.append(line['home_team_id'])
    away_team_id.append(line['away_team_id'])
    home_team_goals.append(line['home_team_goals'])
    away_team_goals.append(line['away_team_goals'])

  for key in range(len(season)):
    entry = dict(season = season[key], stage = stage[key], match_date=match_date[key], home_team_id=home_team_id[key], away_team_id=away_team_id[key], home_team_goals=home_team_goals[key], away_team_goals=away_team_goals[key])
    table.append(entry)

  return table
