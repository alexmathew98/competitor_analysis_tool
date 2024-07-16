from crewai import Crew
from textwrap import dedent

from competitor_analysis_agents import CompetitorAnalysisAgents
from competitor_analysis_tasks import CompetitorAnalysisTasks

from dotenv import load_dotenv
load_dotenv()

class FinancialCrew:
  def __init__(self, company):
    self.company = company

  def run(self):
    agents = CompetitorAnalysisAgents()
    tasks = CompetitorAnalysisTasks()

    research_analyst_agent = agents.research_agent()
    data_processing_agent = agents.processing_agent()
    data_comparison_agent = agents.analysis_agent()
    data_reporting_agent = agents.reporting_agent()

    research_task = tasks.research(research_analyst_agent, self.company)
    data_processing_task = tasks.data_processing(data_processing_agent, self.company)
    data_comparison_task = tasks.data_comparison(data_comparison_agent,self.company)
    data_reporting_task = tasks.data_reporting(data_reporting_agent, self.company)


    crew = Crew(
      agents=[
        research_analyst_agent,
        data_processing_agent,
        data_comparison_agent,
        data_reporting_agent
      ],
      tasks=[
        research_task,
        data_processing_task,
        data_comparison_task,
        data_reporting_task
      ],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to Competitor Analysis Crew")
  print('-------------------------------')
  company = input(
    dedent("""
      What is the competition company you want to analyze?
    """))
  
  financial_crew = FinancialCrew(company)
  result = financial_crew.run()
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)
