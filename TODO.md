### Basic Tasks Overall Checklist
- [ ] Set up SQLite database with tasks table
- [ ] Build add_task and list_tasks functions
- [ ] Create simple command parser (if input starts with "add", call add_task)
- [ ] Add a main loop to keep the agent running


### Main Functions

- [x] add_task(description, priority, due_date) - Creates new task
- [x] list_tasks(filter) - Shows tasks (all, pending, completed, by priority)
- [ ] complete_task(task_id) - Marks task as done
- [ ] delete_task(task_id) - Removes a task
- [ ] update_task(task_id, field, new_value) - Edit task details


# AI Agent Implementation Checklist

## 1. Define Tool for Claude
- [ ] Create a Pydantic model for the tool schema (describes the `add_task` function to Claude)
- [ ] Include fields: description, priority, status, due_date, completed_date
- [ ] Make sure it matches your Task model structure

## 2. Create Tool Execution Handler
- [ ] Write a function that processes tool calls from Claude
- [ ] Extract the tool parameters from Claude's response
- [ ] Create a Task object from those parameters
- [ ] Call your `add_task()` function
- [ ] Return a result message (success/failure)

## 3. Build the Conversation Loop
- [ ] Set up the main agent loop in `main()`
- [ ] Get user input
- [ ] Send message to Claude with the tool definition
- [ ] Check if Claude wants to use a tool
- [ ] If yes: execute the tool, send result back to Claude
- [ ] If no: display Claude's response to user
- [ ] Loop until user exits

## 4. System Prompt
- [ ] Write a system prompt telling Claude it's a task manager assistant
- [ ] Explain when to use the add_task tool
- [ ] Give it personality/guidelines for interaction

## 5. Testing
- [ ] Test: "Add a task to buy groceries with high priority"
- [ ] Test: Natural language variations
- [ ] Test: Missing information (does Claude ask for it?)