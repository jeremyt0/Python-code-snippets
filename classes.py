
# Return attributes of a class	
class ClassName:
    var1 = 42
    def get_attributes(cls):
        attributes = [x for x in cls.__dict__.keys() if not x.startswith('_')]
	return attributes
attr = ClassName.get_attributes(ClassName)


