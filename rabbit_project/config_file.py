from configparser import ConfigParser
_config = ConfigParser()
_config.read('./config.ini')  # Handles everything as a dictionary

# RABBITS
def r_dying_age():
    return _config['DEFAULT']['rabbit_dying_age']

def r_death_chance():
    return _config['DEFAULT']['rabbit_death_chance']

def r_starting_age():
    return _config['DEFAULT']['age_of_starting_rabbits']

def r_starting_males():
    return _config['DEFAULT']['rabbits_num_starting_males']

def r_starting_females():
    return _config['DEFAULT']['rabbits_num_starting_females']

def r_pregnancy_chance():
    return _config['DEFAULT']['rabbit_chance_of_pregnancy']

def r_babies_min():
    return _config['DEFAULT']['rabbit_num_babies_min']

def r_babies_max():
    return _config['DEFAULT']['rabbit_num_babies_max']


# HAWKS
def h_starting_age():
    return _config['DEFAULT']['age_of_starting_hawks']

def h_starting_males():
    return _config['DEFAULT']['hawks_num_starting_males']

def h_starting_females():
    return _config['DEFAULT']['hawks_num_starting_females']

def h_months_introduced():
    return _config['DEFAULT']['months_hawks_introduced']

def h_pregnancy_chance():
    return _config['DEFAULT']['hawks_chance_of_pregnancy']

def h_babies_min():
    return _config['DEFAULT']['hawks_num_babies_min']

def h_babies_max():
    return _config['DEFAULT']['hawks_num_babies_max']

def h_rabbits_eaten():
    return _config['DEFAULT']['num_rabbits_eaten_each_month']