# Package Sorting System

A robust Python 3.10 application that sorts packages into appropriate stacks based on dimensions and mass. Features comprehensive testing, error handling, and modern Python practices.

## Requirements

- Python 3.10 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/bryanstgarcia/Thoughtful-interview.git
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
   # Interactive demo mode (default)
   python main.py
   
   # Comprehensive test suite
   python main.py --test
   ```

3. Deactivate the virtual environment when done:
   ```bash
   deactivate
   ```

### Running Modes

#### Interactive Demo Mode
The default mode runs a demonstration with sample packages:
```bash
python main.py
```
This shows how the sorting system works with various package types including:
- Standard packages
- Bulky packages (by volume and dimension)
- Heavy packages
- Rejected packages (both bulky and heavy)
- Edge case packages

#### Test Suite Mode
Run the comprehensive test suite to verify all functionality:
```bash
python main.py --test
```
This includes:
- **Functional Tests**: 15+ test cases covering all sorting scenarios
- **Edge Case Tests**: Boundary conditions and threshold testing
- **Error Handling Tests**: Invalid input validation
- **Performance Verification**: Correct sorting logic validation

## Project Structure

```
thoughtful/
├── main.py              # Main application file
├── .python-version     # Python version specification (3.10.0)
├── venv/               # Virtual environment directory
└── README.md           # This file
```

## Features

### Core Functionality
- **Package Sorting Algorithm**: Categorizes packages into STANDARD, SPECIAL, or REJECTED stacks
- **Robust Input Validation**: Handles edge cases and invalid inputs gracefully
- **Comprehensive Error Handling**: Clear error messages for debugging


