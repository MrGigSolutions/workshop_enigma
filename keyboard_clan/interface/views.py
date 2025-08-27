import json
import logging
import requests
from django.shortcuts import render

_logger = logging.getLogger(__name__)

def main(request, context=None):
    context = {
        **(context or {}),
        "key": _http_get_simple('http://localhost:8000/machine/key'),
        "current_path": request.path,
    }
    return render(request, 'interface/index.html', context)


def set_key(request):
    if request.method == 'POST':
        key = request.POST.get('message', '')
        # The FastAPI endpoint expects a simple string parameter
        _http_post_simple('http://localhost:8000/machine/key', {"key": key})

    context = {"placeholder": "Enter new key (exactly 3 characters)"}
    return main(request, context)

def encrypt_message(request):
    response = None
    if request.method == 'POST':
        message = request.POST.get('message', '')
        response = _http_post_simple('http://localhost:8000/machine/encrypt', {"message": message})

    context = {
        "placeholder": "Enter the message you want to encrypt",
        "message": response
    }
    return main(request, context)

def decrypt_message(request):
    context = {
        "placeholder": "Enter the message you want to decrypt",
    }
    if request.method == 'POST':
        message = request.POST.get('message', '')
        context["message"] = _http_post_simple('http://localhost:8000/machine/decrypt', {"message": message})

    return main(request, context)

def plugs(request):
    context = {
        "placeholder": "Enter a 2-letter plug pair (e.g., AB), or submit '-' to clear plugs."
    }
    if request.method == 'POST':
        message = request.POST.get('message', '')
        if message == "-":
            _http_delete('http://localhost:8000/machine/plug/reset')
        else:
            _http_post_simple('http://localhost:8000/machine/plug/', {"message": message})
    context["message"] = _http_get_simple('http://localhost:8000/machine/plug/list')
    return main(request, context)


def _http_get_simple(url: str):
    """Simple HTTP client for GET requests"""
    response = requests.get(url)
    response.raise_for_status()
    data = response.json() if response.content else response.text
    _logger.info(f"Data received: {data}")
    return data


def _http_post_simple(url: str, message: dict | None = None):
    """Simple HTTP client that sends key as a query parameter to match FastAPI expectation"""
    response = requests.post(url, params=message)
    response.raise_for_status()
    return response.json() if response.content else response.text

def _http_post_json(url: str, message: dict):
    """Simple HTTP client that sends key as a query parameter to match FastAPI expectation"""
    response = requests.post(url, data=json.dumps(message))
    response.raise_for_status()
    return response.json() if response.content else response.text

def _http_delete(url: str):
    """Simple HTTP client that sends key as a query parameter to match FastAPI expectation"""
    response = requests.delete(url)
    response.raise_for_status()
    return response.json() if response.content else response.text