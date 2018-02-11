"""
Confiuguration parameters for NITES
"""
# e.g. .fits or .fit etc
IMAGE_EXTENSION = "*.fts"

# header keyword for the current filter
FILTER_KEYWORD = 'FILTER'

# header keyword for the current target/field
FIELD_KEYWORD = 'OBJECT'

# RA axis alignment along x or y?
RA_AXIS = 'y'

# imager position angle
CAMERA_ANGLE = 0.0

# guider log file name
LOGFILE = "guider.log"

# rejection buffer length
GUIDE_BUFFER_LENGTH = 20

# outlier rejection sigma
SIGMA_BUFFER = 5

# wait time (s)
WAITTIME = 21600

# pulseGuide conversions
PIX2TIME = {'+x': 100.00,
            '-x': 100.00,
            '+y': 100.00,
            '-y': 100.00}

# guide directions
DIRECTIONS = {'+y': 0, '-y': 1, '+x': 2, '-x': 3}

# max allowed shift to correct
MAX_ERROR_PIXELS = 20

# ACP data base directory
BASE_DIR = "C:\\data"

# PID loop coefficients
PID_COEFFS = {'x': {'p': 1.0, 'i': 0.5, 'd': 0.0},
              'y': {'p': 1.0, 'i': 0.5, 'd': 0.0},
              'set_x': 0.0,
              'set_y': 0.0}

# database set up
DB_HOST = "localhost"
DB_USER = "nites"
DB_DATABASE = "nites_ops"
