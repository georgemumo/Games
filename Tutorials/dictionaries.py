capitals= {'USA':'Washington DC',
           'India':'New Dahli',
           'China':'Beijing',
           'Russia':'San Francisco',
           }
capitals.update( {'Germany':'Berlin'})
capitals.update( {'USA':'Los vegas'})
capitals.pop('China')
# print(capitals['USA'])
print(capitals.get('USA'))
print(capitals.values())
print(capitals.items())
print(capitals.keys())

for key, value in capitals.items():
    print(key, value)