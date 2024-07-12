# AI Crew for Competitor Analysis
## Introduction
This project is an example using the CrewAI frameworka comprehensive AI agent team for e-commerce vendors to automate the process of competitor analysis..

## Details
The AI agents will continuously monitor local competitors' pricing, offers, and promotions across multiple online platforms. The system will generate detailed reports that include competitive pricing strategies, promotional trends, and market positioning. Additionally, the AI agents will provide actionable recommendations for vendors to enhance their competitive edge by suggesting optimal pricing, discount strategies, and marketing tactics.

- [CrewAI Framework](#crewai-framework)
- [Running the script](#running-the-script)
- [Details & Explanation](#details--explanation)
- [Using GPT 3.5](#using-gpt-35)
- [Using Local Models with Ollama](#using-local-models-with-ollama)
- [Contributing](#contributing)
- [Support and Contact](#support-and-contact)
- [License](#license)

## CrewAI Framework
CrewAI is designed to facilitate the collaboration of role-playing AI agents. In this example, these agents work together to choose between different of cities and put together a full itinerary for the trip based on your preferences.

## Running the Script
It uses GPT-4 by default so you should have access to that to run it.

***Disclaimer:** This will use gpt-4 unless you changed it 
not to, and by doing so it will cost you money.*

- **Configure Environment**: Copy ``.env.example` and set up the environment variables for [Browseless](https://www.browserless.io/), [Serper](https://serper.dev/) and [OpenAI](https://platform.openai.com/api-keys)
- **Install Dependencies**: Run `poetry install --no-root`.
- **Execute the Script**: Run `poetry run python3 main.py` and input your idea.

## Details & Explanation
- **Running the Script**: Execute `python main.py`` and input your idea when prompted. The script will leverage the CrewAI framework to process the idea and generate a landing page.
- **Key Components**:
  - `./main.py`: Main script file.
  - `./competitor_analysis_tasks.py`: Main file with the tasks prompts.
  - `./competitor_analysis_agents.py`: Main file with the agents creation.
  - `./tools`: Contains tool classes used by the agents.
  
### Advantages of Using Local Models
- **Privacy**: Local models allow processing of data within your own infrastructure, ensuring data privacy.
- **Customization**: You can customize the model to better suit the specific needs of your tasks.
- **Performance**: Depending on your setup, local models can offer performance benefits, especially in terms of latency.

## License
This project is released under the MIT License.

