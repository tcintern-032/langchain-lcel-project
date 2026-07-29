from langchain_core.prompts import ChatPromptTemplate

teacher_prompt = ChatPromptTemplate.from_template(
    """
You are an experienced teacher.

Explain the following topic in simple language.

Topic: the topic is that i teach you about coding my way of teaching is good
{topic}
"""
)