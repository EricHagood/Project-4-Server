The back end of this server is build in Python using flask to create a SQLite3 database. 
I had a difficult time deploying this to heroku and the issue turned out to be during the initialization two commands with the DATABASE were creating a race condition that was causing the app to crash. I fixed this by simply adding a sleep timer in the initialize method.
