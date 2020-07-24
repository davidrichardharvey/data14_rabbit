from configparser import ConfigParser
_config = ConfigParser()
_config.read('./config.ini')  # Handles everything as a dictionary

def r_dying_age():
    return _config['DEFAULT']['rabbit_dying_age']


def r_death_chance():
    return _config['DEFAULT']['rabbit_death_chance']


def r_starting_age():
    return _config['DEFAULT']['age_of_starting_rabbits']


def r_starting_males():
    return _config['DEFAULT']['number_of_starting_male_rabbits']


def r_starting_females():
    return _config['DEFAULT']['number_of_starting_female_rabbits']


def r_pregnancy_chance():
    return _config['DEFAULT']['rabbit_chance_of_pregnancy']


def r_babies_min():
    return _config['DEFAULT']['rabbit_num_babies_min']


def r_babies_max():
    return _config['DEFAULT']['rabbit_num_babies_max']

