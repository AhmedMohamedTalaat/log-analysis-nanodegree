#!/usr/bin/python3.6
import psycopg2


def execute_query(query):
    try:
        db = psycopg2.connect(database='news')
        cur = db.cursor()
        cur.execute(query)
        result = cur.fetchall()
        db.close()
        return result
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)


def view_popular_three_article():
    """This function for view popular three articles from articles table"""
    query = """
            select title,count(title) as total from articles join log on 
            log.path=concat('/article/',articles.slug)group by title order by total desc limit 3;
            """
    data = execute_query(query)
    print("* View popular three article :")
    for row in data:
        print('"{}" - {} views'.format(str(row[0]), str(row[1])))


def view_most_pop_article_author():
    """This function for view most populart articles for authors from articles and author tables"""
    query = """
            select name,count(articles.title) as total from authors join articles on 
            authors.id=articles.author join log on log.path=concat('/article/',articles.slug)
            group by name order by total desc limit 3;
            """
    data = execute_query(query)
    print("* View most pop article author :")
    for row in data:
        print('"{}" - {} views'.format(str(row[0]), str(row[1])))


def view_log_state():
    """This function for printing error persentage that exceed 1%"""
    query = """
                select all_status.time_,round((100.0*error_status.total_error_state/all_status.total_state),2) as per 
                from error_status,all_status where 
                error_status.time_=all_status.time_ 
                and round((100.0*error_status.total_error_state/all_status.total_state),2) > 1
                order by all_status.time_  desc;
             """
    data = execute_query(query)
    print("* View log state :")
    for row in data:
        print('{} - {}% errors'.format(str(row[0]), str(row[1])))


if __name__ == '__main__':
    view_popular_three_article()
    print('\n')
    view_most_pop_article_author()
    print('\n')
    view_log_state()
    print('\n')
    print("End of App.")
