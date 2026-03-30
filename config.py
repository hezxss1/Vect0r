# Configuration settings for the AI agent

# Model parameters
define_model_params():
    model_name = 'default_model'
    learning_rate = 0.001
    max_tokens = 150
    return model_name, learning_rate, max_tokens

# API endpoints
API_ENDPOINTS = {
    'base_url': 'https://api.example.com',
    'get_data': '/data',
    'post_data': '/data',
}

# Behavioral settings
BEHAVIORAL_SETTINGS = {
    'response_timeout': 5,  # in seconds
    'max_retries': 3,
    'retry_delay': 2,  # in seconds
}