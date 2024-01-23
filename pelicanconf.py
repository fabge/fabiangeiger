AUTHOR = 'Fabian'
SITENAME = 'fabiangeiger'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False
THEME = 'theme'

STATIC_PATHS = ['photos']
DIRECT_TEMPLATES = ['index', 'articles']

PLUGIN_PATHS = ['plugins']
PLUGINS = ['photos']

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

DEFAULT_DATE_FORMAT = '%b %d, %Y'

DELETE_OUTPUT_DIRECTORY = True
