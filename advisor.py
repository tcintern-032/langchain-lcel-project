from langchain_core.prompts import ChatPromptTemplate

advisor_prompt = ChatPromptTemplate.from_template(
    """
You are an AI Career Advisor.

Guide a student who wants to become an AI Engineer.

Question:

{topic}
"""
)