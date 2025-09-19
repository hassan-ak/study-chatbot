from typing import Any
import chainlit as cl

from agents import (
    Agent,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)

from config import Config


def create_study_agent() -> Agent[Any]:
    """
    Create and return a configured study Agent.
    """
    config = Config()

    external_client = AsyncOpenAI(
        api_key=config.gemini_api_key,
        base_url=config.gemini_api_url,
    )

    set_tracing_disabled(True)

    model = OpenAIChatCompletionsModel(
        model=config.gemini_api_model, openai_client=external_client
    )

    study_agent = Agent(
        name="Study Agent",
        instructions=("You are a helpful study assistant"),
        model=model,
    )

    return study_agent
