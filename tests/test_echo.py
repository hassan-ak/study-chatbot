"""Tests for the study chatbot echo functionality."""
import pytest
from unittest.mock import AsyncMock, Mock
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from study_chatbot import app


@pytest.mark.asyncio
async def test_echo_text_message():
    """Test that text messages are echoed back correctly."""
    # Mock chainlit Message
    mock_message = Mock()
    mock_message.content = "Hello, world!"
    
    # Mock chainlit.Message constructor and send method
    mock_response = AsyncMock()
    mock_response.send = AsyncMock()
    
    # Patch chainlit.Message
    import chainlit as cl
    original_message = cl.Message
    cl.Message = Mock(return_value=mock_response)
    
    try:
        # Call the handler
        await app.main(mock_message)
        
        # Verify response was created with echoed content
        cl.Message.assert_called_once_with(content="Hello, world!")
        mock_response.send.assert_called_once()
    finally:
        # Restore original
        cl.Message = original_message


@pytest.mark.asyncio
async def test_empty_message():
    """Test that empty messages get a helpful response."""
    # Mock chainlit Message with empty content
    mock_message = Mock()
    mock_message.content = ""
    mock_message.data = None
    
    # Mock chainlit.Message constructor and send method
    mock_response = AsyncMock()
    mock_response.send = AsyncMock()
    
    # Patch chainlit.Message
    import chainlit as cl
    original_message = cl.Message
    cl.Message = Mock(return_value=mock_response)
    
    try:
        # Call the handler
        await app.main(mock_message)
        
        # Verify helpful message was sent
        cl.Message.assert_called_once_with(content="I can only echo text messages. Please send plain text.")
        mock_response.send.assert_called_once()
    finally:
        # Restore original
        cl.Message = original_message


@pytest.mark.asyncio
async def test_none_message():
    """Test that None content gets a helpful response."""
    # Mock chainlit Message with None content
    mock_message = Mock()
    mock_message.content = None
    mock_message.data = None
    
    # Mock chainlit.Message constructor and send method
    mock_response = AsyncMock()
    mock_response.send = AsyncMock()
    
    # Patch chainlit.Message
    import chainlit as cl
    original_message = cl.Message
    cl.Message = Mock(return_value=mock_response)
    
    try:
        # Call the handler
        await app.main(mock_message)
        
        # Verify helpful message was sent
        cl.Message.assert_called_once_with(content="I can only echo text messages. Please send plain text.")
        mock_response.send.assert_called_once()
    finally:
        # Restore original
        cl.Message = original_message


@pytest.mark.asyncio
async def test_whitespace_only_message():
    """Test that whitespace-only messages get a helpful response."""
    # Mock chainlit Message with whitespace
    mock_message = Mock()
    mock_message.content = "   \n\t   "
    mock_message.data = None
    
    # Mock chainlit.Message constructor and send method
    mock_response = AsyncMock()
    mock_response.send = AsyncMock()
    
    # Patch chainlit.Message
    import chainlit as cl
    original_message = cl.Message
    cl.Message = Mock(return_value=mock_response)
    
    try:
        # Call the handler
        await app.main(mock_message)
        
        # Verify helpful message was sent
        cl.Message.assert_called_once_with(content="I can only echo text messages. Please send plain text.")
        mock_response.send.assert_called_once()
    finally:
        # Restore original
        cl.Message = original_message