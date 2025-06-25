from typing import Dict, Any, Union
import mysql.connector
from mysql.connector import Error
from neuro_san.interfaces.coded_tool import CodedTool

class MySQLExecutorTool(CodedTool):
    def __init__(self, parameters=None):
        # Hardcoded config for now
        self.host = "localhost"
        self.user = "root"
        self.password = "chotu0610"
        self.database = "production_line"

        print(f"MySQLExecutorTool initialized for DB: {self.database} on {self.host}")

    def invoke(self, args: Dict[str, Any], sly_data: Dict[str, Any]) -> Union[Dict[str, Any], str]:
        query = args.get("query")
        if not query:
            return "Error: 'query' argument is required."

        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            cursor = connection.cursor()

            print(f"Executing query on {self.database}: {query}")

            cursor.execute(query)
            result = cursor.fetchall()

            columns = [desc[0] for desc in cursor.description] if cursor.description else []

            cursor.close()
            connection.close()

            return {
                "status": "success",
                "columns": columns,
                "result": result
            }

        except Error as e:
            print(f"MySQL error: {e}")
            return f"Error: {str(e)}"

    async def async_invoke(self, args, sly_data):
        return self.invoke(args, sly_data)
