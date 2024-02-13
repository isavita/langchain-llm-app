from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain_community.tools import DuckDuckGoSearchRun

from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(pet_type, names_count=1):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0.7)
    prompt_tepmlate = PromptTemplate(
        input_variables=["pet_type", "names_count"],
        template="You are a helpful assistant that generates pet names for {pet_type}. The names should be unique, short, and easy to pronounce. You must generate {names_count} names."
    )
    names_chain = LLMChain(llm=llm, prompt=prompt_tepmlate)

    response = names_chain.invoke({"pet_type": pet_type, "names_count": names_count})
    return response

def langchain_agent():
    llm = ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0.5)
    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    agent = initialize_agent(
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        llm=llm,
        tools=tools,
        verbose=True
    )

    result = agent.run(
        "What is the average age of dog?"
    )

    return result

if __name__ == "__main__":
    response = langchain_agent()
    print(response)
