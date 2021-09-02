# import os  # For random password salt generation
# self.saltbytes = os.urandom(32)
# self.password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), self.saltbytes, 1000000)
# dbconnection.submit_query(f'''
#                             INSERT INTO users (username, salt, pass) VALUES (
#                             "{username}",
#                             "{base64.b64encode(self.saltbytes).decode('utf-8')}",
#                             "{base64.b64encode(self.password).decode('utf-8')}"
#                             )''', echo=True)
