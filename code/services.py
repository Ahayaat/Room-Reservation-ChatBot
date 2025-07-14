from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config
from tools import make_reservation, check_room_availability, cancel_reservation


SECRET_KEY = config('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(
    api_key=SECRET_KEY, model='gemini-1.5-flash')

tools = [make_reservation, check_room_availability, cancel_reservation]

llm_call_tools = llm.bind_tools(tools)