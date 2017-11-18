import json
with open('image-list.json') as json_data:
    d = json.load(json_data)
    for i in range(0,len(d)):
        data_element = d[i]
        try:
            value = data_element["base_id"]
            value = data_element["parent_id"]
            value = data_element["project"]
            value = data_element["service"]
        except KeyError:
            print "Wrong schema!!!"
print "OK!"
