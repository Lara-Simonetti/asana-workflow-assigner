# Asana Workflow Assigner
This is a simple script to automate assigning an Asana task's subtasks to multiple users.
## How to Use
### Preparing your Subtasks
This script uses "roles" at the beginning of a subtask's name to assign them to a particular user. For example, if you would like all administrative tasks to be assigned to the same user, you would want all of those subtasks to begin with an identifier for that role. Some examples:\
`ADMIN: Schedule Project Management Meeting`\
`Admin - Schedule Project Management Meeting`\
Whatever the role identifier is, the script will look for subtasks that begin with that word and assign them to the same user.
### Running this Script
1. Clone this repository.
2. Install [Asana's Python client library](https://github.com/Asana/python-asana/).
3. Open the `your_info.py` file.
4. Replace the `roles` dict to reflect your roles (as keys) and the GID of the user those tasks should be assigned to (as values). Please keep in mind that GID should be of `str` type.
5. Replace the `workflow` variable with the GID of the parent task you would like to run the assigner on.
6. Replace the `personal_access_token` variable with your Asana personal access token.
7. Run the script on the terminal with `python workflow_assigner.py`.
8. The script will print `Your workflow has been processed!` once all the subtasks have been assigned! 🎉
## Technical Features
These are some of the skills displayed in this project:
* Knowledge of Asana's API and its Python client library
* Python
