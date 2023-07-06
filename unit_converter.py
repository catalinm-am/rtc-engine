import pint
ureg = pint.UnitRegistry()

ureg.define("lg = 15 grams")
ureg.define("lgt = 5 grams")

def converter(quantity, from_unit, to_unit):
    try:
        # convertim string-urile in unitati de masura
        first_unit = ureg.Unit(from_unit)
        second_unit = ureg.Unit(to_unit)

        # verificam compatibilitatea unitatilor de masura
        if first_unit.is_compatible_with(second_unit):
            # determinam greutatea finala 
            mass = quantity * ureg(from_unit)

            # convertim
            value = mass.to(to_unit)
            return value
        
        print(f"Unitatile de masura {from_unit} si {to_unit} nu sunt compatibile!")
    
    except pint.errors.UndefinedUnitError as e:
        print (f"Unitatea de masura furnizata nu este valida!")

if __name__ == "__main__":
    result = converter(89, "lgst", "grams")
    if result is not None:
        print(result)
