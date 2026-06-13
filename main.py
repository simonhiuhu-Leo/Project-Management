import argparse
from tabulate import tabulate

from models import User, Project, Task
from utils.storage import load_data, save_data


def create_user(username):
    data = load_data()

    user = User(username)

    data.append(user.to_dict())

    save_data(data)

    print("User created successfully!")


def list_users():
    data = load_data()

    if not data:
        print("No users found.")
        return

    table = []

    for user in data:
        table.append([user["username"]])

    print(tabulate(table,
                   headers=["Users"],
                   tablefmt="grid"))


def add_project(username, project_name):
    data = load_data()

    for user in data:
        if user["username"] == username:

            project = {
                "name": project_name,
                "tasks": []
            }

            user["projects"].append(project)

            save_data(data)

            print("Project added.")
            return

    print("User not found.")


def list_projects(username):
    data = load_data()

    for user in data:
        if user["username"] == username:

            table = []

            for project in user["projects"]:
                table.append([project["name"]])

            print(tabulate(table,
                           headers=["Projects"],
                           tablefmt="grid"))
            return

    print("User not found.")


def add_task(username, project_name, task_name):
    data = load_data()

    for user in data:

        if user["username"] == username:

            for project in user["projects"]:

                if project["name"] == project_name:

                    project["tasks"].append({
                        "name": task_name,
                        "completed": False
                    })

                    save_data(data)

                    print("Task added.")
                    return

    print("Project not found.")


def complete_task(username, project_name, task_name):
    data = load_data()

    for user in data:

        if user["username"] == username:

            for project in user["projects"]:

                if project["name"] == project_name:

                    for task in project["tasks"]:

                        if task["name"] == task_name:

                            task["completed"] = True

                            save_data(data)

                            print("Task completed.")
                            return

    print("Task not found.")


parser = argparse.ArgumentParser(
    description="Project Management CLI Tool"
)

subparsers = parser.add_subparsers(dest="command")


create_user_parser = subparsers.add_parser("create-user")
create_user_parser.add_argument("username")


list_users_parser = subparsers.add_parser("list-users")


project_parser = subparsers.add_parser("add-project")
project_parser.add_argument("username")
project_parser.add_argument("project_name")


list_project_parser = subparsers.add_parser("list-projects")
list_project_parser.add_argument("username")


task_parser = subparsers.add_parser("add-task")
task_parser.add_argument("username")
task_parser.add_argument("project_name")
task_parser.add_argument("task_name")


complete_parser = subparsers.add_parser("complete-task")
complete_parser.add_argument("username")
complete_parser.add_argument("project_name")
complete_parser.add_argument("task_name")


args = parser.parse_args()


if args.command == "create-user":
    create_user(args.username)

elif args.command == "list-users":
    list_users()

elif args.command == "add-project":
    add_project(args.username,
                args.project_name)

elif args.command == "list-projects":
    list_projects(args.username)

elif args.command == "add-task":
    add_task(args.username,
             args.project_name,
             args.task_name)

elif args.command == "complete-task":
    complete_task(args.username,
                  args.project_name,
                  args.task_name)