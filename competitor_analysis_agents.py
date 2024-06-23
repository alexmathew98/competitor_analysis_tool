from crewai import Agent

from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
from tools.sec_tools import SECTools
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool

# Test
import os
os.environ["OPENAI_API_KEY"] = "sk-proj-teEaMucAlXCFs2vbaWTHT3BlbkFJadJSIYWF3lFP4SjNGeqM"   #Need to hide API keys from here
os.environ['OPENAI_MODEL_NAME'] = 'gpt-3.5-turbo-0125'

class StockAnalysisAgents():
  # Agent-1: Data collection Agent
  def data_collection_agent(self):
    return Agent(
      role='The Best Financial Analyst',
      goal="""Impress all customers with your financial data 
      and market trends analysis""",
      backstory="""The most seasoned financial analyst with 
      lots of expertise in stock market analysis and investment
      strategies that is working for a super important customer.""",
      verbose=True,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        CalculatorTools.calculate,
        SECTools.search_10q,
        SECTools.search_10k
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