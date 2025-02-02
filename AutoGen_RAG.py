import autogen 
from autogen import AssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
import os
import dotenv

dotenv.load_dotenv()


# LLMエージェントを設定
assistant = AssistantAgent(
    name="assistant",
    system_message="You are a helpful assistant.",
    llm_config={
        "config_list": [
            {
                "model": "gpt-4o",
                "api_key": os.environ.get("OPENAI_API_KEY"),
            }
        ]
    },
)


# RAGエージェントを設定
ragproxyagent = RetrieveUserProxyAgent(
    name="ragproxy",
    retrieve_config={
        "task": "qa",
        "docs_path": "./docs",
    },
)


assistant.reset()
ragproxyagent.initiate_chat(assistant,problem="TechVision Solutions的核心业务是什么？")
