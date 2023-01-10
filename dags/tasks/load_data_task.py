
from integrations.db_integration import PostgressDB

def load_data():
    # Connect to the database
    db_instance = PostgressDB()

    # execute statement
    for index in range(1, 11):
        # Execute a SQL query
        db_instance.executeSQLStatement(f"INSERT INTO harsh (num, square_num) values({index}, {index**2})")

