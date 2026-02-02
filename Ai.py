from langchain.chat_models import init_chat_model

llm = init_chat_model(
    model_provider='openai',
    model="Model",
    api_key='None',
    streaming=True,
)

def Ai_Agent(Agent_Data, user_input):

    return llm.invoke(f'''
    You are Ai Agent Personal Assistant
    User Data:
    {Agent_Data}

    User input:
    {user_input}

    return MD''')


def Ai_Test(prompt):

    return llm.invoke(prompt)