def namelist(names):
    if len(names)==0: 
        return ""
    elif len(names)==1: 
        return names[0]['name']
    else:
        return ", ".join([item['name'] for item in names[:-1]]) + " & " + names[-1]['name']