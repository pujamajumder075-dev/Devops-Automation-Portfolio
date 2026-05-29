# 🐍 Python Automation Scripts

A collection of Python scripts for DevOps automation, API integration, system monitoring, and learning exercises.

## 📁 Folder Structure

### 1. **api-integration/** - API Integration Examples
Scripts demonstrating how to interact with external APIs and process responses.

- **api.py** - Basic API GET request to JSONPlaceholder API
- **jokes_api.py** - Fetch jokes from multiple APIs with user choice
- **stock_market_api.py** - Fetch real-time stock market data using Alpha Vantage API

**Use Cases:** Data retrieval, real-time monitoring, external service integration

### 2. **data-structures/** - Python Data Structure Examples
Demonstration of Python's built-in data structures and common operations.

- **dictionary_test.py** - Dictionary creation, access, update, and iteration
- **list_test.py** - List operations including append, insert, remove, pop
- **set_test.py** - Set operations and duplicate removal

**Use Cases:** Data manipulation, data processing, learning Python fundamentals

### 3. **system-monitoring/** - System Monitoring Scripts
Scripts for monitoring system resources and generating alerts.

- **cpu_monitoring_task.py** - Monitor CPU utilization and alert on threshold breach

**Use Cases:** Infrastructure monitoring, alerting, system health checks

### 4. **learning-exercises/** - Learning and Practice Scripts
Basic Python scripts covering fundamental concepts and exercises.

- **my-first-file.py** - Basic arithmetic operations and type casting
- **check_env.py** - Environment access checking with conditionals
- **function_test.py** - Function definition and parameter validation
- **loop_test.py** - For loops and conditional statements
- **tables.py** - Multiplication table generator with user interaction

**Use Cases:** Learning, practice, understanding Python fundamentals

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.7+
python --version

# Install required dependencies
pip install -r requirements.txt
```

### Running Scripts

#### API Integration
```bash
# Simple API call
python api-integration/api.py

# Fetch jokes from APIs
python api-integration/jokes_api.py

# Get stock market data (requires API key)
python api-integration/stock_market_api.py
```

#### Data Structures
```bash
# Dictionary operations
python data-structures/dictionary_test.py

# List operations
python data-structures/list_test.py

# Set operations
python data-structures/set_test.py
```

#### System Monitoring
```bash
# Monitor CPU usage
python system-monitoring/cpu_monitoring_task.py
```

#### Learning Exercises
```bash
# Run any learning script
python learning-exercises/my-first-file.py
python learning-exercises/check_env.py
python learning-exercises/function_test.py
python learning-exercises/loop_test.py
python learning-exercises/tables.py
```

## 📦 Dependencies

**Core Requirements:**
- Python 3.7+
- requests (for API calls)
- psutil (for system monitoring)

**Install all dependencies:**
```bash
pip install requests psutil
```

## 🔧 API Keys Required

### Stock Market API (Alpha Vantage)
1. Get free API key from: https://www.alphavantage.co/
2. Replace `API_KEY` in `stock_market_api.py` with your actual key

### Dad Jokes API
- Get free API key from: https://api-ninjas.com/
- Replace `DAD_JOKES_API_KEY` in `jokes_api.py` with your actual key

## 📚 Learning Outcomes

✅ API integration and HTTP requests  
✅ JSON data parsing and manipulation  
✅ Python data structures (lists, dicts, sets)  
✅ Functions and parameter validation  
✅ Control flow (loops, conditionals)  
✅ System monitoring and resource checking  
✅ Error handling and exception management  
✅ Type casting and data type operations  

## 🎯 Use Cases

- **DevOps Automation:** System monitoring, resource tracking
- **Data Integration:** API consumption, external service integration
- **Infrastructure Monitoring:** CPU monitoring, resource alerts
- **Learning & Practice:** Python fundamentals, scripting patterns

## 📝 Notes

- All scripts include error handling for robustness
- Scripts are commented for easy understanding
- Each script can be run independently
- Suitable for beginners learning Python automation

## 🤝 Contributing

Feel free to:
- Add more API integration examples
- Enhance monitoring capabilities
- Add more learning exercises
- Improve error handling

---

**Built with ❤️ for DevOps learning and automation**
