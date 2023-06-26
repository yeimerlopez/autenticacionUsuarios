from .entities.User import User

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password, fullname FROM user 
                    WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)  


    @classmethod
    def create_user(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO user (username, password, fullname) 
                    VALUES ('{}', '{}', '{}')""".format(user.username, user.password, user.fullname)
            cursor.execute(sql)
            db.connection.commit()
            
            user_id = cursor.lastrowid
            new_user = User(user_id, user.username, user.password, user.fullname )
            return new_user
        except Exception as ex:
            raise Exception(ex)

