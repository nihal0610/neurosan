from typing import Dict, Any, Union
from datetime import datetime
from neuro_san.interfaces.coded_tool import CodedTool


class CurrentTimeTool(CodedTool):
    """
    A simple tool that returns the current datetime.
    """

    def __init__(self):
        print("... CurrentTimeTool initialized ...")

    def invoke(self, args: Dict[str, Any], sly_data: Dict[str, Any]) -> Union[Dict[str, Any], str]:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"The current time is {now}."
        print(message)
        return message

    async def async_invoke(self, args: Dict[str, Any], sly_data: Dict[str, Any]) -> Union[Dict[str, Any], str]:
        return self.invoke(args, sly_data)
