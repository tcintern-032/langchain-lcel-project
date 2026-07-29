from chains.lcel_chain import create_chain

from prompts.teacher import teacher_prompt
from prompts.reviewer import review_prompt
from prompts.advisor import advisor_prompt
def menu():
    print("\n===== LangChain LCEL Demo =====")
    print("1. Teacher")
    print("2. Code Reviewer")
    print("3. Career Advisor")
    print("4. Exit")


while True:

    menu()

    choice = input("\nChoose Option: ")

    if choice == "1":

        topic = input("\nEnter Topic:You are an experienced teacher.")

        chain = create_chain(teacher_prompt)

        response = chain.invoke(
            {
                "topic": topic
            }
        )

        print("\nResponse:\n")
        print(response)

    elif choice == "2":

        code = input("\nPaste Code:- Strengths- Weaknesses- Improvements\n")

        chain = create_chain(review_prompt)

        response = chain.invoke(
            {
                "topic": code
            }
        )

        print("\nReview:\n")
        print(response)

    elif choice == "3":

        question = input("\nAsk Career Question:You are an AI Career Advisor.Guide a student who wants to become an AI Engineer.")

        chain = create_chain(advisor_prompt)

        response = chain.invoke(
            {
                "topic": question
            }
        )

        print("\nAdvice:\n")
        print(response)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")
        