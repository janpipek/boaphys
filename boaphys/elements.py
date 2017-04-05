class Element:
    pass
    

def as_element(a):
    if isinstance(a, Element):
        return a
    elif isinstance(a, str):
        pass
    elif isinstance(a, int):
        pass
    
    
class Isotope:
    def __init__(self, element, A : int):
        self.element = as_element(element)
        self.A = A
        
    def __getattr__(self, name):
        return getattr(self.element, name)
        
    @property
    def N(self) -> int:
        """Number of neutrons."""
        return self.A - self.Z
    
        