from typing import Dict, Any, Union
from neuro_san.interfaces.coded_tool import CodedTool

class ResponseDisplayerTool(CodedTool):
    def invoke(self, args: Dict[str, Any], sly_data: Dict[str, Any]) -> Union[str, Dict[str, Any]]:
        response = args.get("response")
        if not response:
            return "Error: No response to display."
        print(f"User Response:\n{response}")
        return response

    async def async_invoke(self, args, sly_data):
        return self.invoke(args, sly_data)
