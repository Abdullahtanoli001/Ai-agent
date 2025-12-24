from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_classic import hub
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize tools
search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
    """
    The function fetches the current weather data from a given city
    """
    api_key = os.getenv('WEATHER_API_KEY')
    url = f'https://api.weatherstack.com/current?access_key={api_key}&query={city}'
    response = requests.get(url)
    return response.json()

# Initialize LLM
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv('GROQ_API_KEY')
)

# Create ReAct agent
prompt = hub.pull("hwchase17/react")
agent = create_react_agent(
    llm=model,
    tools=[search_tool, get_weather_data],
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather_data],
    verbose=True
)

@app.route('/search', methods=['POST'])
def search_news():
    try:
        data = request.json
        query = data.get('query', '')
        
        if not query:
            return jsonify({
                'success': False,
                'error': 'Query is required'
            }), 400
        
        result = search_tool.invoke(query)
        
        return jsonify({
            'success': True,
            'query': query,
            'result': result
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/weather', methods=['POST'])
def get_weather():
    try:
        data = request.json
        city = data.get('city', '')
        
        if not city:
            return jsonify({
                'success': False,
                'error': 'City is required'
            }), 400
        
        result = get_weather_data.invoke({'city': city})
        
        return jsonify({
            'success': True,
            'city': city,
            'weather': result
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/agent', methods=['POST'])
def run_agent():
    try:
        data = request.json
        query = data.get('query', '')
        
        if not query:
            return jsonify({
                'success': False,
                'error': 'Query is required'
            }), 400
        
        response = agent_executor.invoke({"input": query})
        
        return jsonify({
            'success': True,
            'query': query,
            'output': response['output'],
            'full_response': response
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, port=5002)