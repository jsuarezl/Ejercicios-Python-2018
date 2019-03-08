def conteo():
    dict_list = [
        {
            'nombre': 'Francisca',
            'edad': 25,
            'comuna': 'Providencia'
        },
        {
            'nombre': 'Juanito',
            'edad': 26,
            'comuna': 'Las Condes'
        },
        {
            'nombre': 'Anita',
            'edad': 25,
            'comuna': 'Providencia'
        },
        {
            'nombre': 'Pedro',
            'edad': 24,
            'comuna': 'La Florida'
        },
        {
            'nombre': 'Camila',
            'edad': 27,
            'comuna': 'Ñuñoa'
        }
    ]
    coincidences = 0
    counted = []
    for ent in dict_list:
        for ent2 in dict_list:
            if ent['edad'] == ent2['edad'] and ent['comuna'] == ent2['comuna'] and ent['nombre'] != ent2['nombre']:
                if ent['nombre'] in counted:
                    continue
                counted.append(ent['nombre'])
                coincidences += 1
    print("Cantidad de personas que coinciden con su edad y comuna con al menos una persona: ", coincidences)
