#!/usr/bin/env python2.7
"""
To run locally:

    python server.py

Go to http://localhost:8111 in your browser.

A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""

import os
from classes import *
from sqlalchemy import *
from sqlalchemy import exc
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

DATABASEURI = "postgresql://dsr2141:password@35.227.79.146/proj1part2"
engine = create_engine(DATABASEURI)

#Reflect tables all at once: http://docs.sqlalchemy.org/en/latest/core/reflection.html
meta = MetaData()
meta.reflect(bind=engine)


#Create database connection
@app.before_request
def before_request():
  try:
    g.conn = engine.connect()
  except:
    print "uh oh, problem connecting to database"
    import traceback; traceback.print_exc()
    g.conn = None

#Close database connection
@app.teardown_request
def teardown_request(exception):
  try:
    g.conn.close()
  except Exception as e:
    pass


#Home page
@app.route('/')
def index():
  print request.args
  return render_template("index.html")

#Users page
@app.route('/user_selects')
def user_selects():
  cursor = g.conn.execute('SELECT * FROM User_Selects JOIN Teams ON User_Selects.team_id = Teams.team_id ORDER BY user_name ASC')
  table = user_selects_view(cursor)
  cursor.close()
  return render_template('user_selects.html', table=table)

#Search for users
@app.route('/user_selects', methods=['POST'])
def user_selects_search():
  search_name = request.form['search_name'].encode('ascii', 'ignore')
  cursor = g.conn.execute("SELECT * FROM User_Selects JOIN Teams ON User_Selects.team_id = Teams.team_id WHERE user_name LIKE '%" + search_name + "%'")

  matches = cursor.fetchall()
  cursor.close()
  table = get_user_selects_view(matches)
  return render_template('user_selects.html', table=table)

#Add user 
@app.route('/add_user', methods=['POST']
def add_user_selects():
  user_selects = meta.tables['user_selects']
  user_id = request.form['user_id']
  user_name = request.form['user_name']
  team_id = request.form['team_id']

  insert = user_selects.insert().values(user_id=user_id, user_name=user_name, team_id=team_id)

  try:
    g.conn.execute(insert)
  except exc.SQLAlchemyError:
    return render_template('user_selects.html', message='Insert failed.')
  return redirect('/user_selects')

#Players page
@app.route('/players')
def players():
  cursor = g.conn.execute("SELECT * FROM Players ORDER BY player_name ASC")
  table = player_view(cursor)
  cursor.close()
  return render_template("players.html", table=table)

#Search for player
@app.route('/player_search', methods=['POST'])
def player_search():
  search_name = request.form['search_name'].encode('ascii', 'ignore')
  cursor = g.conn.execute("SELECT * FROM Players WHERE player_name LIKE '%" + search_name + "%'")

  matches = cursor.fetchall()
  cursor.close()
  table = get_players_view(matches)
  return render_template('players.html', table=table) 

#Add player
@app.route('/add_player', methods=['POST'])
def add_player():
  players = meta.tables['players']
  player_id = request.form['player_id']
  player_name = request.form['player_name']
  player_dob = request.form['player_dob']
  height = request.form['height']
  weight = request.form['weight']
  overall_rating = request.form['overall_rating']
  potential = request.form['potential']
  team_id = request.form['potential']

  insert = players.insert().values(player_id=player_id, player_name=player_name, 
	 player_dob=player_dob, height=height, weight=weight, 
	 overall_rating=overall_rating, potential=potential, team_id=team_id)

  try:
    g.conn.execute(insert)
  except exc.SQLAlchemyError:
    return render_template('players.html', message='Insert failed.')
  return redirect('/players')

#Goalkeeper page
@app.route('/goal_keeper')
def goal_keeper():
  cursor = g.conn.execute('SELECT * FROM Players JOIN Goal_Keeper ON Players.player_id=Goal_Keeper.player_id ORDER BY player_name ASC')
  table = goal_keeper_view(cursor)
  cursor.close()
  return render_template('goal_keeper.html', table=table)

#Add goalkeeper 
@app.route('/add_goal_keeper', methods=['POST'])
def add_goal_keeper():
  goal_keeper = meta.tables['goal_keeper']
  player_id = request.form['player_id']
  gk_diving_rating = request.form['gk_diving_rating']
  gk_reflexes_rating = request.form['gk_reflexes_rating']
  
  insert = goal_keeper.insert().values(player_id=player_id, gk_diving_rating=gk_diving_rating, gk_reflexes_rating=gk_reflexes_rating)

  try:
    g.conn.execute(insert)
  except exc.SQLAlchemyError:
    return render_template('goal_keeper.html', message='Insert Failed')
  return redirect('/goal_keeper')

#Defender page
@app.route('/defender')
def defender():
  cursor = g.conn.edecute('SELECT * FROM Players JOIN Defender ON Players.player_id=Defender.player_id ORDER BY player_name ASC')
  table = defender_view(cursor)
  cursor.close()
  return render_template('defender.html', table=table)

#Add defender
@app.route('/add_defender', methods=['POST'])
def add_defender():
  defender = meta.tables['defender']
  player_id = request.form['player_id']
  aggression_rating = request.form['aggression_rating']
  marking_rating = request.form['marking_rating']
  
  insert = defender.insert().values(player_id=player_id, aggression_rating=aggression_rating, marking_rating=marking_rating)

  try:
    g.conn.execute(insert)
  except exc.SQLAlchemyError:
    return render_template('defender.html', message='Insert Failed')
  return redirect('/defender')

#Midfielder page
@app.route('/defender')
def defender():
  cursor = g.conn.edecute('SELECT * FROM Players JOIN Midfielder ON Players.player_id=Midfielder.player_id ORDER BY player_name ASC')
  table = defender_view(cursor)
  cursor.close()
  return render_template('midfielder.html', table=table)

#Add Midfielder
@app.route('/add_midfielder', methods=['POST'])
def add_defender():
  midfielder = meta.tables['midfielder']
  player_id = request.form['player_id']
  preferred_foot = request.form['preferred_foot']
  crossing_rating = request.form['crossing_rating']

  insert = midfielder.insert().values(player_id=player_id, preferred_foot=preferred_foot, crossing_rating=crossing_rating)

  try:
    g.conn.execute(insert)
  except exc.SQLAlchemyError:
    return render_template('midfielder.html', message='Insert Failed')
  return redirect('/midfielder')


#Forward page
@app.route('/forward')
def forward():
  cursor = g.conn.edecute('SELECT * FROM Players JOIN Forward ON Players.player_id=Forward.player_id ORDER BY player_name ASC')
  table = defender_view(cursor)
  cursor.close()
  return render_template('forward.html', table=table)

#Add Forward
@app.route('/add_forward', methods=['POST'])
def add_forward():
  forward = meta.tables['forward']
  player_id = request.form['player_id']
  sprint_speed_rating = request.form['sprint_speed_rating']
  shot_power_rating = request.form['shot_power_rating']

  insert = forward.insert().values(player_id=player_id, sprint_speed_rating=sprint_speed_rating, shot_power_rating=shot_power_rating)

  try:
    g.conn.execute(insert)
  except exc.SQLAlchemyError:
    return render_template('forward.html', message='Insert Failed')
  return redirect('/forward')


#Delete player
@app.route('/delete_player', methods=['POST'])
def delete_player():
  players = meta.tables['players']
  player_id = request.form['player_id']
  
  delete = players.delete().where(players.c.player_id==player_id)
 
  try:
    g.conn.execute(delete)
  except exc.SQLAlchemyError:
    return render_template('players.html', message='Delete failed')
  return redirect('/players')





@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()


if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using:

        python server.py

    Show the help text using:

        python server.py --help

    """

    HOST, PORT = host, port
    print "running on %s:%d" % (HOST, PORT)
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)


  run()