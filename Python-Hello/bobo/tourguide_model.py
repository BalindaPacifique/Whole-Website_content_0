import uuid
from datetime import datetime
from bobo import storage

class TourGuideModel():
    """This class will define the model for TourGiude"""
    def __init__(self, *args, **kwargs):
        """this module defines all the public instances for TourGiude"""
        super.__init__(self)
        if kwargs:
            for key, values in kwargs.items():
                if key == "created_at":
                    self.create_at = datetime.fromisoformat(kwargs["created_at"])
                if key == "updated_at":
                    self.updated_at = datetime.fromisoformat(kwargs["updated_at"])
                if key != "class":
                    setattr(self, key, values)
                if key == "class":
                    continue
        else:
            self.id = str(uuid.uuid4)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
    def save(self):
        """This module update my_dictionary for a new change"""
        self.updated_at = datetime.now()
        storage.save()
    def __str__(self):
        """This module defines the str format for TourGuide model"""
        return "<{}> [{}] {}".format(self.__class__.__name__, self.id, self.__dict__)
    def Model_dict(self):
        """This module organize all instance in a form of dictionary"""
        my_dictionary = self.__dict__.copy()
        
        my_dictionary["class"] = self.__class__.__name__
        my_dictionary['id'] = self.id
        my_dictionary["created_at"]= self.created_at.isoformat()
        my_dictionary["updated_at"]= self.updated_at.isoformat()

        return my_dictionary
# if __name__ =="__main__":
#     my_model = TourGuideModel()
#     my_model.name = "My First Model"
#     my_model.my_number = 89
#     print(my_model)
#     my_model.save()
#     print(my_model)
#     my_model_json = my_model.Model_dict()
#     print(my_model_json)
#     print("JSON of my_model:")
#     for key in my_model_json.keys():
#       print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
#     print("--")
#     my_new_model = TourGuideModel(**my_model_json)
#     print(my_new_model.id)
#     print(my_new_model)
#     print(type(my_new_model.created_at))

#     print("--")
#     print(my_model is my_new_model)