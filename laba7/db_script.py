import psycopg2
from psycopg2 import sql

# Параметри підключення до бази даних
connection_params = {
    "dbname": "mydatabase",
    "user": "user",
    "password": "password",
    "host": "localhost",
    "port": 5434
}

# Клас для роботи з базою даних
class Database:
    def __init__(self, connection_params):
        self.connection_params = connection_params

    def connect(self):
        try:
            self.conn = psycopg2.connect(**self.connection_params)
            self.cursor = self.conn.cursor()
            print("Підключено до бази даних.")
        except Exception as e:
            print("Помилка підключення:", e)

    def close(self):
        self.cursor.close()
        self.conn.close()

    def execute_query(self, query, params=None, fetch=False):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            if fetch:
                return self.cursor.fetchall()
        except Exception as e:
            print("Помилка виконання запиту:", e)
            self.conn.rollback()

    def create_tables(self):
        self.execute_query("""
            CREATE TABLE IF NOT EXISTS errors (
                error_id SERIAL PRIMARY KEY,
                description TEXT NOT NULL,
                received_date DATE NOT NULL,
                severity VARCHAR(20) NOT NULL,
                category VARCHAR(50),
                source VARCHAR(50)
            );
            CREATE TABLE IF NOT EXISTS programmers (
                programmer_id SERIAL PRIMARY KEY,
                last_name VARCHAR(50) NOT NULL,
                first_name VARCHAR(50) NOT NULL,
                phone VARCHAR(20) NOT NULL
            );
            CREATE TABLE IF NOT EXISTS error_fixes (
                fix_id SERIAL PRIMARY KEY,
                error_id INT REFERENCES errors(error_id) ON DELETE CASCADE,
                start_date DATE NOT NULL,
                duration INT NOT NULL,
                programmer_id INT REFERENCES programmers(programmer_id) ON DELETE CASCADE,
                cost_per_day NUMERIC(10, 2) NOT NULL
            );
        """)
        print("Таблиці успішно створені.")

    def insert_sample_data(self):
        # Вставка даних для прикладу
        for i in range(1, 21):
            self.execute_query("""
                INSERT INTO errors (description, received_date, severity, category, source)
                VALUES (%s, %s, %s, %s, %s)
                """, (f"Помилка {i}", f"2024-10-{i:02}", "критична" if i % 2 == 0 else "важлива", "інтерфейс", "користувач"))
        print("Зразкові дані для помилок додані.")

    def display_critical_errors(self):
        result = self.execute_query("SELECT * FROM errors WHERE severity = 'критична' ORDER BY error_id;", fetch=True)
        print("\nКритичні помилки:")
        for row in result:
            print(row)

    def count_errors_by_severity(self):
        result = self.execute_query("SELECT severity, COUNT(*) FROM errors GROUP BY severity;", fetch=True)
        print("\nКількість помилок за рівнями:")
        for row in result:
            print(row)

    def calculate_fix_cost(self):
        result = self.execute_query("""
            SELECT fix_id, error_id, (duration * cost_per_day) AS total_cost
            FROM error_fixes;
        """, fetch=True)
        print("\nВартість роботи для виправлення кожної помилки:")
        for row in result:
            print(row)

    def display_errors_by_source(self, source):
        result = self.execute_query("SELECT * FROM errors WHERE source = %s;", (source,), fetch=True)
        print(f"\nПомилки від джерела '{source}':")
        for row in result:
            print(row)

    def count_errors_by_source(self):
        result = self.execute_query("""
            SELECT source, COUNT(*)
            FROM errors
            WHERE source IN ('користувач', 'тестувальник')
            GROUP BY source;
        """, fetch=True)
        print("\nКількість помилок від користувачів та тестувальників:")
        for row in result:
            print(row)

    def count_errors_by_programmer_severity(self):
        result = self.execute_query("""
            SELECT p.programmer_id, p.last_name, p.first_name, e.severity, COUNT(*) as error_count
            FROM error_fixes ef
            JOIN errors e ON ef.error_id = e.error_id
            JOIN programmers p ON ef.programmer_id = p.programmer_id
            GROUP BY p.programmer_id, p.last_name, p.first_name, e.severity;
        """, fetch=True)
        print("\nКількість помилок, виправлених кожним програмістом за рівнями:")
        for row in result:
            print(row)

    def display_all_tables(self):
        tables = ["errors", "programmers", "error_fixes"]
        for table in tables:
            print(f"\nТаблиця {table}:")
            self.cursor.execute(f"SELECT * FROM {table};")
            columns = [desc[0] for desc in self.cursor.description]
            print(f"{' | '.join(columns)}")
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)


if __name__ == "__main__":
    db = Database(connection_params)
    db.connect()
    db.create_tables()
    db.insert_sample_data()
    db.display_critical_errors()
    db.count_errors_by_severity()
    db.calculate_fix_cost()
    db.display_errors_by_source('користувач')
    db.count_errors_by_source()
    db.count_errors_by_programmer_severity()
    db.display_all_tables()
    db.close()
