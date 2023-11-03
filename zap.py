from tabulate import tabulate
def zapros(cur):
    cur.execute("""
    SELECT "Складання іспитів"."код студента", "Прізвище студента", "Ім'я студента", "По батькові студента", "курс", "факультет"
    FROM "Складання іспитів"
    INNER JOIN Студенти ON "Складання іспитів"."код студента" = Студенти."Код студента"
    WHERE Студенти."чи є старостою" = 'Так'
    ORDER BY "Прізвище студента";
    """)
    results = cur.fetchall()

    columns = [desc[0] for desc in cur.description]
    print(tabulate(results, headers=columns, tablefmt="pretty"))

    cur.execute("""
        SELECT "Складання іспитів"."код студента", "Прізвище студента", "Ім'я студента", ROUND(AVG("отримана_оцінка"), 1) AS "Середній бал"
        FROM "Складання іспитів"
        INNER JOIN Студенти ON "Складання іспитів"."код студента" = Студенти."Код студента"
        GROUP BY "Складання іспитів"."код студента", "Прізвище студента", "Ім'я студента"
        ORDER BY "Прізвище студента";
        """)
    results = cur.fetchall()

    columns = [desc[0] for desc in cur.description]
    print(tabulate(results, headers=columns, tablefmt="pretty"))

