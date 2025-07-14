from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from random import randint
from nodes import call_func
from services import tools
from classes import State
from langgraph.types import Command


memory = MemorySaver()

graph_builder = StateGraph(State)


graph_builder.add_node("call_func", call_func)

tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools", tool_node)

graph_builder.add_edge(START, "call_func")
graph_builder.add_conditional_edges("call_func",tools_condition)
graph_builder.add_edge("tools", END)

graph = graph_builder.compile(checkpointer=memory)


user_input = "make reservation"
config = {"configurable": {"thread_id": "1"}}

events = graph.stream(
    {"messages": [("user", user_input)]}, config, stream_mode="updates"
)
for event in events:
    event

snapshot = graph.get_state(config)

existing_message = snapshot.values["messages"][-1]

if existing_message.tool_calls:
    user_input = input("permission granted: yes or no. ")
    if user_input == "yes":
       for event in graph.stream(Command(resume={"correct": "yes"}), config, stream_mode="updates"
        ):
        print(event["tools"]["messages"])
    elif user_input == "no":
        print("Permission denied")