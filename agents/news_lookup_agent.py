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
    template = """Given the source {name_of_the_source} get the first article content"""
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_the_source"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Top news headlines from the given news source",
            func=scrape_top_news,
            description="Useful for when you need to find the Article Page URL",
        )
    ]

    obj = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=obj)
    agentexecutor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agentexecutor.invoke(
        input={"input": prompt_template.format_prompt(name_of_the_source=source)}
    )
    article_url = result["output"]
    return article_url
