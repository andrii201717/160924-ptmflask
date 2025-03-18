from models_relations import User, Project, ProjectsToUsers
from db_connection import DBConnection

from sqlalchemy_train import engine


# users = [
#     User()
#     User()
#     User()
#     User()
#     User()
#     User()
#     User()
# ]


with DBConnection(engine) as session:
    user = User(id=1, name='Julia', surname="Black")
    project = Project(id=1, name='First Project')

    proj_2_us = ProjectsToUsers(user.id, project.id)
    session.add(user)
    session.add(project)
    session.add(proj_2_us)

    # TODO: добавить альтернативный вариант записи объектов

    # session.add_all(users)
    session.commit()

