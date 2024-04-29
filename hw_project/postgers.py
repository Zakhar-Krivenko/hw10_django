import psycopg2

try:
    # Підключення до бази даних
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="567234",
        host="localhost",
        port="5432"
    )
    print("Підключення успішно встановлено")
    
    


    # Закриття підключення
    conn.close()
except psycopg2.Error as e:
    print(f"Помилка підключення: {e}")