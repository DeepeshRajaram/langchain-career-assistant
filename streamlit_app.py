import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from prompts import career_prompt

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7,
    max_tokens=500
)

chain = career_prompt | llm | StrOutputParser()

st.title("AI Career Assistant")

st.write(
    "Generate a personalized career roadmap using LangChain and OpenAI"
)

role = st.text_input("Enter your current role", placeholder="e.g., Software Engineer")

goal = st.text_input("Enter your career goal", placeholder="e.g., Become a Data Scientist")

if st.button("Generate Career Roadmap"):
    if role and goal:
        response = chain.invoke(
            {
                "role": role,
                "goal": goal
            }
        )
        st.markdown(response)
    else:
        st.warning("Please enter both your current role and career goal to generate a roadmap.")
