import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            email varchar(255),
            language varchar(3),
            PRIMARY KEY (id)
            );
"""

        self.execute(sql, commit=True)

    def create_table_main(self):
        sql = """
            CREATE TABLE Main (
                id int PRIMARY KEY NOT NULL,
                qollanma TEXT NULL,
                shartlar TEXT NULL
                );
    """
        self.execute(sql, commit=True)

    def create_table_kanal(self):
        sql = """
        CREATE TABLE Kanal (
            id int PRIMARY KEY NOT NULL,
            username TEXT NOT NULL,
            kunlikpm TEXT NOT NULL,
            obunachilari INTEGER NOT NULL,
            kanalnomi TEXT NOT NULL,
            type1 INTEGER NOT NULL,
            type2 INTEGER NOT NULL,
            type3 INTEGER NOT NULL,
            slug TEXT NOT NULL
            );
"""
        self.execute(sql, commit=True)

    def create_table_bot(self):
        sql = """
            CREATE TABLE Bot (
                id int PRIMARY KEY NOT NULL,
                username TEXT NOT NULL,
                obunachilari INTEGER NOT NULL,
                botnomi TEXT NOT NULL,
                rekpuli INTEGER NOT NULL
                );
    """
        self.execute(sql, commit=True)


    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email: str = None, language: str = 'uz'):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, Name, email, language) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, email, language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)



    def select_qollanma(self):
        sql = """
        SELECT qollanma FROM Main
        """
        return self.execute(sql, fetchall=True)

    def select_shartlar(self):
        sql = """
        SELECT shartlar FROM Main
        """
        return self.execute(sql, fetchall=True)

    def select_kanal(self, slug: str):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Kanal WHERE slug=?"
        sql, parameters = self.format_args(sql, slug)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


def logger(statement):
    print(f"""
_____________________________________________________
Executing:
{statement}
_____________________________________________________
""")
