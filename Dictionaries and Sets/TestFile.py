instruments = {'drums': {'color':'black', 'sound':'boom'},
               'guitar': {'color':'blue', 'sound':'wahhh'}}
#print('Original', instruments)
for instrument, properties in instruments.items():
    print('Instrument: ', instrument)
    for property in properties:
        print(property + ":", properties[property])