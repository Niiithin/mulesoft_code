import sqlite3 as sql

connection = sql.connect("movies.db")

cursor = connection.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS MOVIES( NAME TEXT, ACTOR TEXT, ACTRESS TEXT,DIRECTOR_NAME TEXT, YEAR INTEGER )")
cursor.execute(
    "INSERT INTO MOVIES VALUES('Interstellar','Mathew Macconaghey','Anne Hathway','Christoper Nolan',2014)")
cursor.execute(
    "INSERT INTO MOVIES VALUES('Dune','Timothée Chalamet','Rebecca Ferguson','Denis Villeneuve',2021)")
cursor.execute(
    "INSERT INTO MOVIES VALUES('Fight Club','Brad Pitt','Bonnie Carter','David FIncher',1999)")
cursor.execute(
    "INSERT INTO MOVIES VALUES('Saving Private Ryan','Tom Hanks','Matt Damon','Steven Spielberg',1993)")
cursor.execute(
    "INSERT INTO MOVIES VALUES('Jurasic World','Chris Pratt','Bryce Dallas Howard','Colin Trevv',2015)")
cursor.execute(
    "INSERT INTO MOVIES VALUES('The Curious Case of Benjamin Button','Brad Pitt','Cate Blanchet','David Fincher',2008)")


movie_name = cursor.execute("SELECT * FROM MOVIES").fetchall()
for i in movie_name:
    title, actor, actress, director, released_year = i
    print(f"Title = {title}, Actor = {actor}, Actress = {actress}, Director = {director}, Release Year = {released_year}")

print("ACTOR QUERY")
actor_name = cursor.execute(
    "SELECT * FROM MOVIES WHERE ACTOR = 'Brad Pitt'").fetchall()
for i in actor_name:
    title, actor, actress, director, released_year = i
    print(f"Title = {title}, Actor = {actor}, Actress = {actress}, Director = {director}, Release Year = {released_year}")
