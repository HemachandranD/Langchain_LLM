from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain_core.prompts import PromptTemplate
from tools.tools import scrape_top_news


def lookup(source: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """Give the source {name_of_source}, I want you to get the URL of the first article only.
                    Your answer should contain only a URL."""
    # Instantiation using from_template (recommended)
    prompt = PromptTemplate.from_template(template)
    prompt.format(name_of_source=source)
    tools_for_agent = [
        Tool(
            name="Crawl Top most news headlines",
            func=scrape_top_news,
            description="Useful for when you need to find the Articles",
        )
    ]

    obj = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=obj)
    agentexecutor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agentexecutor.invoke(
        input={"input": source}
    )
    article_url = result["output"]
    return article_url
