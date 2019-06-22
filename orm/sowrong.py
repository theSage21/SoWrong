import inspect
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()


def run(fn):
    for line in inspect.getsourcelines(fn)[0]:
        if line.strip().startswith("sql:"):
            sql = line.strip()[5:].strip()
            break
    sql = sql.replace(" . ", " ").split(" ")
    sql = " ".join(w if w != "frm" else "from" for w in sql)
    sql += "" if sql.endswith(";") else ";"
    print(sql)
    print("-" * 10)
    for row in c.execute(sql):
        print(row)
    print("")
    conn.commit()
