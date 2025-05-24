# UF LMS Chatbot

Simple web-based chatbot that answers basic questions about your classes using real tool/function calling.

### 🔧 Features
- Get your weighted average grade for a course
- See upcoming topics and class content with dates
- Real OpenAI-style function calling via LangChain
- CSV-based mock data for easy updates

### 📁 Files
- `app.py`: Flask backend
- `langchain_agent.py`: LLM + tool logic
- `tools.py`: Functions for grades and topics
- `grades.csv`: Grade + weight data
- `coursecontent.csv`: Topic + date data
- `templates/index.html`: Web interface

### ▶️ How to Run
1. Install packages:
```bash
pip install flask openai langchain langchain-community pandas python-dotenv
