# J.A.B's Primary Backend
# As it stands, I hope to not just have a regular calculator, I want to try and use native TI libraries for it, So ill use inputs as placeholders for the later changes TI_systems methods

# Variable Bank

metricMassUnits = {
    "A": 1e12,
    "B": 1e9,
    "C": 1e6,
    "D": 1e3,
    "E": 1,
    "F": 1e-2,
    "G": 1e-3,
    "H": 1e-6,
    "I": 1e-9,
    "J": 1e-12,
}


imperialMassUnits = {}


def impAndMetConversion():  # Imperial -> Metric or Metric -> Imperial
    isMetricStr = input("Metric -> Imperial? (Y/N)")
    if isMetricStr == "" or isMetricStr == "y" or isMetricStr == "Y":
        selector = int(
            input(
                """What are you measuring?
                             
                             1. Mass
                             2. Distance
                             3. """
            )
        )  # I wanna seperate fundemental measurement and derived. Basically, once u convert one, another function can do the derived with the same num

        if selector == 1:
            firstValue = input(
                """Input Mass Value(float) followed by the corresponding letter:
                             
                             A. Teragram (e12)
                             B. Gigagram (e9)
                             C. Megagram (e6)
                             D. Kilogram (e3)
                             E. Gram (e0)
                             F. Centigram (e-2)
                             G. Milligram (e-3)
                             H. Microgram (e-6)
                             I. Nanogram (e-9)
                             J. Picogram (e-12)"""
            )
            secondValue = input(
                """Input Imperial Mass Value(float) followed by corresponding letter:
                                
                             A. Ounce
                             B. Pounds"""
            )
