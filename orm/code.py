from sowrong import run


def create_user_table():
    sql: create.table.user(name.text, age.real)


def insert_values():
    sql: insert.into.user.values("arjoonn", 600)


def show_table():
    sql: select * frm.user


run(create_user_table)
run(show_table)
run(insert_values)
run(show_table)
