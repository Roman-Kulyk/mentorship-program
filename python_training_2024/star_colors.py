"""
Implement python sprint  that calculate visible color of star based on its
temperature.

The colors can be blue, white, yellow, orange and red.

Input of the script should be dictionary where key is name of the star and
value is a temperature

Output of the script schould be colors separated by newlines that has at least
one star  in it spectrum and star name separated by comma.

Script should has at least two functions: one for calculating values and one
for printing it.
"""
star_temperatures = {"Achernar": 15200,
                    "Acrux": 28000,
                    "Adhafera": 4550,
                    "Adhara": 22800,
                    "Alcor": 7400,
                    "Alcyone": 12000,
                    "Aldebaran": 3900,
                    "Alderamin": 7400,
                    "Algenubi": 4840,
                    "Algol A": 12200,
                    "Algorab": 11600,
                    "Alhena": 9260,
                    "Alioth": 9400,
                    "Alkaid": 9600,
                    "Alnilam": 27500,
                    "Alnitak": 29000,
                    "Alpha Centauri A": 5790,
                    "Alphard": 4030,
                    "Alphecca": 9000,
                    "Alpheratz": 13500,
                    "Alsephina": 25000,
                    "Altair": 7500,
                    "Aludra": 22500,
                    "Ankaa": 4930,
                    "Antares": 3100,
                    "Arcturus": 4290,
                    "Atlas": 9800,
                    "Avior": 5300,
                    "Bellatrix": 21500,
                    "Betelgeuse": 3500,
                    "Canopus": 7350,
                    "Capella Aa": 5890,
                    "Caph": 7000,
                    "Castor": 10100,
                    "Celaeno": 10600,
                    "Chertan": 9300,
                    "Cursa": 7400,
                    "Deneb": 8500,
                    "Denebola": 8500,
                    "Dubhe": 4800,
                    "Electra": 12800,
                    "Elnath": 13300,
                    "Eltanin": 3900,
                    "Enif": 3000,
                    "Errai": 4750,
                    "Fomalhaut": 8590,
                    "Gacrux": 3640,
                    "Gienah": 9400,
                    "Grumium": 3700,
                    }

star_colors = {'blue':[], 'white':[], 'yellow':[], 'orange':[], 'red':[]}

def define_star_color():
    """
    This is the function to define stars colors depends on their temperatures.
    """
    for star_name, temp in star_temperatures.items():
            if temp >= 25000:
                star_colors['blue'].append(star_name)
            elif 25000 > temp >= 10000:
                star_colors['white'].append(star_name)
            elif 10000 > temp >= 6000:
                star_colors['yellow'].append(star_name)
            elif 6000 > temp >= 4000:
                star_colors['orange'].append(star_name)
            elif 4000 > temp >= 3000:
                star_colors['red'].append(star_name)
    
    return star_colors
        
        

def print_star_color():
    """
    This is the function to print colors value for certain stars.
    """
    for color, star_name in star_colors.items():
        
        if star_name != []:
            star_string =', '.join(star_name)
            print(f"{color}: {star_string}")
            print()
        
define_star_color()        
print_star_color()