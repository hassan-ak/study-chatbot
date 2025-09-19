import chainlit as cl
from typing import cast

# Ensure configuration is validated at import time so missing environment
# variables cause the process to exit with a clear message before Chainlit starts.
from config import Config

_config = Config()  # will exit(1) with a printed message if required vars are missing

from study_chatbot.agent import create_study_agent
from agents import Runner, Agent


@cl.on_chat_start
async def on_start():
    """Create and store the study agent in the user session when a chat starts."""
    agent = create_study_agent()
    cl.user_session.set("agent", agent)
    cl.user_session.set("chat_history", [])
    await cl.Message(content="Welcome! How can I help you today?").send()


@cl.on_message
async def main(message: cl.Message) -> None:
    """Process incoming messages with the triage agent instead of echoing."""
    # Extract text from message safely
    text = None
    if isinstance(message.content, str) and message.content.strip():
        text = message.content

    if text is None:
        payload = getattr(message, "data", None)
        if isinstance(payload, dict):
            for key in ("text", "message", "content"):
                val = payload.get(key)
                if isinstance(val, str) and val.strip():
                    text = val
                    break

    if not text:
        await cl.Message(content="Please send a short text question or request.").send()
        return

    # send a temporary thinking message
    thinking = cl.Message(content="Thinking...")
    await thinking.send()

    agent = cast(Agent, cl.user_session.get("agent"))
    history = cl.user_session.get("chat_history") or []
    history.append({"role": "user", "content": text})

    try:
        result = await Runner.run(agent, history)
        response = result.final_output

        thinking.content = str(response)
        await thinking.send()

        history.append({"role": "agent", "content": str(response)})
        cl.user_session.set("chat_history", history)

    except Exception as e:
        thinking.content = f"Error: {e}"
        await thinking.update()