from langchain.chains import LLMChain, ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)

## TODO: Make sure to update the example_user_config.py file and save it as user_config
import user_config

#An Alternative Way to handle this would be to use
# os.envrion["OPENAI_API_KEY"] = "sk-..."  # Replace with your key
api_key = user_config.openai_key

llm = ChatOpenAI(openai_api_key=api_key, temperature=1.0, model='gpt-3.5-turbo-0613')

def basicConversation(message_history):

    gpt_response = llm(message_history)
    return gpt_response.content