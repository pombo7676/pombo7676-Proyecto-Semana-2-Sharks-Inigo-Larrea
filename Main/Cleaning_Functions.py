# Function to clean the Species Column by selecting strings present in the names and assigning them to an Specific and clean name for each shark species, and once all most common are assigned the rest will be assigned as "Unknown Shark"

def clean_species(x):
    
    if 'white' in x.lower():
        return 'White Shark'
    
    elif 'bull' in x.lower():
        return 'Bull Shark'
    
    elif 'tiger' in x.lower():
        return 'Tiger Shark'     
    
    elif 'nurse' in x.lower():
        return 'Nurse Shark'
    
    elif 'blacktip' in x.lower():
        return 'Blacktip Shark'
    
    elif 'blue' in x.lower():
        return 'Blue Shark'
    
    elif 'mako' in x.lower():
        return 'Mako Shark'
    
    elif 'hammerhead' in x.lower():
        return 'Hammerhead Shark'
    
    elif 'wobbegong' in x.lower():
        return 'Wobbegong Shark'
    
    elif 'raggedtooth' in x.lower():
        return 'Raggedtooth Shark'
    
    elif 'lemon' in x.lower():
        return 'Lemon Shark'
    
    elif 'zambesi' in x.lower():
        return 'Zambesi Shark'
    
    elif 'spinner' in x.lower():
        return 'Spinner Shark'
    
    elif 'blue' in x.lower():
        return 'Blue Shark'
    
    elif 'grey reef' in x.lower():
        return 'Grey Reef Shark'
    
    elif 'bonita' in x.lower():
        return 'Bonita Shark'
    
    elif 'basking' in x.lower():
        return 'Basking Shark'
    
    else:
        return 'Unknown Shark'
    
    
# Function to clean the Ages Column by selecting strings present in the names and assigning an Specific age by cleaning the string.

def clean_age(x):
    
    if ',' in x:
        x = x.split(' , ')
        return  x[0]
    
    elif '&' in x:
        x = x.split(' & ')
        return x[1]
    
    elif 'or' in x:
        x = x.split(' or ')
        return x[0]
    
    elif 'months' in x:
        return 1
      
    elif 'teen' in x.lower():
        return 15
    
    elif 'young' in x.lower():
        return 25
    
    elif 'adult' in x.lower():
        return 35
    
    elif 'middle-age' in x:
        return 50
    
    elif 'elderly' in x.lower():
        return 70
    
    else:    
        return x
          
def clean_activity(x):
    
    if 'pad' in x.lower():
        return  'Paddle Surfing'
    
    elif 'kite' in x.lower():
        return 'Kite Surfing'
    
    elif 'surf' in x.lower():
        return 'Surfing'
        
    elif 'swim' in x.lower():
        return 'Swimming'
    
    elif 'bath' in x.lower():
        return 'Bathing'
    
    elif 'scu' in x.lower():
        return 'Scubba Diving'
    
    elif 'div' in x.lower():
        return 'Diving'
    
    elif 'kay' in x.lower():
        return 'Kayaking'
    
    elif 'fish' in x.lower():
        return 'Fishing'
    
    elif 'boat' in x.lower():
        return 'Boating'
    
    
    
    else:    
        return x    

    
    
        
        
    
    




