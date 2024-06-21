class Connection:
    def __init__(self, host="LocalHost"):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection


p1 = Connection()
p1.set_user("Wagner")
p1.set_password(456)
print(p1)
print(p1.user, p1.password)
p2 = Connection.create_with_auth('larissa', 123)
print(p2)
print(p2.user, p2.password)
