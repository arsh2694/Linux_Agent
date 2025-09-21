import os

os.environ["GOOGLE_API_KEY"]="---Your Gemini-2.5-flash API key"

#AI LLM Model Access
from langchain_google_genai import ChatGoogleGenerativeAI
google_llm = ChatGoogleGenerativeAI(
        model = "gemini-2.5-flash",
        temperature = 0
        )

#Tools to run Linux Commands
from langchain_community.tools import ShellTool
shell_tool = ShellTool()

from langchain.agents import initialize_agent

 
myagent = initialize_agent(
            llm = google_llm,
            tools=[shell_tool],
            verbose = True
        )


while True:
    myprompt = input("Enter your Requirement:")
    input_message = {
            "role" : "user",
            "content" : "you are a linux administrator, and always give final output only and append in output.log file in current directory , for given prompt --" + myprompt
            }
    myagent.run({"input": input_message})
