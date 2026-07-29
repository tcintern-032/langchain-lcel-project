# LangChain LCEL Application
A modular AI application built with **LangChain Expression Language (LCEL)** that demonstrates how to create reusable AI pipelines using Prompt Templates, Chat Models, and Output Parsers. This project includes multiple AI roles such as a Teacher, Code Reviewer, and Career Advisor to showcase how different prompt templates can produce different responses using the same underlying language model.
# Features
* Built using **LangChain Expression Language (LCEL)**
* Uses **Prompt Templates** for structured prompting
* Integrates with **OpenAI Chat Model**
* Demonstrates the **Prompt → Model → Output** workflow
* Uses **Runnable Chains** for modular AI pipelines
* Includes multiple prompt templates:

  * Teacher
  * Code Reviewer
  * Career Advisor
* Organized project structure
* Easy to extend with additional prompts and chains
# Project Structure
```text
langchain-lcel-app/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── prompts/
│   ├── teacher.py
│   ├── reviewer.py
│   └── advisor.py
│
└── chains/
    └── lcel_chain.py
```
# Technologies Used
* Python 3.11+
* LangChain
* LangChain OpenAI
* OpenAI API
* LangChain Core
# Running the Application
Start the application with:

```bash
python app.py
```
# Menu
```
===== LangChain LCEL Demo =====

1. Teacher
2. Code Reviewer
3. Career Advisor
4. Exit
```

Select an option and provide your input.

---
# Example 1 – Teacher
Input
```
What is Artificial Intelligence?
```
Output
```
Artificial Intelligence (AI) is a field of computer science that enables
computers to perform tasks that normally require human intelligence such as
learning, reasoning, and decision-making.
```

---
# Example 2 – Code Reviewer

Input

```python
for i in range(5):
    print(i)
```
Output

```
Strengths
- Simple
- Easy to read

Weaknesses
- No comments
- Not reusable

Suggestions
- Wrap the code inside a function
- Add documentation
```

---

# Example 3 – Career Advisor

Input

```
How do I become an AI Engineer?
```

Output

```
1. Learn Python
2. Study Data Structures and Algorithms
3. Learn Machine Learning
4. Explore Deep Learning
5. Build AI Projects
6. Learn LangChain
7. Learn FastAPI
8. Deploy AI Applications
```
# LCEL Workflow

```
User Input
      │
      ▼
Prompt Template
      │
      ▼
Chat Model
      │
      ▼
Output Parser
      │
      ▼
Generated Response
```

---
# What is LCEL?

LangChain Expression Language (LCEL) is a declarative way to connect LangChain components together. Instead of manually calling each component, LCEL allows developers to build clean and reusable pipelines using the `|` operator.

Example:

```python
chain = prompt | model | parser
```

This chain executes:

1. Prompt Template
2. Chat Model
3. Output Parser

---

# Runnables

LCEL introduces the concept of **Runnables**, which are reusable components that can be combined into AI pipelines.

Examples include:
* Prompt Templates
* Chat Models
* Output Parsers
* Chains

Runnables make applications easier to maintain and extend.

---

# Prompt Templates Included

## Teacher

Explains any topic in simple and beginner-friendly language.

Example:

```
Explain Python Functions.
```

---

## Code Reviewer

Reviews source code and provides:

* Strengths
* Weaknesses
* Suggestions

---

## Career Advisor

Provides career guidance for students interested in Artificial Intelligence and software development.

---

# Learning Outcomes

After completing this project, you will understand:

* LangChain Expression Language (LCEL)
* Prompt Templates
* Runnable Components
* Output Parsers
* Chat Models
* Modular AI Application Design
* Prompt Chaining
* Reusable AI Pipelines

---

# Future Improvements

* Add conversation memory
* Support multiple LLM providers
* Build a FastAPI version
* Create a web interface
* Add document question answering
* Integrate Retrieval-Augmented Generation (RAG)
* Add streaming responses
* Store chat history

---

# Requirements

```
langchain
langchain-openai
python-dotenv
```
# Author
**Devolped By Muhammad Zeeshan**
