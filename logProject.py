import psycopg2


def view_popular_three_article():
    db = psycopg2.connect(database='news')
    cur = db.cursor()
    query = "select title,count(title) as total from articles join log on " \
            " log.path=concat('/article/',articles.slug)group by title order by total desc limit 3; "
    cur.execute(query)
    data = cur.fetchall()
    db.close()
    print("View popular three article :")
    for row in data:
        print(str(row[0]) + "-" + str(row[1]) + " " + "views")


def view_most_pop_article_author():
    db = psycopg2.connect(database='news')
    cur = db.cursor()
    query = "select name,count(articles.title) as total from authors join articles on " \
            " authors.id=articles.author join log on log.path=concat('/article/',articles.slug) " \
            " group by name order by total desc limit 3;"
    cur.execute(query)
    data = cur.fetchall()
    db.close()
    print("View most pop article author :")
    for row in data:
        print(str(row[0]) + str(row[1]) + " " + "views")


def view_log_state():
    db = psycopg2.connect(database='news')
    cur = db.cursor()
    cur.execute("select all_status.time_,round((100.0*error_status.total_error_state/all_status.total_state),2) as per "
                " from error_status,all_status where "
                " error_status.time_=all_status.time_ "
                " and round((100.0*error_status.total_error_state/all_status.total_state),2) > 0.01 "
                " order by all_status.time_  desc;")
    data = cur.fetchall()
    db.close()
    print("View log state :")
    for row in data:
        print(str(row[0]) + " - " + str(row[1]) + "%")


view_popular_three_article()
print('\n')
view_most_pop_article_author()
print('\n')
view_log_state()
print('\n')
print("End of App.")
