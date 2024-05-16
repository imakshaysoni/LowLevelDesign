class User:
    _id = 1

    def __init__(self, name, driving_licence_no):
        self.id = User._id
        self.name = name
        self.dl_no = driving_licence_no
        User._id += 1
