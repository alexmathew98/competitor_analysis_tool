from crewai import Task
from textwrap import dedent

class CompetitorAnalysisTasks():

  """
  Task-1: Research competitor information.

  Parameters:
  agent (str): The agent responsible for performing the task.
  company (str): The company to be researched.

  Returns:
  Task: A Task object containing the description and expected output of the research task.

  Description:
  The research agent is to search the web for competitor information, including promotions.
  They should collect only relevant information and provide a summary that will be delivered
  to the data processing agent. The final report must tell which product is the better option,
  using the most recent data available.

  Expected Output:
  A table showing a side-by-side comparison between the latest iPhone model in Canada in 2024 and its competition.
  """
  def research(self, agent, company):
    return Task(description=dedent(f"""
        Your task as the research agent is to search the web for competitor information including promotions.  You are to collect only what is required as part of your task and remove any unnecessary information not relevant to your assignment. Using our specific niche only collect and report information that will be beneficial for comparison. Your final answer is to be a summary of the relevant information you have found to be delivered to the data processing agent.Very important to keep in mind that we have to limit the searches to the relevant product for comparison which is phones. Your final report must tell which product is the better option.
        
        Make sure to use the most recent data as possible.
        Selected company by the customer: {company}
      """),
      agent=agent,
      expected_output='From the research done develop a table to show side by side comparison between the latest iphone model and its competition in Canada in 2024.Also show the compiled data in the list format to be sent to the processing agent'
    )

  """
  Task-2: Process and analyze research findings.

  Parameters:
  agent (str): The agent responsible for performing the task.
  company (str): The company whose data is being processed.

  Returns:
  Task: A Task object containing the description and expected output of the data processing task.

  Description:
  The data processing agent collects and analyzes findings from the research agent. They should compare
  relevant offers and promotions and provide a clean, detailed summary of their findings for further comparison.

  Expected Output:
  An analysis comparing the two companies, with excess information removed.
  """
  def data_processing(self, agent, company):
    return Task(description=dedent(f"""
        Your task is to process and clean the findings from the research agent. Use Python to remove duplicates and irrelevant data, focusing on relevant data points for comparison of our products (A) with competitor products (B). Filter out non-comparable products, and highlight key offers and promotions pertinent to our products. Ensure the processed data is well-organized and ready for further analysis and comparison by the next data analysis agent. Provide a clear and concise summary of your findings.Use Python to clean, filter, and visualize the data which will be passed for the report data.You have strong knowledge of Python libraries  such as pandas, NumPy, and matplotlib for data manipulation, statistical analysis
        """),
      agent=agent,
      expected_output='From the research done develop an analysis between the two companies and scrape any excess information not needed.'
    )

  """
  Task-3: Compare processed data with our products.

  Parameters:
  agent (str): The agent responsible for performing the task.
  company (str): The company being compared.

  Returns:
  Task: A Task object containing the description and expected output of the data comparison task.

  Description:
  The data comparison agent analyzes data from the processing agent and compares it with our products/offers.
  They should use their search tool to evaluate where we stand with the competition and provide a report on 
  how we compare in terms of price, promotion, and overall company standing.

  Expected Output:
  A report on our standing next to the competition and potential areas for improvement.
  """
  def data_comparison(self, agent, company):
    return Task(description=dedent(f"""
        Analyze the data from the processing agent and compare with our products/offers. Use your search tool to see where we stand with the competition, do we require lots of work or are we on track? Compare price, promotion and the company as a whole to report findings and see how we compare to the competition. 
      """),
      agent=agent,
      expected_output='Your final answer must be a report on where we stand next to the competition and what we could potentially work on to compete.'
    )

  """
  Task-4: Report findings to the user.

  Parameters:
  agent (str): The agent responsible for performing the task.
  company (str): The company being reported on.

  Returns:
  Task: A Task object containing the description and expected output of the data reporting task.

  Description:
  The data reporting agent collects information from the comparison agent and provides a detailed report to the user
  on the findings. The report should include a comparison on pricing, promotions, and offers between the competition 
  and our company, as well as suggestions for improvement and strengths to maintain.

  Expected Output:
  A detailed summary report presenting all findings and showing a detailed comparison with an answer.
  """
  def data_reporting(self, agent, company):
    return Task(description=dedent(f"""
        Your task is to collect the information from the comparison agent and provide a report to the user on the findings. The report should be a detailed comparison on the competition and my company. It should include but not limited to pricing, promotions and offers company B has compared to us (company A). It should also include what can be worked on to be up to par with the competition but also things done right that should remain the same.  
      """),
        agent=agent,
        expected_output='From the research done create a report presenting all findings and show a detailed summary with an answer.'
    )
