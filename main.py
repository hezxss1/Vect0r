import requests

class OllamaAI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.ollama.com/v1/"

    def analyze_code(self, code):
        endpoint = "analyze"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        response = requests.post(self.base_url + endpoint, json={"code": code}, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}

if __name__ == '__main__':
    api_key = "YOUR_OLLAMA_API_KEY"
    ollama_agent = OllamaAI(api_key)

    # Example code to analyze
    example_code = "def hello_world():\n    print('Hello, world!')"
    analysis_result = ollama_agent.analyze_code(example_code)
    print(analysis_result)