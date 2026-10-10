import os

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


from prompts import career_prompt

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7
)

chain = career_prompt | llm | StrOutputParser()

role = input("Enter your current role: ")
goal = input("Enter your career goal: ")

print ("\nGenerating career roadmap...\n")

response = chain.invoke(
    {
        "role": role,
        "goal": goal
    }
)

print(response)