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
PLUGIN_PATHS = ['plugins']
PLUGINS = ['gallery']

GALLERY_PATH = 'images/gallery'
DIRECT_TEMPLATES = ['index', 'archives', 'articles']

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLES_SAVE_AS = 'articles/index.html'

DEFAULT_DATE_FORMAT = '%b %d, %Y'