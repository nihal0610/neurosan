from typing import Dict, Any, Union
from neuro_san.interfaces.coded_tool import CodedTool

class ResponseGeneratorTool(CodedTool):
    def invoke(self, args: Dict[str, Any], sly_data: Dict[str, Any]) -> Union[str, Dict[str, Any]]:
        result = args.get("result")
        columns = args.get("columns")
        if not result:
            return "No records found."

        response_lines = []
        for row in result:
            row_text = ", ".join(f"{col}: {val}" for col, val in zip(columns, row))
            response_lines.append(row_text)

        final_response = "\n".join(response_lines)
        return {"response": final_response}

    async def async_invoke(self, args, sly_data):
        return self.invoke(args, sly_data)
