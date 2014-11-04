class HighQualityBikeMixin(object):
    def rating(self):
        return "High Quality"

class LowQualityBikeMixin(object):
    def rating(self):
        return "Low Quality"

class BikeMetaClass(type):
    makes = {}

    def __init__(cls, name, bases, classdict):
        super(BikeMetaClass, cls).__init__(cls, bases, classdict)
        if not BikeBase in bases:
            BikeMetaClass.makes[name] = cls

    def __call__(self, *args, **kwargs):
        make = kwargs.get('make').title()
        quality_class = kwargs.get('quality') > 5 and HighQualityBikeMixin or LowQualityBikeMixin

        if BikeMetaClass.makes.has_key(make) and not (self is BikeMetaClass.makes[make]):
            obj = BikeMetaClass.makes[make].__call__(*args, **kwargs)
        else:
            obj = None
            if not BikeMetaClass.makes.has_key(self.__name__):
                # create a new class for this type by mixing in the appropriate class
                new_class = BikeMetaClass(make, (GenericBike, quality_class), {}) 
                globals()[make] = new_class
                obj = new_class(*args, **kwargs)
            else:
                obj = super(BikeMetaClass, self).__call__(*args, **kwargs)

        return obj
        
class BikeBase(object):
    pass

class Bike(BikeBase):
    __metaclass__ = BikeMetaClass
    
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return "%s: %s" % (self.make, self.rating())

class GenericBike(Bike):
    def __init__(self, **kwargs):
        kwargs['make'] = self.__class__.__name__
        super(GenericBike, self).__init__(**kwargs)

data_source = (
    {'make': 'huffy', 'quality': 1},
    {'make': 'colnago', 'quality': 10},
    {'make': 'bianchi', 'quality': 8}
)

bikes = []
for record in data_source:
    bike = Bike(**record)
    bikes.append(bike)

for bike in bikes:
    print type(bike)
    print bike
    print
