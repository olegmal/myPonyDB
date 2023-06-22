from pony.orm import Database, PrimaryKey, Optional, Required, Set, set_sql_debug

db = Database()
db.bind(provider='postgres', user='postgres', password='q9896', host='127.0.0.1',
        database='artlesscoder')


class Bicycle(db.Entity):
    _tablename_ = "bicycle"

    id = PrimaryKey(int, auto=True)
    make = Required(str, 15)
    type = Required(str, 15)
    price = Required(str, 10)
    employee = Set("Employee")

    def __str__(self):
        return f"id = {self.id},make = {self.make}, type = {self.type}, price = {self.price}"


class Employee(db.Entity):
    _tablename_ = "employee"

    id = PrimaryKey(int, auto=True)
    first_name = Required(str, 35)
    last_name = Required(str, 35)
    gender = Required(str, 15)
    email = Required(str, 50)
    date_of_birth = Required(int)
    country_of_birth = Required(str, 25)
    bicycle = Required(Bicycle, column="bicycle.id")


set_sql_debug()
db.generate_mapping(create_tables=False)
