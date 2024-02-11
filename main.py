from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate
)

load_dotenv()

def generate_pet_name():
    system_template = "You are a helpful assistant that generates pet names for {pet_type}. The names should be unique, short, and easy to pronounce."
    system_prompt = SystemMessagePromptTemplate.from_template(system_template)
    user_template = "{text}"
    user_prompt = HumanMessagePromptTemplate.from_template(user_template)
    chat_prompt = ChatPromptTemplate.from_messages([system_prompt, user_prompt])

    chat = ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0.7)

    return chat.invoke(
        chat_prompt.format_prompt(
            pet_type="dogs", text="I need five pet names in Bulgarian. I want them to be in cyrillic."
        ).to_messages()
    )

if __name__ == "__main__":
    print(generate_pet_name().content)
