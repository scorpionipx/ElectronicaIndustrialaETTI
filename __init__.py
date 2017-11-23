import logging
import os
from time import gmtime, strftime

__version__ = '0.0.1'

try:
    os.mkdir(r'log')
except FileExistsError:
    pass

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M',
    filename=r'log\log {}.txt'.format(strftime("%Y-%m-%d %H-%M-%S", gmtime())),
    filemode='w'
)
CONSOLE = logging.StreamHandler()
CONSOLE.setLevel(logging.DEBUG)
FORMATTER = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
CONSOLE.setFormatter(FORMATTER)
logging.getLogger('').addHandler(CONSOLE)
