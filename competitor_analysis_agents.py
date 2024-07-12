from crewai import Agent

#New
from tools.search_tools_MK0 import SearchTools
from tools.browser_tools_MK0 import BrowserTools
from tools.processing_tool import DataProcessingTool
# from tools.analysis_tools_MK0 import ComparisonTool

# Test - Needs to be set in env file
import os
os.environ["OPENAI_API_KEY"] = "sk-proj-teEaMucAlXCFs2vbaWTHT3BlbkFJadJSIYWF3lFP4SjNGeqM"   #Need to hide API keys from here
os.environ['OPENAI_MODEL_NAME'] = 'gpt-4o'

class CompetitorAnalysisAgents():
  # Agent-1: Research Agent
  """
  Description:
  The research agent is tasked with scraping data from competitor websites, including prices, offers, and promotions.
  The agent is specifically focused on comparing mobile products from Apple to local competition using the apple.com website.
  """
  def research_agent(self):
    return Agent(
      role='The Best Competitor Research Analyst',
      goal="""Scrape data from competitor websites including prices, offers, and promotions. Research local competition to provide best analysis on competitors prices and promotions. Compare to the mobile products from Apple. Use apple.com to do your research for apple iphones.""",
      backstory="""Trained researcher ,highly skilled in analyzing and comparing market trends from apple.com to the competition..""",
      verbose=True,
      tools=[
        SearchTools.search_internet,
        SearchTools.search_prices,
        BrowserTools.scrape_and_summarize_website,
      ]
    )

  #Agent-2: Processing Agent
  """
  Description:
  The processing agent analyzes the findings from the research agent and determines the most relevant data for the scenario.
  The agent is skilled in processing data and providing only useful and relevant information for the task.
  """
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
  """
  Description:
  The reporting agent generates comprehensive reports on the findings. 
  The agent summarizes the processed and analyzed data in a user-friendly manner.
  """
  def reporting_agent(self):
     return Agent(
       role='Generate comprehensive reports on findings.',
       goal="""Summarize findings in a user friendly way""",
       backstory="""After receiving the processed and analyzed data,generate a report to showcase all findings to report back to user""",
       verbose=True,

      )

  #Agent-4: Analysis Agent
  """
  Description:
  The analysis agent compares the findings from the data processing agent based on specific input data and prices provided. 
  The agent identifies pricing strategies by comparing competitor prices with our own.
  """
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