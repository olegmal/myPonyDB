from pony.orm import db_session, select, left_join
from models import Employee

class Base:
    def __int__(self):
        self.model = None

    @db_session
    def get_by_id(self, id):
        entity = self.model.get(lambda emp: emp.id == id)
        return entity

    @db_session
    def delete_by_id(self, id):
        entity = self.get_by_id(id)
        entity.delete()

class EmployeeRepo(Base):
    def __int__(self):
        super().__int__()
        self.model = Employee

    @db_session
    def get_employee_by_id(self):
        employee = self.model.get(lambda emp: emp.id == id)
        return employee

    @db_session
    def update_by_id(self, id, new_email):
        employee = self.get_employee_by_id(id)
        employee.email = new_email

    @db_session
    def left_join(self):
        results = left_join(employee, bicycle) for employee in Employee for bicycle in employee.bicycle:
        for result in results:
            employee = result[0]
            bicycle = result[1]
            print(f"{employee} ||| {bicycle}")

    @db_session
    def delete_by_id(self, id):
        employee_to_delete = self.get_employee_by_id(id)
        employee_to_delete.delete()

    @db_session
    def delete_by_range(self):
        employees = self.model.select(lambda emp: emp.id > id)
        for emp in employees:
            emp.delete()


if __name__ == "__main__":
    employee_repo = EmployeeRepo()
    result = employee_repo.get_employee_by_id(2)
    # employee_repo.get_employee_by_id (3)
    # employee_repo.delete_by_id(4)
    print(result)

