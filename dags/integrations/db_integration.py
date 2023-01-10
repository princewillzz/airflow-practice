import psycopg2

class DBIntegration:

    def connect(self):
        pass

    def executeSQLStatement(self, sqlStatement: str):
        pass

    def fetch_data_from_db(self, sqlStatement: str, many=False):
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

    def fetch_data_from_db(self, sqlStatement: str, many=False):

        cursor = self.conn.cursor()
        cursor.execute(sqlStatement)

        records = None

        if many:
            records = cursor.fetchall()
        
        records = cursor.fetchone()

        cursor.close()

        return records


    
    def __del__(self):
        if self.conn:
            self.conn.close()