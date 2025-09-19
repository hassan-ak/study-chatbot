import chainlit as cl


@cl.on_message
async def main(message: cl.Message) -> None:
    """Echo bot: responds with the same message content that was sent.

    Features:
    - Validates and safely extracts text content from messages
    - Returns helpful notices for non-text or empty messages
    - Handles edge cases like whitespace-only content
    """
    # Prefer plain text content; fall back to `content` attr if available
    text = None

    if isinstance(message.content, str) and message.content.strip():
        text = message.content

    # If no text available, try to extract from data (safe defensive coding)
    if text is None:
        payload = getattr(message, "data", None)
        if isinstance(payload, dict):
            # look for common fields
            for key in ("text", "message", "content"):
                val = payload.get(key)
                if isinstance(val, str) and val.strip():
                    text = val
                    break

    if not text:
        await cl.Message(content="I can only echo text messages. Please send plain text.").send()
        return

    # Echo the user's text
    await cl.Message(content=text).send()