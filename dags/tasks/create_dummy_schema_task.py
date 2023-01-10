
from integrations.db_integration import DBIntegration
from integrations.db_integration import PostgressDB

def create_dummy_schema():

    db_instance = PostgressDB()
    
    # Create a cursor object

    table_name = "harsh"
    columns = "id SERIAL PRIMARY KEY, num INT, square_num INT"

    print("Here", db_instance)

    # Execute a SQL query
    db_instance.executeSQLStatement(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")

