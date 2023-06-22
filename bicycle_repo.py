from pony.orm import db_session, select
from models import Bicycle
from employee_repo  import Base


class BicycleRepo(Base):
    def __int__(self):
        self.model = Bicycle

    @db_session
    def get_bike_by_id(self):
        bicycle = self.model.get(lambda b: b.id == id)
        return bicycle


    @db_session
    def get_all_with_lambda(self):
        bicycle = Bicycle.select(lambda  bicycle: bicycle)
        return bicycle.page(1).to_list()

    @db_session
    def update_type_by_id(self, id, new_type):
        bicycle = self.get_bike_by_id(id)
        bicycle.type = new_type


    @db_session
    def delete_by_id(self, id):
        bicycle_to_delete = self.get_bike_by_id(id)
        bicycle_to_delete.delete()

if __name__ == "__main__":
    bike_repo = BicycleRepo()
    result = bike_repo.get_bike_by_id(2)
    # bikes = bike_repo.get_all_with_lambda()
    # for bike in bikes:
    #     print(bike.type)
    print(result)