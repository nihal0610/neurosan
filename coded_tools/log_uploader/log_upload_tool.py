from typing import Dict, Any, Union
from neuro_san.interfaces.coded_tool import CodedTool
import os

class FileUploaderTool(CodedTool):
    """
    A tool that reads the content of all files in a given folder and returns a dictionary of filename-content pairs.
    """
    def __init__(self):
        # Hardcoded folder path (update this path as needed)
        self.folder_path = "C:/Users/Administrator/Desktop/log_articles"
        print("... FileUploaderTool initialized with folder path:", self.folder_path)

    def invoke(self, args: Dict[str, Any], sly_data: Dict[str, Any]) -> Union[Dict[str, Any], str]:
        if not os.path.exists(self.folder_path) or not os.path.isdir(self.folder_path):
            return {"error": f"Folder not found: {self.folder_path}"}

        file_contents = {}
        try:
            for filename in os.listdir(self.folder_path):
                file_path = os.path.join(self.folder_path, filename)
                if os.path.isfile(file_path):
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        file_contents[filename] = content
            print(f"Read {len(file_contents)} files from folder: {self.folder_path}")
            return {"folder_contents": file_contents}
        except Exception as e:
            error_msg = f"Failed to read files from folder: {e}"
            print(error_msg)
            return {"error": error_msg}

    async def async_invoke(self, args: Dict[str, Any], sly_data: Dict[str, Any]) -> Union[Dict[str, Any], str]:
        return self.invoke(args, sly_data)
