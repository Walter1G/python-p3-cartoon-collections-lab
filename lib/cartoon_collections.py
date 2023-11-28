def roll_call_dwarves(dwarfs):
    for dwarf in dwarfs:
        print(f"{dwarfs.index(dwarf)+1}. {dwarf}")
        
    pass

def summon_captain_planet(planeteer_calls ):
    newList =[f"{call.capitalize()}!" for call in planeteer_calls ]
    return newList
    
    pass

def long_planeteer_calls(calls):
    longCalls=[call for call in calls if len(call)>4]
    if len(longCalls)>0:
        return True
    else:
        return False
    
    pass

def find_the_cheese(strings):
    cheeses=["cheddar", "gouda","camembert"]
    for item in cheeses:
        if item in strings:
            return item
    return None
    pass




roll_call_dwarves(["innie","minnie","mainie"])
print(summon_captain_planet(["innie","minnie","mainie"]))
print(long_planeteer_calls(["innie","minnie","mainie"]))
print(find_the_cheese(["garlic", "rosemary", "bread"]))