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
    # financial_analyst_agent = agents.financial_analyst()
    # investment_advisor_agent = agents.investment_advisor()

    research_task = tasks.research(research_analyst_agent, self.company)
    data_processing_task = tasks.research(data_processing_agent, self.company)

    # financial_task = tasks.financial_analysis(financial_analyst_agent)
    # filings_task = tasks.filings_analysis(financial_analyst_agent)
    # recommend_task = tasks.recommend(investment_advisor_agent)

    crew = Crew(
      agents=[
        research_analyst_agent,
        data_processing_agent
        # investment_advisor_agent
      ],
      tasks=[
        research_task,
        data_processing_task
        # filings_task,
        # recommend_task
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
