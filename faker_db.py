import random
from table import*
from middle_name import*
from faker import Faker
from datetime import date

fake = Faker('uk_UA')
starost = ['Так','Ні']

def write(cur):
    for _ in range(11):
        last_name = fake.last_name()
        first_name = fake.first_name()
        middle_name = fake.random_element(ukrainian_middle_names)
        address = fake.address()
        phone = fake.phone_number()
        course = fake.random_int(min=1, max=4)
        faculty = fake.random_element(["Аграрний менеджмент", "Економіка", "Інформаційні технології"])
        group = fake.random_int(min=1, max=4)
        is_head = fake.random_element(starost)

        cur.execute(
            "INSERT INTO Студенти (\"Прізвище студента\", \"Ім'я студента\", \"По батькові студента\", \"Адреса студента\", \"телефон студента\", \"курс\", \"факультет\", \"група\", \"чи є старостою\") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (last_name, first_name, middle_name, address, phone, course, faculty, group, is_head)
        )

    # Додавання даних про предмети
    subject_data = [
        ('Захист Рослин', 60, 2),
        ('Бізнес Економіка', 45, 2),
        ('Програмуваня з Python', 30, 1),
    ]

    for subject in subject_data:
        cur.execute("INSERT INTO Предмети (\"назва\", \"кількість годин за семестр\", \"кількість семестрів\") VALUES (%s, %s, %s)", subject)
    cur.execute("SELECT \"Код студента\" FROM Студенти")
    students = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT \"Код предмету\" FROM Предмети")
    subjects = [row[0] for row in cur.fetchall()]


    # Обмеження для дат складання іспитів
    start_date = date(2023, 11, 27)
    end_date = date(2023, 12, 30)

    # Заповнення таблиці "Складання іспитів" фіктивними даними
    for _ in range(20):  # Заповнюємо 20 записів
        exam_date = fake.date_between_dates(start_date, end_date)
        student_id = random.choice(students)
        subject_id = random.choice(subjects)
        grade = random.randint(2, 5)

        cur.execute(
            "INSERT INTO \"Складання іспитів\" (\"дата складання\", \"код студента\", \"код предмету\", \"отримана_оцінка\") "
            "VALUES (%s, %s, %s, %s)",
            (exam_date, student_id, subject_id, grade)
        )