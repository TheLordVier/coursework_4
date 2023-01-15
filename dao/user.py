# Импортируем модель User
from dao.model.user import User


# Создаём класс UserDAO
class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def get_by_username(self, username):
        return self.session.query(User).filter(User.name == username).one_or_none()

    def get_user_by_email(self, email):
        return self.session.query(User).filter(User.email == email).one_or_none()

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def update(self, user_d):
        user = self.get_one(user_d.get("id"))

        for key, value in user_d.items():
            setattr(user, key, value)

        self.session.add(user)
        self.session.commit()

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()
