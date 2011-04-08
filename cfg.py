import sys
import materials
import ConfigParser

from utils import *

parser = ConfigParser.SafeConfigParser()

offset = ''
min_dist = 1
max_dist = 16
tower = 1.0
doors = 50
portcullises = 50
torches_top = 50
torches_bottom = 50
wall = 'Cobblestone'
floor = 'Stone'
ceiling = 'Cobblestone'
mvportal = ''
chests = 1
spawners = 2
arrow_traps = 5
loops = 0

master_halls = {}
master_rooms = {}
master_features = {}
master_floors = {}
master_mobs = []

def Load(filename = 'mcdungeon.cfg'):
    global parser, offset, tower, doors, portcullises, torches_top, wall, \
    floor, ceiling, mvportal, master_halls, master_rooms, master_features, \
    master_floors, chests, spawners, master_mobs, torches_bottom, min_dist, \
    max_dist, arrow_traps, loops

    print 'Reading config from', filename, '...'
    try:
        parser.readfp(open(filename))
    except:
        print "Failed to read config file:", filename
        sys.exit(1)

    # Load master tables from .cfg.
    master_halls = parser.items('halls')
    master_rooms = parser.items('rooms')
    master_features = parser.items('features')
    master_floors = parser.items('floors')
    temp_mobs = parser.items('mobs')

    # Fix the mob names...
    for mob in temp_mobs:
        mob2 = mob[0].capitalize()
        if (mob2 == 'Pigzombie'):
            mob2 = 'PigZombie'
        master_mobs.append((mob2, mob[1]))

    # Load other config options
    offset = parser.get('dungeon', 'offset')
    tower = parser.getfloat('dungeon','tower')
    doors = parser.getint('dungeon','doors')
    portcullises = parser.getint('dungeon', 'portcullises')
    torches_top = parser.getint('dungeon', 'torches_top')
    torches_bottom = parser.getint('dungeon', 'torches_bottom')
    wall = parser.get('dungeon', 'wall').lower()
    ceiling = parser.get('dungeon', 'ceiling').lower()
    floor = parser.get('dungeon', 'floor').lower()
    subfloor = parser.get('dungeon', 'subfloor').lower()
    mvportal = parser.get('dungeon', 'mvportal')
    chests = parser.getfloat('dungeon', 'chests')
    spawners = parser.getfloat('dungeon', 'spawners')
    min_dist = parser.getint('dungeon', 'min_dist')
    max_dist = parser.getint('dungeon', 'max_dist')
    arrow_traps = parser.getint('dungeon', 'arrow_traps')
    loops = parser.getint('dungeon', 'loops')

    if (tower < 1.0):
        sys.exit('The tower height parameter is too small. This should be \
                 >= 1.0. Check the cfg file.')

    if (chests < 0.0 or chests > 10.0):
        sys.exit('Chests should be between 0 and 10. Check the cfg file.')

    if (spawners < 0.0 or spawners > 10.0):
        sys.ext('Spawners should be between 0 and 10. Check the cfg file.')

    # Set the wall, ceiling, and floor materials
    for name, val in materials.__dict__.items():
        if type(val) == materials.Material:
            if (val.name == wall):
                materials._wall = copy(val)
            if (val.name == ceiling):
                materials._ceiling = copy(val)
            if (val.name == floor):
                materials._floor = copy(val)
            if (val.name == subfloor):
                materials._floor = copy(val)
