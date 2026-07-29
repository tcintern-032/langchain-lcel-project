from langchain_core.output_parsers import StrOutputParser

from config import model

parser = StrOutputParser()


def create_chain(prompt):
    return prompt | model | parser