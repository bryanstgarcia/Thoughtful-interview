# Python App

A simple Python application built with Python 3.10.

## Requirements

- Python 3.10 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd thoughtful
   ```

2. Install Python 3.10 (if not already installed):
   ```bash
   # Using pyenv (recommended)
   pyenv install 3.10.0
   pyenv local 3.10.0
   
   # Or using your system package manager
   # macOS: brew install python@3.10
   # Ubuntu: sudo apt install python3.10
   ```

3. Verify Python 3.10 installation:
   ```bash
   python --version  # Should show Python 3.10.0
   ```

4. Create and activate virtual environment:
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Verify virtual environment is active
   which python  # Should point to venv/bin/python
   ```

5. No external dependencies required - this is a pure Python 3.10 application

## Usage

1. Activate the virtual environment (if not already active):
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Deactivate the virtual environment when done:
   ```bash
   deactivate
   ```

## Project Structure

```
thoughtful/
├── main.py              # Main application file
├── requirements.txt     # Dependencies (none required)
├── .python-version     # Python version specification (3.10.0)
├── venv/               # Virtual environment directory
└── README.md           # This file
```
