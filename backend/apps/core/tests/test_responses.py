"""Response tests."""
from apps.core.responses.api_response import ApiResponse


class TestApiResponse:
    def test_success_response_format(self):
        response = ApiResponse(data={"key": "value"})
        assert response.status_code == 200
        assert response.data["status"] == "success"
