# SQL - more queries

Files

* 0-privileges.sql - a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
	* to run 
			cat 0-privileges.sql | mysql -hlocalhost -uroot -p
	* output will be no ....
	* create user and try agian to do this
		* $echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
		* $ echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
		* cat 0-privileges.sql | mysql -hlocalhost -uroot -p
* 1-create_user.sql -  a script that creates the database hbtn_0d_2 and the user user_0d_2.
* 3-force_name.sql -  a script that creates the table force_name on your MySQL server.
* 4-never_empty.sql - a script that creates the table id_not_null on your MySQL server.
* 5-unique_id.sql -  a script that creates the table unique_id on your MySQL server.


* 6-states.sql -  script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
* 7-cities.sql - a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
* 8-cities_of_california_subquery.sql - a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
* 9-cities_by_state_join.sql -  script that lists all cities contained in the database hbtn_0d_usa.
* 10-genre_id_by_show.sql - Import the database dump from hbtn_0d_tvshows to your MySQL server: download
* 11-genre_id_all_shows.sql - 
* 12-no_genre.sql 
* 13-count_shows_by_genre.sql
* 14-my_genres.sql
*  15-comedy_only.sql
* 16-shows_by_genre.sql
