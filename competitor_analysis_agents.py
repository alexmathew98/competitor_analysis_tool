from crewai import Agent
#Old
#from tools.browser_tools import BrowserTools
#from tools.calculator_tools import CalculatorTools
#from tools.search_tools import SearchTools
#from tools.sec_tools import SECTools

#New
from prototype_tools.search_tools_MK0 import SearchTools
from prototype_tools.browser_tools_MK0 import BrowserTools
from prototype_tools.processing_tool import DataProcessingTool
# from prototype_tools.analysis_tools_MK0 import ComparisonTool


# Test
import os
os.environ["OPENAI_API_KEY"] = "sk-proj-9KGThuxIwfFMg7CQ3yLVT3BlbkFJxLaqnD2gUiDnGYUt67BO"   #Need to hide API keys from here
os.environ['OPENAI_MODEL_NAME'] = 'gpt-4o'

class CompetitorAnalysisAgents():
  # Agent-1: Data collection Agent
  def research_agent(self):
    return Agent(
      role='The Best Competitor Research Analyst',
      goal="""Scrape data from competitor websites including prices, offers, and promotions. Research local competition to provide best analysis on competitors prices and promotions. Compare to the mobile products from Apple. Use apple.ca to do your research for apple iphones.""",
      backstory="""Trained researcher ,highly skilled in analyzing and comparing market trends from apple.com to the competition..""",
      verbose=True,
      tools=[
        SearchTools.search_internet,
        SearchTools.search_prices,
        BrowserTools.scrape_and_summarize_website,
      ]
    )

  #Agent-2: Processing Agent
  def processing_agent(self):
     return Agent(
       role='Data processing agent',
       goal="""Analyze the research agent’s finding and determine what’s best needed data for this scenario""",
       backstory="""Skilled in processing data and only providing useful and relevant information to the task""",
       verbose=True,
       tools=[
         DataProcessingTool.preprocess_data,
         DataProcessingTool.organize_data,
         DataProcessingTool.aggregate_data,
       ]
     )
  #Agent-3: Reporting Agent
  def reporting_agent(self):
     return Agent(
       role='Generate comprehensive reports on findings.',
       goal="""Summarize findings in a user friendly way""",
       backstory="""After receiving the processed and analyzed data,generate a report to showcase all findings to report back to user""",
       verbose=True,

      )

  #Agent-4: Analysis Agent
  def analysis_agent(self):
     return Agent(
       role='Price comparison agent',
       goal="""Compare findings from data processing agent based on specific input data/prices we provide.Compare competitor prices with your own and identify pricing strategies. """,
       backstory="""Skilled in competitor analysis, based on analyzing price and promotion from competition and compare with our own""",
       verbose=True,
       tools=[
         SearchTools.search_internet,
         # ComparisonTool.compare_prices,
       ]
     )
  # # Agent-3: Reporting Agent
  # def reporting_agent(self):
  #   return Agent(
  #     role='Private Investment Advisor',
  #     goal="""Impress your customers with full analyses over stocks
  #     and completer investment recommendations""",
  #     backstory="""You're the most experienced investment advisor
  #     and you combine various analytical insights to formulate
  #     strategic investment advice. You are now working for
  #     a super important customer you need to impress.""",
  #     verbose=True,
  #     tools=[
  #       BrowserTools.scrape_and_summarize_website,
  #       SearchTools.search_internet,
  #       SearchTools.search_news,
  #       CalculatorTools.calculate,
  #       YahooFinanceNewsTool()
  #     ]
  #   )