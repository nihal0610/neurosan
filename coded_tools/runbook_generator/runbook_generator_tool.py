from typing import Dict, Any, Union
from neuro_san.interfaces.coded_tool import CodedTool

class RunbookGeneratorTool(CodedTool):
    """
    Generates a runbook using uploaded logs and knowledge base content.
    """

    def __init__(self):
        print("... RunbookGeneratorTool initialized ...")

    def invoke(self, args: Dict[str, Any], sly_data: Dict[str, Any]) -> Union[str, Dict[str, Any]]:
        logs = args.get("logs", "")
        kb_content = args.get("kb_content", "")
        incident_summary = args.get("summary", "")

        prompt = (
            f"You are a Site Reliability Engineer. Based on the following:\n"
            f"Incident Summary:\n{incident_summary}\n\n"
            f"Logs:\n{logs[:1000]}\n\n"
            f"Knowledge Base:\n{kb_content[:1000]}\n\n"
            f"Generate a step-by-step diagnostic and resolution runbook in Markdown format."
        )

        return {"prompt": prompt}
