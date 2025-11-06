class CreateUserDto:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class UpdateUserDto:
    def __init__(self,user_id, username, email, password, level, xp, created_at, image_path):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.level = level
        self.xp = xp
        self.created_at = created_at
        self.image_path = image_path
