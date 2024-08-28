from bobo.tourguide_model import TourGuideModel
import json
import os

class TourGuideFilestorage():
    """This class saves all the data from diffrent class into json files"""
    __objects = {}
    _file = "tourguide_jsonfile.json"
    CLASSES = {
        "TourGuideModel" : TourGuideModel
    }

    def all(self):
        """This moduel returns the official dictionary for tourguide"""
        return self.__objects

    def new(self, obj):
        """This module returns the new and updated dictionayry"""
        key = "<{}>.{}}".format(self.__class__.__name__, obj.id)
        self.__objects[key] = obj()
    def save(self):
        """ This moduel save all the data into a json file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.Model_dict()
            with open (self._file, "w") as file:
                json.dump(serialized_objects, file)
    def reload(self):
        """This module reloads all the serialized data from a json file to a dictionary"""
        if os.path.isfile(self._file):
            deserialized_objects = json.reload(self._file)
            try:
                for key, obj in deserialized_objects.items():
                  class_name, obj_id = key.split(".")
                  clss_name = eval(class_name)
                  instance = clss_name(**obj)
                  self.__objects[key] = instance
            except Exception as e :
                pass
if __name__ == "__main__":
    from bobo import storage
    from bobo.tourguide_model import TourGuideModel
    
    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)
        
        print("-- Create a new object --")
        my_model = TourGuideModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        print(my_model)
