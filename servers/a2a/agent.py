
"""
crewAI agents for an A2A server example
"""

# Copyright (C) 2023-2025 Cognizant Digital Business, Evolutionary AI.
# All Rights Reserved.
# Issued under the Academic Public License.
#
# You can be released from the terms, and requirements of the Academic Public
# License by purchasing a commercial license.
# Purchase of a commercial license is mandatory for any use of the
# neuro-san SDK Software in commercial settings.
#
# END COPYRIGHT

# pylint: disable=import-error
from crewai import Agent
from crewai import Crew
from crewai import LLM
from crewai import Task


class CrewAiResearchReport:
    """
    Use CrewAI to perform research via web search and generate a report.

    This example is adapted from https://docs.crewai.com/quickstart,
    but does not use any tools.
    """

    def __init__(self):

        # LLM for agents
        llm = LLM(model="gpt-4o-mini")

        # Agents are researcher and reporting_analyst
        researcher = Agent(
            role="{topic} Senior Researcher",
            goal="Uncover cutting-edge developments in {topic}",
            backstory=(
                "You're a seasoned researcher with a knack for uncovering the "
                "latest developments in {topic}. Known for your ability to "
                "find the most relevant information and present it in a clear "
                "and concise manner."
            ),
            llm=llm,
            verbose=False
        )

        reporting_analyst = Agent(
            role="{topic} Reporting Analyst",
            goal=(
                "Create detailed reports based on {topic} data analysis and "
                "research findings"
            ),
            backstory=(
                "You're a meticulous analyst with a keen eye for detail. "
                "You're known for your ability to turn complex data into "
                "clear and concise reports, making it easy for others to "
                "understand and act on the information you provide."
            ),
            llm=llm,
            verbose=False
        )

        # researcher conducts research while reporting_analyst write a report
        research_task = Task(
            description=(
                "Conduct a thorough research about {topic} "
                "Make sure you find any interesting and relevant information "
            ),
            expected_output=(
                "A list with 10 bullet points of the most relevant information"
                " about {topic}"
            ),
            agent=researcher
        )

        reporting_task = Task(
            description=(
                "Review the context you got and expand each topic into a full "
                "section for a report. Make sure the report is detailed and "
                "contains any and all relevant information."
            ),
            expected_output=(
                "A fully fledge reports with the mains topics, each with a "
                "full section of information. Formatted as markdown "
                "without '```'"
            ),
            agent=reporting_analyst
        )

        # Put agents and tasks into crew
        self.crew = Crew(
            agents=[researcher, reporting_analyst],
            tasks=[research_task, reporting_task],
            verbose=True
        )

    async def ainvoke(self, topic: str) -> str:
        """
        Execute the run with given topic.
        :param topic: Topic for crew to do research and write report.

        :return: Report on the topic.
        """
        inputs = {'topic': topic}
        result = await self.crew.kickoff_async(inputs=inputs)

        return result.raw
