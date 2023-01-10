import psycopg2

class DBIntegration:

    def connect(self):
        pass



class PostgressDB(DBIntegration):

    conn = None

    def __init__(self):
        conn = psycopg2.connect(host="localhost",
                            database="harshtiwari",
                            user="tutorial_dag",
                            password="password")