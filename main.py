from conection import *
from table import *
from nine import print_zavd
from faker_db import write
from zap import zapros


connection = create_connection(
    "postgres", "admin", "root", "127.0.0.1", "5432"
)

execute_query(connection, create_students_table)
execute_query(connection, create_subjects_table)
execute_query(connection, create_exams_table)

cur = connection.cursor()

write(cur)
# zapros(cur)
# print_zavd(cur)