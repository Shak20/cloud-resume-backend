import sys
from unittest.mock import MagicMock

# Mock boto3 before importing the app
sys.modules["boto3"] = MagicMock()

from src.app import lambda_handler


def test_lambda_handler():
    event = {}
    context = None
    response = lambda_handler(event, context)

    assert response["statusCode"] == 200