import os

BASE_DIR = os.path.dirname(__file__)

COMPONENTS = {
    'button': os.path.join(BASE_DIR, 'components', 'button.j2'),
    'input': os.path.join(BASE_DIR, 'components', 'input.j2'),
    'select': os.path.join(BASE_DIR, 'components', 'select.j2')
    # add more components here
}