from langchain_openai import ChatOpenAI

OPENAI_API_KEY="api_key"
model = ChatOpenAI(
    model="gpt-5.4-mini",
    api_key=OPENAI_API_KEY,
    temperature=0.7
)