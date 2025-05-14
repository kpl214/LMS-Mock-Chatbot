# langchain_agent.py
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType

from tools import get_current_grade, get_course_topics

load_dotenv()

tools = [get_current_grade, get_course_topics]

llm = ChatOpenAI(
    temperature=0,
    model_name=os.getenv("MODEL"),
    openai_api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

# Initialize agent with tools
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True  # debugging
)

def run_agent(query: str) -> str:
    return agent.run(query)
