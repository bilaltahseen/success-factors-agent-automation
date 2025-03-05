# SAP Browser Agents

## Overview
SAP Browser Agents is an automated browser interaction tool designed to perform complex tasks in SAP SuccessFactors and other SAP applications. It uses AI-powered agents to navigate web interfaces, complete form submissions, and execute predefined workflows with precision and reliability.

## Key Features
- **Automated Browser Interaction**: Navigate and interact with SAP interfaces programmatically
- **Task-Based Execution**: Define precise sequences of steps to be executed by the agent
- **AI-Powered Navigation**: Leverages GPT-4o for understanding complex interfaces
- **Screenshot Capture**: Document process execution with automated screenshots
- **Robust Error Handling**: Retry mechanisms for handling unstable elements

## Use Cases
- **Permission Role Management**: Create and assign permission roles in SAP SuccessFactors
- **Automated Testing**: Verify functionality across SAP applications
- **Process Automation**: Automate repetitive administrative tasks
- **Training Documentation**: Generate visual documentation of SAP processes

## Architecture
The project is built with the following components:
- **Agent**: AI-powered automation agent that interprets tasks and executes actions
- **Controller**: Manages the registry of available actions and their execution
- **Browser Integration**: Direct control of Chrome browser instances through Playwright

## Prerequisites
- Python 3.12
- Google Chrome installed (path configurable in the agent.py file)
- SAP SuccessFactors access credentials

## Installation

### Setting up the environment
1. Clone this repository
2. Install dependencies:
   ```
   pipenv install
   ```
3. Create a .env file with your credentials:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

### Defining Tasks
Tasks are defined in the `tasks.py` file as strings containing step-by-step instructions for the agent to follow. The instructions should be precise and detailed.

### Running Tasks
To run a predefined task:
```python
python agent.py
```

### Custom Actions
Custom actions can be registered with the controller using decorators:
```python
@controller.registry.action("action_name")
async def custom_action(browser: BrowserContext, ...):
    # Action implementation
    return ActionResult(success=True, message="Action completed")
```

## Example Task
The project includes an example task for creating and assigning permission roles in SAP SuccessFactors, demonstrating how to:
1. Navigate to the SAP SuccessFactors login page
2. Authenticate with provided credentials
3. Create a new permission role with specific settings
4. Assign the role to HR managers
5. Capture screenshots at critical steps for documentation

## License
[Add appropriate license information here]

## Acknowledgements
This project uses [browser-use](https://github.com/browser-use/browser-use) for browser automation capabilities. 