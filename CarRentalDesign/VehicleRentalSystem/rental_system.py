from LowLevelDesign.CarRentalDesign.Store.store import Store
from LowLevelDesign.CarRentalDesign.User.user import User


class VehicleRentalSystem:
    def __init__(self, stores_list=None, users_list=None):
        self.stores = stores_list if stores_list else []
        self.users = users_list if users_list else []

    def create_store(self, location):
        store_obj = Store(location)
        self.stores.append(store_obj)
        return store_obj

    def get_store(self, location):
        for store in self.stores:
            if store.location == location:
                return store
        return None

    def create_user(self, name, driving_licence_no):
        user = User(name, driving_licence_no)
        self.users.append(user)
        return user
