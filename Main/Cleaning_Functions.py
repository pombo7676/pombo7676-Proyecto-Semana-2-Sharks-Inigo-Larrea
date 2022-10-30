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
    
    
# Function to clean the Species Column by selecting strings present in the names and assigning them to an Specific and clean name for each shark species, and once all most common are assigned the rest will be assigned as "Unknown Shark"


