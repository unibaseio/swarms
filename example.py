import os

from swarm_models import OpenAIChat
from swarms import Agent
from swarms.prompts.finance_agent_sys_prompt import (
    FINANCIAL_AGENT_SYS_PROMPT,
)
from dotenv import load_dotenv

load_dotenv()

# Get the OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Model
model = OpenAIChat(
    openai_api_base="https://dashscope.aliyuncs.com/compatible-mode/v1",
    openai_api_key=api_key,
    model_name="qwen-max",
    temperature=0.1,
)

print("agent")
# Initialize the agent
agent = Agent(
    agent_name="Financial-Analysis-Agent",
    agent_description="Personal finance advisor agent",
    system_prompt=FINANCIAL_AGENT_SYS_PROMPT,
    max_loops=1,
    llm=model,
    dynamic_temperature_enabled=True,
    user_name="swarms_exmaple_user",
    retry_attempts=3,
    context_length=8192,
    return_step_meta=False,
    output_type="str",  # "json", "dict", "csv" OR "string" "yaml" and
    auto_generate_prompt=False,  # Auto generate prompt for the agent based on name, description, and system prompt, task
    max_tokens=4000,  # max output tokens
    autosave=True,
    saved_state_path="agent_00.json",
    interactive=False,
)
print("agent run: ")

agent.run(
    "Create a table of super high growth opportunities for AI. I have $40k to invest in ETFs, index funds, and more. Please create a table in markdown.",
    all_cores=True,
)
print("finish agent run: ")
