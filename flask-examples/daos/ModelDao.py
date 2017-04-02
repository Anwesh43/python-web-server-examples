class ModelDao:
    def create(self,Model,**dict):
        model = Model(**dict)
        model.save()

    def findObjects(self,Model):
        objects = []
        for object in Model.objects:
            objects.append(object)
        return  objects
