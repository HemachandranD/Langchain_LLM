from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain import hub
from tools.tools import scrape_top_news


def lookup(source: str) -> str:
    prompt_template = """Give the source {name_of_source}, get the News Title and URL of the content.
                            Your answer should contain News Title and the URL"""

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    tool = [
        Tool(
            name="Crawl Top most news headlines from sources",
            func=scrape_top_news,
            description="Useful for when you need to find the Articles",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tool, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tool, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format(name_of_source=source)}
    )
    news_url = result["output"]
    return news_url
