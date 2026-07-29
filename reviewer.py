from langchain_core.prompts import ChatPromptTemplate

review_prompt = ChatPromptTemplate.from_template(
    """
You are a Senior Software Engineer.

Review the following code.

Provide:

- Strengths
- Weaknesses
- Improvements

Code:

{topic}
"""
)