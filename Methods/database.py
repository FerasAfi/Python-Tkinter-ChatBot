import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


db = mysql.connector.connect(host="localhost",
    user=os.getenv("DATA_BASE_USER"),
    password=os.getenv("DATA_BASE_PASSWORD"),
    port=int(os.getenv("DATA_BASE_PORT")),
    database=os.getenv("DATA_BASE_NAME"))

cursor = db.cursor()



create_table_query = """CREATE TABLE users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(100) UNIQUE NOT NULL,
                    password VARCHAR(100) NOT NULL,
                    gender ENUM('male', 'female') NOT NULL,
                    secret_question VARCHAR(255) NOT NULL,
                     secret_question_answer VARCHAR(255) NOT NULL
                     );"""

create_conversation_query = """CREATE TABLE conversations (
                            id INT PRIMARY KEY AUTO_INCREMENT,
                            user_id INT NOT NULL,
                            title VARCHAR(100) NOT NULL,
                            creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (user_id) REFERENCES users(id)
                            );"""
            
create_message_query = """CREATE TABLE messages (
                        message_id INT PRIMARY KEY AUTO_INCREMENT,
                        convo_id INT NOT NULL,
                        sender ENUM('user', 'ai') NOT NULL,
                        content TEXT NOT NULL,
                        sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (convo_id) REFERENCES conversations(id)
                        );"""
"""
cursor.execute(create_message_query)
db.commit()
"""






def user_check(username):
    try:
        with db.cursor() as cursor:
            check=("SELECT * FROM users WHERE username=%s")
            cursor.execute(check, (username, ))
            user = cursor.fetchone()
            if user:
                return 1
            else:
                return 0
    except mysql.connector.Error as err:
            print(f"Error: {err}")

def insert_info(username, password, secret_question, secret_question_answer):
    try:
        with db.cursor() as cursor:
            insert = ("INSERT INTO users (username, password, secret_question, secret_question_answer) VALUES (%s, %s, %s, %s)")
            cursor.execute(insert, (username, password, secret_question, secret_question_answer))
            db.commit()
            return 1
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return 0
    finally:
        cursor.close()

def login_check(username, password):
    try:
        with db.cursor() as cursor:
            check=("SELECT * FROM USERS WHERE username=%s AND password=%s ")
            cursor.execute(check, (username, password))
            user=cursor.fetchone()
            if user:
                return 1
            else:
                return 0

    except mysql.connector.Error as err:
            print(f"Error: {err}")

def get_user_id(username, password):
    try:
        with db.cursor(dictionary=True) as cursor:
            check=("SELECT id FROM users WHERE username=%s AND password=%s ")
            cursor.execute(check, (username, password))
            id=cursor.fetchone()
            if id:
                return (id['id'])
            else:
                return 0
    except mysql.connector.Error as err:
            print(f"Error: {err}")

def reset_password(username, password):
    try:
        with db.cursor() as cursor:
            update = ("UPDATE users SET password = %s WHERE username = %s")
            cursor.execute(update, (password, username))
            db.commit()
            return 1
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return 0
    finally:
        cursor.close()

def check_answer(username, question, answer):
    try:
        with db.cursor() as cursor:
            check=("SELECT * FROM USERS WHERE username=%s AND secret_question = %s AND secret_question_answer = %s" )
            cursor.execute(check, (username, question, answer))
            user=cursor.fetchone()
            if user:
                return 1

            else:
                return 0

    except mysql.connector.Error as err:
            print(f"Error: {err}")

def create_new_convo(user_id, title):
    try:
        with db.cursor() as cursor:
            insert = ("INSERT INTO conversations (user_id, title) VALUES (%s, %s)")
            cursor.execute(insert, (user_id, title))
            db.commit()
            return 1
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return 0
    finally:
        cursor.close()

def insert_message(convo_id,sender, message):
    try:
        with db.cursor() as cursor:
            insert = ("INSERT INTO messages (convo_id, sender, content) VALUES (%s, %s, %s)")
            cursor.execute(insert, (convo_id,sender,message ))
            db.commit()
            return 1
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return 0
    finally:
        cursor.close()

def get_all_chat(user_id):
    try:
        with db.cursor(dictionary=True) as cursor:
            check=("SELECT title, id FROM conversations WHERE user_id=%s")
            cursor.execute(check, (user_id,))
            titles=cursor.fetchall()
            if id:
                return titles
            else:
                return 0
    except mysql.connector.Error as err:
            print(f"Error: {err}")

def delete_chat(chat_id):
    delete_messages(chat_id)
    try:
        with db.cursor() as cursor:
            delete = ("DELETE FROM conversations WHERE id = %s")
            cursor.execute(delete, (chat_id, ))
            db.commit()
            return 1
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return 0
    finally:
        cursor.close()

def delete_messages(chat_id):
    try:
        with db.cursor() as cursor:
            delete = ("DELETE FROM messages WHERE convo_id = %s")
            cursor.execute(delete, (chat_id,))
            db.commit()
            return 1
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return 0
    finally:
        cursor.close()

def load_messages(chat_id):
    try:
        with db.cursor(dictionary=True) as cursor:
            check=("SELECT content, sender FROM messages WHERE convo_id=%s")
            cursor.execute(check, (chat_id,))
            messages=cursor.fetchall()
            if messages:
                return messages
            else:
                return 0
    except mysql.connector.Error as err:
            print(f"Error: {err}")






