from clcrypto import hash_password
class User():

    def __init__(self, username="", password="",slat=""):
        self._id = -1
        self.username = username
        self._hashed_password = hash_password(password, slat)

    @property
    def id(self):
        return self._id

    @property
    def hash_password(self):
        return self._hashed_password


    def set_password(self, password, salt=""):
        self._hashed_password = hash_password(password, salt)

    @hash_password.setter
    def hash_password(self, password):
        self.set_password(password)

    def save_to_db(self, cursor):
        if self._id == -1:
            sql = """INSERT INTO users(username, hashed_password)
                            VALUE(%s, %s) RETURNING id"""
            values = (self.username, self.hashed_password)
            cursor.execute(sql, values)
            self._id = cursor.fetchone()[0]
            return True
        else:
            sql = """UPDATE Users SET username=%s, hashed_password=%s WHERE id=%s"""
            values = (self.username, self._hashed_password)
            cursor.execute(sql, values)
            return True

    @staticmethod
    def load_user_by_id(curosr, id_):
        sql = "SELECT id, username, hashed_password from users WHERE id=%s"
        curosr.execute(sql, (id_,))
        data = curosr.fetchone()
        if data:
            id_, username, hashed_password = data
            loaded_user = User(username)
            loaded_user._id = id_
            loaded_user._hashed_password = hashed_password
            return loaded_user
        else:
            return None


    @staticmethod
    def load_all_users(cursor):
        sql = """SELECT id, username, hashed_password FROM Users"""
        users = []
        cursor.execute(sql)
        for row in cursor.fetchall():
            id_, username, hashed_password = row
            loaded_user = User()
            loaded_user._id = id_
            loaded_user.username = username
            loaded_user._hashed_password = hashed_password
            users.append(loaded_user)
        return users







print(User.load_all_users('marcin'))

    





