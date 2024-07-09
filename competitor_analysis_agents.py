from crewai import Agent
#Old
#from tools.browser_tools import BrowserTools
#from tools.calculator_tools import CalculatorTools
#from tools.search_tools import SearchTools
#from tools.sec_tools import SECTools

#New
from prototype_tools.search_tools_MK0 import SearchTools
from prototype_tools.browser_tools_MK0 import BrowserTools

from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool

# Test
import os
os.environ["OPENAI_API_KEY"] = "sk-proj-teEaMucAlXCFs2vbaWTHT3BlbkFJadJSIYWF3lFP4SjNGeqM"   #Need to hide API keys from here
os.environ['OPENAI_MODEL_NAME'] = 'gpt-4o'

class CompetitorAnalysisAgents():
  # Agent-1: Data collection Agent
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

  # # Agent-2: Processing Agent
  # def processing_agent(self):
  #   return Agent(
  #     role='Staff Research Analyst',
  #     goal="""Being the best at gather, interpret data and amaze
  #     your customer with it""",
  #     backstory="""Known as the BEST research analyst, you're
  #     skilled in sifting through news, company announcements,
  #     and market sentiments. Now you're working on a super
  #     important customer""",
  #     verbose=True,
  #     tools=[
  #       BrowserTools.scrape_and_summarize_website,
  #       SearchTools.search_internet,
  #       SearchTools.search_news,
  #       YahooFinanceNewsTool(),
  #       SECTools.search_10q,
  #       SECTools.search_10k
  #     ]
  #   )
  #
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