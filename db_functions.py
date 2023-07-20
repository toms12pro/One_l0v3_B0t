import sqlite3

class Database(object):
    def __init__(self):
        self.conn = sqlite3.connect('db.sqlite')
        self.c = self.conn.cursor()
        self.initialize_db()

    def initialize_db(self):
        '''Creates necessary tables if they do not exist'''
        with self.conn:
            self.c.execute("CREATE TABLE IF NOT EXISTS user_info(chat_id INTEGER, user TEXT, key TEXT,secret TEXT)")
            #self.c.execute("INSERT INTO user_info (chat_id, user, key, secret) VALUES (0, 'None', 'None', 'None')")
    
    #execute and return info
    def query(self, sql_str):
        with self.conn:
            _tuple = self.c.execute(sql_str)
        return  _tuple    
    #execute no info                
    def execute(self, sql_str):
        with self.conn:
            _tuple = self.c.execute(sql_str)
           
            #self.c.execute("UPDATE user_info SET chat_id=?", (chat_id,))
  
