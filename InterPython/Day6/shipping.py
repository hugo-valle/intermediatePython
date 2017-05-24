import iso6346


class ShippingContainer:
    next_serial = 1337

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code, *args, **kwargs):
        return cls(owner_code, contents=None, *args, **kwargs)

    @classmethod
    #def create_with_items(cls, owner_code, items, *args, **kwargs):
    #    return cls(owner_code, contents=list(items),*args, **kwargs)
    def create_with_items(cls, owner_code, *items, **kwargs):
        return cls(owner_code, contents=list(items), **kwargs)

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        #self.serial = ShippingContainer._get_next_serial()
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._get_next_serial())


class RefrigeratorShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6),
                              category='R')

    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code, contents)
        if celsius > RefrigeratorShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature is too hot!")
        self._celsius = celsius # "Private" attribute

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, temperature):
        if temperature > RefrigeratorShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature is too hot!")
        self._celsius = temperature


def main():
    r = RefrigeratorShippingContainer.create_with_items(
        "ESE", ["broccoli", "carrots", "cauliflower"], celsius=2.0)
    print(r)
    print(r.contents)
    print(r.bic)
    print(r.celsius)
    r.celsius = 5.0
    print(r.celsius)



if __name__ == '__main__':
    main()
    exit(0)
