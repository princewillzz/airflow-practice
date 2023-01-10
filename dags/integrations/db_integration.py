import psycopg2

class DBIntegration:

    def connect(self):
        pass

    def executeSQLStatement(self, sqlStatement: str):
        pass



class PostgressDB(DBIntegration):

    conn = None

    def __init__(self):
        self.conn = psycopg2.connect(host="localhost",
                            database="harshtiwari",
                            user="tutorial_dag",
                            password="password")

    def executeSQLStatement(self, sqlStatement: str):

        cursor = self.conn.cursor()

        cursor.execute(sqlStatement)

        self.conn.commit()

        cursor.close()

    
    def __del__(self):
        if self.conn:
            self.conn.close()