class Element:
    def __init__(self, name : str, symbol : str, Z : int):
        self.name = name
        self.symbol = symbol
        self.Z = Z
        
    def __repr__(self):
        return "Element(\"{0}\", Z={1})".format(self.name, self.Z)
        
    def __str__(self):
        return self.symbol
            
    
class _Table:
    def __init__(self):
        self._data = [
            Element("Hydrogen", "H", 1),
            Element("Helium", "He", 2),
            Element("Lithium", "Li", 3),
            Element("Beryllium", "Be", 4)
        ]
        for element in self._data:
            setattr(self, element.symbol, element)
            setattr(self, element.name, element)
        
    def __getitem__(self, x):
        if isinstance(x, int):
            return next((element for element in self._data if element.Z == x), None)
        elif isinstance(x, str):
            if len(x) <= 2:
                return next((element for element in self._data if element.symbol == x), None)
            else:
                return next((element for element in self._data if element.name == x), None)
        else:
            raise IndexError()
            
    def __iter__(self):
        return iter(self._data)

                
table = _Table()
    
    
class Isotope:
    def __init__(self, element, A : int):
        self.element = as_element(element)
        self.A = A
        
    def __getattr__(self, name):
        return getattr(self.element, name)
        
    def __str__(self):
        return "{0}-{1}".format(self.element.symbol, self.A)
        
    @property
    def Z(self) -> int:
        return self.element.Z
        
    @property
    def N(self) -> int:
        """Number of neutrons."""
        return self.A - self.Z
        
        
def as_element(a):
    if isinstance(a, Element):
        return a
    else:
        return table[a]
        
def as_isotope(a):
    if isinstance(a, Isotope):
        return a
    if isinstance(a, (tuple, list)):
        return Isotope(*a)
    if isinstance(a, str):
        raise NotImplementedError()