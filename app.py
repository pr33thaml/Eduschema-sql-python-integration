import mysql.connector

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",   # replace with your MySQL username
            password="admin",   # replace with your MySQL password
            database="userdb"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def insert_user(conn, name, age, city):
    cursor = conn.cursor()
    query = "INSERT INTO users (name, age, city) VALUES (%s, %s, %s)"
    values = (name, age, city)
    try:
        cursor.execute(query, values)
        conn.commit()
        print("User inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    cursor.close()

def main():
    conn = connect_to_database()
    if conn:
        insert_user(conn, "Alice", 30, "New York")
        insert_user(conn, "Bob", 25, "Los Angeles")
        conn.close()

if __name__ == "__main__":
    main()
