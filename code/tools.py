from langchain_core.messages import ToolMessage
from langchain_core.tools import InjectedToolCallId
from typing import Annotated
from langgraph.types import Command, interrupt


def make_reservation(room_type: str, nights: int, tool_call_id: Annotated[str, InjectedToolCallId]):
    """
    Constructs a reservation summary.

    Args:
        room_type: str - The type of room being reserved (e.g., single, double, suite).
        nights: int - The number of nights for the reservation.

    Returns:
        str - A summary of the reservation.
    """
    human_response = interrupt({"correct": ""})
    answer = human_response.get["correct"]
    print("...................", answer)

    response = f"Reservation confirmed: {room_type} room for {nights} night(s)."

    state_updated = {"messages": [ToolMessage(response, tool_call_id=tool_call_id)]}

    return Command(update=state_updated)

def check_room_availability(total_rooms: int, booked_rooms: int, tool_call_id: Annotated[str, InjectedToolCallId]):
    """
    Checks the availability of rooms.

    Args:
        total_rooms: int - The total number of rooms in the hotel.
        booked_rooms: int - The number of rooms that are already booked.

    Returns:
        str - A message indicating the number of available rooms.
    """

    human_response = interrupt({})

    if booked_rooms > total_rooms:
        return "Error: Booked rooms cannot exceed total rooms."
    available_rooms = total_rooms - booked_rooms
    return f"{available_rooms} room(s) are available out of {total_rooms} total room(s)."

def cancel_reservation(room_type: str, nights: int, tool_call_id: Annotated[str, InjectedToolCallId]):
    """
    Cancels a reservation.

    Args:
        room_type: str - The type of room being reserved (e.g., single, double, suite).
        nights: int - The number of nights for the reservation.

    Returns:
        str - A message indicating the cancellation of the reservation.
    """
    human_response = interrupt({})

    return f"Reservation canceled: {room_type} room for {nights} night(s)."