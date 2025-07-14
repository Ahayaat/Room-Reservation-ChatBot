from classes import State
from services import llm_call_tools

def call_func(state: State):
  return{"messages": llm_call_tools.invoke(state["messages"])}