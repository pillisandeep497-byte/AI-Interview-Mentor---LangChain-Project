from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from dotenv import load_dotenv
import os 
from pydantic import BaseModel,Field
from langchain_core.output_parsers import PydanticOutputParser
load_dotenv()
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)



class InterviewModel(BaseModel):
    interview: str= Field(description="\ngive mpost important interview quistions")
    instructions: str= Field(description="\na detailed intruction in interview hall and how to move on with fear")
    expert: str= Field(description="\ngive some advices from must succesfuoo intervieres ")

parcer =PydanticOutputParser(pydantic_object=InterviewModel)


promt = ChatPromptTemplate.from_messages([
    ("system",
     """
    1.act as a senior interviewer
    2.ask some important questions about user role
    3.implement art rule for output  
    art rule = a means act as , r means request , t means terms
    4. give output with structured format {format_instructions} """),

    MessagesPlaceholder(variable_name="history"),
    ("human",'{input}')
])


chain = (
    promt.partial(format_instructions=parcer.get_format_instructions)|
    llm|parcer
)
store = {}
def get_session(session_id:str):
    if session_id not in store:
        store[session_id]=InMemoryChatMessageHistory()

    return store[session_id]


mentor = RunnableWithMessageHistory(
    chain,
    get_session,
    input_messages_key="input",
    history_messages_key="history"

)
print("=====================================AI interview specilist=======================================")
print("type 'exit' to quit")

while True:
    user_input = input("you: ")

    if user_input.lower()== "exit":
        break 

    responce = mentor.invoke(
        {"input":user_input},
        config={"configurable": {"session_id":"sandeep"}}


    )

    print("\nImportant questions: ",{responce.interview})
    print("\nInstruction: ",{responce.instructions})
    print("\nAdvice",{responce.expert})
    print()