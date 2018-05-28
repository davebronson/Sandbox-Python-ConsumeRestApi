class Address(object):
    '''
    Represents a place of residence for a person or business.

    Attributes:
        userId: The ID of the User that this Address belongs to.
        street: The number and street name.
        suite: The suite or apartment number, if any.
        city: The name of the city or town.
        zipCode: The postal code that the Address exists within.
        geoLatitude: The precise north-south geographic location on the surface
            of the Earth.
        geoLongitude: The precise east-west geographic location on the surface
            of the Earth.
    '''

    def __init__(self):
        '''
        Initializes Address with default values.
        '''
        self.userId = None
        self.street = None
        self.suite = None
        self.city = None
        self.zipCode = None
        self.geoLatitude = None
        self.geoLongitude = None