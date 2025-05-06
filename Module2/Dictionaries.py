#collection of items, mutable, not indexable, works on a pair key:value
contact_info = {
    'Alma': '012345678',
    'Erin': "049654321"

}
print(contact_info)
alma_info=contact_info["Alma"]
print(alma_info)
contact_info['Orkidea']='049000123'
contact_info['Orkidea']='0490001233'
contact_info['orkidea']='0490001233'
del contact_info['orkidea']
print(contact_info)
keys=contact_info.keys()
print(keys)
values=contact_info.values()
print(values)
items=contact_info.items()
print(items)#print out the key value pair as a list