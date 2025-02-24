import pytest
from utils.api_helper import APIHelper

class TestAPI:
    def test_get_user_details(self):
        url = "https://api.example.com/users/1"
        response = APIHelper.get(url)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        json_data = response.json()
        # Validate key elements in the JSON response
        assert "id" in json_data, "User ID not found in response"
        assert json_data["id"] == 1, "Unexpected user ID"
