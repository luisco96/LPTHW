estados = {
    'Baja California': 'BC',
    'Baja California Sur': 'BCS',
    'Sinaloa': 'SIN',
    'Ciudad de Mexico': 'CDMX'
}

estados['Nuevo Leon'] = 'NL'
estados['Veracruz'] = 'VER'

capitales = {
    'BC': 'Mexicali',
    'BCS': 'La Paz',
    'SIN': 'Culiacan',
    'CDMX': 'DF',
    'NL': 'Monterrey',
    'VER': 'Xalapa'
}

for estado, abbrev in list(estados.items()):
    print(f"La abreviacion de {estado} es {abbrev}")

for estado, abbrev in list(estados.items()):
    print(f"La abreviacion de {estado} es {abbrev} y su capital es {capitales[abbrev]}")