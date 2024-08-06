from crewai import Agent

#New
from tools.search_tools import SearchTools
from tools.browser_tools import BrowserTools

# Test - Needs to be set in env file
import os
os.environ["OPENAI_API_KEY"] = "sk-proj-9KGThuxIwfFMg7CQ3yLVT3BlbkFJxLaqnD2gUiDnGYUt67BO"   #Need to hide API keys from here
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
       verbose=True
     )
  #Agent-2(MK2): Processing Agent
  # Data-processing agent - coding based - need to remove tools and describe it via tasks and input
  def processing_agent_coding(self):
     return Agent(
       role='Data Processing Specialist',
       goal="""Process and analyze scraped data from research agent’s finding for competitor analysis and determine what’s best needed data for this scenario.Use Python to clean, filter, and visualize the data which will be passed for the report data. 
                and generate comprehensive reports""",
       backstory="""You are an expert in data processing and analysis, skilled at identifying relevant data points, filtering out noise, and generating insightful reports.You have strong knowledge of Python libraries  such as pandas, NumPy, and matplotlib for data manipulation, statistical analysis, and visualization.""",
       verbose=True,
       allow_code_execution=True
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
       verbose=True
     )