import pytest
import httpx
from unittest.mock import Mock, patch
from mcp_py_devto.server import (
    get_latest_articles,
    get_top_articles,
    get_articles_by_tag,
    get_article_by_id,
    search_articles,
    get_user_info,
    format_articles,
    format_article_details,
    format_user_profile
)

@pytest.fixture
def mock_article():
    return {
        "title": "Test Article",
        "user": {"name": "Test Author"},
        "readable_publish_date": "Jan 1",
        "id": "123",
        "tags": "python,test",
        "description": "Test description",
        "body_markdown": "Test content"
    }

@pytest.fixture
def mock_user():
    return {
        "username": "testuser",
        "name": "Test User",
        "summary": "Test bio",
        "twitter_username": "testtwitter",
        "github_username": "testgithub",
        "website_url": "https://test.com",
        "location": "Test Location",
        "joined_at": "2023-01-01"
    }

async def test_get_latest_articles(mock_httpx_client, mock_article):
    mock_httpx_client.get.return_value.json.return_value = [mock_article]
    result = await get_latest_articles()
    assert "Test Article" in result
    assert "Test Author" in result

async def test_get_top_articles(mock_httpx_client, mock_article):
    mock_httpx_client.get.return_value.json.return_value = [mock_article]
    result = await get_top_articles()
    assert "Test Article" in result

async def test_get_articles_by_tag(mock_httpx_client, mock_article):
    mock_httpx_client.get.return_value.json.return_value = [mock_article]
    result = await get_articles_by_tag("python")
    assert "Test Article" in result

async def test_get_article_by_id(mock_httpx_client, mock_article):
    mock_httpx_client.get.return_value.json.return_value = mock_article
    result = await get_article_by_id("123")
    assert "Test Article" in result
    assert "Test content" in result

async def test_search_articles(mock_httpx_client, mock_article):
    mock_httpx_client.get.return_value.json.return_value = [mock_article]
    result = await search_articles("test")
    assert "Test Article" in result

async def test_get_user_info(mock_httpx_client, mock_user):
    mock_httpx_client.get.return_value.json.return_value = mock_user
    result = await get_user_info("testuser")
    assert "Test User" in result
    assert "Test Location" in result

def test_format_articles(mock_article):
    result = format_articles([mock_article])
    assert "Test Article" in result
    assert "Test Author" in result
    assert "Test description" in result

def test_format_article_details(mock_article):
    result = format_article_details(mock_article)
    assert "Test Article" in result
    assert "Test content" in result

def test_format_user_profile(mock_user):
    result = format_user_profile(mock_user)
    assert "Test User" in result
    assert "Test Location" in result
    assert "testtwitter" in result
