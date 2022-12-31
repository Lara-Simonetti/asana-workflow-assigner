# Import the Asana library and your information
import asana
import your_info

#Get access to Asana
personal_access_token = your_info.personal_access_token

client = asana.Client.access_token(personal_access_token)

#Get the workflow tasks
workflow_tasks = client.tasks.subtasks(your_info.workflow)

#Assign tasks according to your roles list
for task in workflow_tasks:
    for role, role_gid in your_info.roles.items():
        if task['name'].startswith(role):
            client.tasks.update_task(task['gid'], {'assignee': role_gid})

print("Your workflow has been processed!")