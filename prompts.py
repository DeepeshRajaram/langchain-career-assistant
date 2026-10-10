from langchain_core.prompts import (ChatPromptTemplate, MessagesPlaceholder)


career_prompt = ChatPromptTemplate.from_messages(
    [
       ( "system",
        """
        You are an AI Career Mentor.

        Help users with:
        - Career Roadmap
        - Skills Assessment
        - Certification Recommendations
        - Portfolio projects
        - Interview Preparation
        """
       ),
       MessagesPlaceholder(
           variable_name="history"
       ),
        (
            "human",
            "{input}"
        )
    ]
)






# from langchain_core.prompts import PromptTemplate

# career_prompt = PromptTemplate(
#     input_variables = ["role", "goal"],
#     template = """
# You are an experienced career mentor.

# Current Role: {role}

# Career Goal: {goal}

# Provide:
# 1. Learning Roadmap
# 2. Skills to learn
# 3. Portfolio Projects
# 4. Interview Preparation Tips

# Be Practical and concise in your suggestions.
# """
# )
