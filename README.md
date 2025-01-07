# langchain-research
### Knowledge Base QA Bot


## Installation

Firstly install UV packet manager 

```
On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```
```
On Windows.
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```
To install dependencies 
```
uv pip install -r requirements.txt
```

To install hooks follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the cloned directory and run:

   ```sh
   pre-commit install
   pre-commit install --hook-type commit-msg    

   ```
### Pre-commit Hooks

Example commit message, `feat/add example`, adheres to the specified format and successfully communicates the necessary details about the commit:

feature: Indicates that the commit introduces a new feature to the project.
PT-3581: Specifies the ticket or issue number from the project's tracking system.
add example: Provides a concise description of what the commit does — in this case, adding an example to the project.
