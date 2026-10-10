import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import (HumanMessage, AIMessage)

from prompts import career_prompt



def build_markdown():
    markdown = "Career Plan"

    for message in st.session_state.history:
        if isinstance(message, HumanMessage):
            markdown += (
                f"## User \n\n"
                f"{message.content}\n\n"
            )
        elif isinstance(message, AIMessage):
            markdown += (
                f"## Assistant\n\n"
                f"{message.content}\n\n"
            )
    return markdown

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7,
    max_tokens=500
)

chain = career_prompt | llm | StrOutputParser()

st.title("AI Career Assistant")

if "history" not in st.session_state:
    st.session_state.history = []

for message in st.session_state.history:
    if isinstance(message, HumanMessage):
        st.chat_message("user").write(
            message.content
        )
    elif isinstance(message, AIMessage):
        st.chat_message("assistant").write(
            message.content
        )


user_input = st.chat_input("Ask a career question...")

if user_input:
    st.chat_message("user").write(
        user_input
    )

    response = chain.invoke(
        {
            "input": user_input,
            "history": st.session_state.history
        }
    )
    st.chat_message("assistant").write(
        response
    )

    st.session_state.history.append(HumanMessage(content=user_input))

    st.session_state.history.append(AIMessage(content=response))

# if st.button("Clear Chat"):
#     st.session_state.history = []
#     st.rerun()

if st.session_state.history:
    markdown_content = build_markdown()
    st.download_button(
        label="Download Career Plan",
        data=markdown_content,
        file_name="career_plan.md",
        mime="text/markdown"
    )