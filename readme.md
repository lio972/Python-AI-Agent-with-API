Voici le fichier README.md au format Markdown :


# AI Agent - Calculator with CLI and UI

The AI Agent is a Python-based calculator with both a **command-line interface (CLI)** and a **web-based user interface (UI)**. It supports basic and advanced mathematical operations, a **cancel operation** feature, and a **health check** functionality. It runs entirely within WebContainer's constraints and requires no external dependencies.

---

## Features

- **Basic Operations**: Addition, subtraction, multiplication, and division
- **Advanced Operations**: Square root and power calculations
- **Cancel Operation**: Stop the current operation
- **Health Check**: Check the system status and supported operations
- **Interactive CLI**: Simple command-line prompts for easy use
- **Web UI**: User-friendly interface for calculations
- **Error Handling**: Graceful handling of invalid inputs and operations

---

## Available Operations

| Operation  | Description                     | Example Input       |
|------------|---------------------------------|---------------------|
| `add`      | Add two numbers                 | 5 + 3 = 8           |
| `subtract` | Subtract two numbers            | 5 - 3 = 2           |
| `multiply` | Multiply two numbers            | 5 * 3 = 15          |
| `divide`   | Divide two numbers              | 6 / 3 = 2           |
| `sqrt`     | Square root of a number         | √9 = 3              |
| `power`    | Raise a number to a power       | 2^3 = 8             |

---

## Getting Started

### 1. Run the Server
Start the server to enable both CLI and UI functionality:
```bash
python3 server.py
2. Access the Web UI
Open your browser and navigate to:


http://localhost:5000
3. Use the CLI
Run the CLI interface:


python3 agent.py
Web UI Usage
Select Operation: Choose an operation from the dropdown menu.
Enter Numbers: Provide the required numbers in the input fields.
Calculate: Click the "Calculate" button to see the result.
Cancel Operation: Click the "Cancel" button to stop the current operation.
Health Check: Click the "Health Check" button to view system status.
CLI Usage
Commands
Calculate: Enter the operation and numbers when prompted.
Cancel Operation: Type cancel to stop the current operation.
Health Check: Type health to check system status.
Exit: Type exit to quit the program.
Example CLI Session

$ python3 agent.py
AI Agent Calculator
Available operations: add, subtract, multiply, divide, sqrt, power
Type 'cancel' to cancel the current operation or 'health' to check status.

Enter operation: add
Enter first number: 5
Enter second number: 3
Result: 8.0

Enter operation: health
Status: {'status': 'healthy', 'operations_supported': ['add', 'subtract', 'multiply', 'divide', 'sqrt', 'power'], 'current_operation': 'add'}

Enter operation: cancel
Operation canceled.

Enter operation: exit
Health Check
The health check provides the following information:

Status: System health (healthy or unhealthy)
Supported Operations: List of available operations
Current Operation: The operation currently being processed (if any)
Error Handling
The AI Agent handles various error cases:

Invalid operations
Division by zero
Non-numeric inputs
Missing inputs
Error messages will be displayed clearly in both the CLI and UI.

Development
This project was developed to work within WebContainer's constraints:

No external dependencies
Uses only Python standard library
Runs entirely in the browser environment
License
This project is open-source and available for use under the MIT License.



---

### Comment utiliser ce fichier

1. Copiez le contenu ci-dessus.
2. Collez-le dans un fichier nommé `README.md`.
3. Enregistrez le fichier.

Ce fichier `README.md` est prêt à être utilisé pour documenter votre projet. Si vous avez besoin d'autres ajustements, faites-le moi savoir !
