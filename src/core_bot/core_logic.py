"""Core logic."""

from pub_sub import Message

def get_echo_response(input_message: Message) -> Message:
    """Return the input message as the echo response.

    Args:
        input_message (Message): The message to be echoed.

    Returns:
        Message: The echoed message.
    """
    return input_message
