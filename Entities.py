
# @author: Antriksh Agarwal
# Version 0: 4/13/2018

# Named Entities:
# 	geo = Geographical Entity
# 	org = Organization
# 	per = Person
# 	gpe = Geopolitical Entity
# 	tim = Time indicator
# 	art = Artifact
# 	eve = Event
# 	nat = Natural Phenomenon

entities = dict({'O': 0, 'geo': 1, 'org': 2, 'per': 3,
                 'gpe': 4, 'tim': 5, 'art': 6, 'eve': 7, 'nat': 8})


def getEntity(label):
    for entity in entities.keys():
        if entity in label:
            return entities[entity]

    return 0
