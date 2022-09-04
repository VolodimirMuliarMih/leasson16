#leasson 16
import json
tel_dict = {354654:('Petr', 35) , 321654: ('Irina',17) , 556454: ('Oleg',55) , 879654: ('Genadiy', 42)}
tel_dict_json = json.dumps(tel_dict)
with open("lel_dict_json.json", "w") as my_file:
    my_file.write(tel_dict_json)
