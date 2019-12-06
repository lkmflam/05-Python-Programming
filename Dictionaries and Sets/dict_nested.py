# Multi Dimensional Dictionary

# Intitialize instrument dictionary
instruments = {'drums': {'color':'black', 'sound':'boom'},
               'guitar': {'color':'blue', 'sound':'wahhh'}}
print('Original', instruments)

# Add something to the nested dictionary
instruments.update({'violin':{'color':'brown', 'sound':'whineeee'}})
print('After updating', instruments)

# More ways to add instruments
instruments['bass'] = {'color':'purple', 'sound':'slappadabass'}
print('AFter adding bass', instruments)

# Access items/nested items within our dictionary
print('guitar', instruments['guitar'])
print('guitar sound', instruments['guitar']['sound'])

# Iterate through nested dictionary
for instrument, properties in instruments.items():
    print('Instrument: ', instrument)
    for property in properties:
        print(property + ":", properties[property])
