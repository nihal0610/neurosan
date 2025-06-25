from typing import Dict, Any, Union
from neuro_san.interfaces.coded_tool import CodedTool

class SQLQueryGeneratorTool(CodedTool):
    def invoke(self, args: Dict[str, Any], sly_data: Dict[str, Any]) -> Union[Dict[str, Any], str]:
        user_input = args.get("user_input")
        if not user_input:
            return "Error: 'user_input' argument is required."

        query = f"SELECT * FROM customers WHERE city = '{user_input}'"
        return {"query": query}

    async def async_invoke(self, args, sly_data):
        return self.invoke(args, sly_data)
