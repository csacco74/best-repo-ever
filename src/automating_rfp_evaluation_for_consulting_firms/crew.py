from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import DirectoryReadTool
from crewai_tools import PDFSearchTool
from crewai_tools import DOCXSearchTool
from crewai_tools import CSVSearchTool
from crewai_tools import TXTSearchTool

@CrewBase
class AutomatingRfpEvaluationForConsultingFirmsCrew():
    """AutomatingRfpEvaluationForConsultingFirms crew"""

    @agent
    def info_extraction_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['info_extraction_agent'],
            tools=[DirectoryReadTool(), PDFSearchTool(), DOCXSearchTool(), CSVSearchTool(), TXTSearchTool()],
        )

    @agent
    def categorization_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['categorization_agent'],
            tools=[],
        )

    @agent
    def summarization_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['summarization_agent'],
            tools=[],
        )

    @agent
    def senior_bid_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_bid_manager'],
            tools=[],
        )

    @agent
    def email_preparation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['email_preparation_agent'],
            tools=[],
        )


    @task
    def read_documents_task(self) -> Task:
        return Task(
            config=self.tasks_config['read_documents_task'],
            tools=[DirectoryReadTool()],
        )

    @task
    def extract_information_task(self) -> Task:
        return Task(
            config=self.tasks_config['extract_information_task'],
            tools=[PDFSearchTool(), DOCXSearchTool(), CSVSearchTool(), TXTSearchTool()],
        )

    @task
    def categorize_information_task(self) -> Task:
        return Task(
            config=self.tasks_config['categorize_information_task'],
            tools=[],
        )

    @task
    def summarize_information_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_information_task'],
            tools=[],
        )

    @task
    def review_and_integrate_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_and_integrate_task'],
            tools=[],
        )

    @task
    def prepare_email_task(self) -> Task:
        return Task(
            config=self.tasks_config['prepare_email_task'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the AutomatingRfpEvaluationForConsultingFirms crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
