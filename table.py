create_students_table= ("""
    CREATE TABLE IF NOT EXISTS Студенти (
        "Код студента" SERIAL PRIMARY KEY,
        "Прізвище студента" VARCHAR(255),
        "Ім'я студента" VARCHAR(255),
        "По батькові студента" VARCHAR(255),
        "Адреса студента" VARCHAR(255),
        "телефон студента" VARCHAR(255),
        "курс" INTEGER CHECK (курс BETWEEN 1 AND 4),
        "факультет" VARCHAR(255),
        "група" INTEGER,
        "чи є старостою" VARCHAR(255)
    )
""")

# Створення таблиці "Предмети"
create_subjects_table= ("""
   CREATE TABLE IF NOT EXISTS "Предмети" (
        "Код предмету" SERIAL PRIMARY KEY,
        "назва" VARCHAR(255),
        "кількість годин за семестр" INTEGER,
        "кількість семестрів" INTEGER
)
""")

# Створення таблиці "Складання іспитів"
create_exams_table= ("""
    CREATE TABLE IF NOT EXISTS "Складання іспитів" (
        "Код складання" SERIAL PRIMARY KEY,
        "дата складання" DATE,
        "код студента" INTEGER REFERENCES Студенти("Код студента"),
        "код предмету" INTEGER REFERENCES Предмети("Код предмету"),
        "отримана_оцінка" INTEGER CHECK (отримана_оцінка BETWEEN 2 AND 5)
    )
""")