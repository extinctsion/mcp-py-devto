import pytest
from unittest.mock import Mock, AsyncMock
import httpx

@pytest.fixture
def mock_response():
    response = Mock()
    response.status_code = 200
    response.raise_for_status = Mock()
    return response

@pytest.fixture
def mock_httpx_client(monkeypatch, mock_response):
    client = AsyncMock()
    client.get.return_value = mock_response
    client.post.return_value = mock_response
    client.put.return_value = mock_response
    
    async def mock_context_manager(*args, **kwargs):
        return client
        
    monkeypatch.setattr(httpx, "AsyncClient", Mock(return_value=AsyncMock(__aenter__=mock_context_manager)))
    return client
