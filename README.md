##Project Description:
This project is used to make analysis on large data and try to get info by using queries and this is the first project in Full-stack Nanodegree.
###
##Requirment:
- Vagrant.
- virtualbox.
- Python 3.6
- PostgreSQL.
- psycopg2
###
##
##Database that used:
- we used news database that provide there tables that we used ('author,articles,log).
##Function that return data from "news"
There are three functions that read from news database **'author,article,log'** :
- **view_popular_three_article()**: this function for select three top article from articles table.
- **view_most_pop_article_author()**:this function for select three pop author from authors table.
- **view_log_state()**: this function for view more than 1% of requests lead to errors.
##Create View for Error State:
- ```sql 
       create view all_status as
       select count(log.status)as total_state, date(log."time") as time_ 
       from log  group by time_ ;
     ```
######
- ```sql 
        create view error_status as 
        select count(log.status)as total_error_state, date(log."time") as time_ 
        from log where log.status like '404%'  group by time_;
     ```