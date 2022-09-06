-- lists the number of records with the same score in the table second_table of the database hbtn_0c_0 
-- cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT score, count(score) AS number FROM second_table
GROUP BY score;
