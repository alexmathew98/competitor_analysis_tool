from crewai import Task
from textwrap import dedent

class CompetitorAnalysisTasks():
  # Task-1
  def research(self, agent, company):
    return Task(description=dedent(f"""
        Your task as the research agent is to search the web for competitor information including promotions.  You are to collect only what is required as part of your task and remove any unnecessary information not relevant to your assignment. Using our specific niche only collect and report information that will be beneficial for comparison. Your final answer is to be a summary of the relevant information you have found to be delivered to the data processing agent. Your final report must tell which product is the better option.
        
        
        Make sure to use the most recent data as possible.
  
        Selected company by the customer: {company}
      """),
      agent=agent,
      expected_output='From the research done develop a table to show side by side comparison between the latest iphone model and its competition in Canada in 2024.'
    )

  def data_processing(self, agent, company):
    return Task(description=dedent(f"""
        Your task is to collect and analyze the findings from the research agent. You are to know how to compare A to B and to scrape the remainder. When analyzing you must know what offers and promotions are relevant to our product and they must be a direct competitor. Products that are competitors but are not comparable with our products are not to be reported. Your final answer is to include a clean and detailed summary of your findings for comparison to progress. 
      """),
      agent=agent,
      expected_output='From the research done develop an analysis between the two companies and scrape any excess information not needed.'
      )

  def data_comparison(self, agent, company):
    return Task(description=dedent(f"""
        Analyze the data from the processing agent and compare with our products/offers. Use your search tool to see where we stand with the competition, do we require lots of work or are we on track? Compare price, promotion and the company as a whole to report findings and see how we compare to the competition. 
      """),
        agent=agent,
        expected_output='Your final answer must be a report on where we stand next to the competition and what we could potentially work on to compete.'
      )

  def data_reporting(self, agent, company):
    return Task(description=dedent(f"""
        Your task is to collect the information from the comparison agent and provide a report to the user on the findings. The report should be a detailed comparison on the competition and my company. It should include but not limited to pricing, promotions and offers company B has compared to us (company A). It should also include what can be worked on to be up to par with the competition but also things done right that should remain the same.  
      """),
                agent=agent,
                expected_output='From the research done create a report presenting all findings and show a detailed summary with an answer.'
      )
  # # Task-2
  # def financial_analysis(self, agent):
  #   return Task(description=dedent(f"""
  #       Conduct a thorough analysis of the stock's financial
  #       health and market performance.
  #       This includes examining key financial metrics such as
  #       P/E ratio, EPS growth, revenue trends, and
  #       debt-to-equity ratio.
  #       Also, analyze the stock's performance in comparison
  #       to its industry peers and overall market trends.
  #
  #       Your final report MUST expand on the summary provided
  #       but now including a clear assessment of the stock's
  #       financial standing, its strengths and weaknesses,
  #       and how it fares against its competitors in the current
  #       market scenario.{self.__tip_section()}
  #
  #       Make sure to use the most recent data possible.
  #     """),
  #     agent=agent,
  #     expected_output='A refined finalized analysis of the mentioned stock based on the details provided in the description'
  #     )
  #
  # # Task-3
  # def filings_analysis(self, agent):
  #   return Task(description=dedent(f"""
  #       Analyze the latest 10-Q and 10-K filings from EDGAR for
  #       the stock in question.
  #       Focus on key sections like Management's Discussion and
  #       Analysis, financial statements, insider trading activity,
  #       and any disclosed risks.
  #       Extract relevant data and insights that could influence
  #       the stock's future performance.
  #
  #       Your final answer must be an expanded report that now
  #       also highlights significant findings from these filings,
  #       including any red flags or positive indicators for
  #       your customer.
  #       {self.__tip_section()}
  #     """),
  #     agent=agent,
  #     expected_output='A refined finalized analysis of the mentioned stock based on the details provided in the description'
  #     )
  #
  # # Task-4
  # def recommend(self, agent):
  #   return Task(description=dedent(f"""
  #       Review and synthesize the analyses provided by the
  #       Financial Analyst and the Research Analyst.
  #       Combine these insights to form a comprehensive
  #       investment recommendation.
  #
  #       You MUST Consider all aspects, including financial
  #       health, market sentiment, and qualitative data from
  #       EDGAR filings.
  #
  #       Make sure to include a section that shows insider
  #       trading activity, and upcoming events like earnings.
  #
  #       Your final answer MUST be a recommendation for your
  #       customer. It should be a full super detailed report, providing a
  #       clear investment stance and strategy with supporting evidence.
  #       Make it pretty and well formatted for your customer.
  #       {self.__tip_section()}
  #     """),
  #     agent=agent,
  #     expected_output='A refined list of recommendtiones similiar to the mentioned stock based on the details provided in the description'
  #   )

  # def __tip_section(self):
  #   return "If you do your BEST WORK, I'll give you a $10,000 commission!"                 //TODO: Need to modify this

