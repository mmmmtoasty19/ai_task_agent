### Basic Tasks Overall Checklist
- [x] Set up SQLite database with tasks table
- [x] Build add_task and list_tasks functions
- [x] Create simple command parser (if input starts with "add", call add_task)
- [x] Add a main loop to keep the agent running


### Main Functions

- [x] add_task(description, priority, due_date) - Creates new task
- [x] list_tasks(filter) - Shows tasks (all, pending, completed, by priority)
- [ ] complete_task(task_id) - Marks task as done
- [ ] delete_task(task_id) - Removes a task
- [ ] update_task(task_id, field, new_value) - Edit task details

### Optional Enhancements
- [ ] data validation (e.g., valid date format)
- [ ] error handling (e.g., task not found)
