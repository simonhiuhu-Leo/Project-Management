from models.project import Project


class User:
    def __init__(self, username):
        self.username = username
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            "username": self.username,
            "projects": [project.to_dict() for project in self.projects]
        }