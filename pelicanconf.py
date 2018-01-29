from __future__ import unicode_literals

LOAD_CONTENT_CACHE = False

SITEURL = ''
# SITEURL = 'http://danielfrg.github.io'
AUTHOR = u'Olamilekan Wahab'
SITENAME = u'Indent'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

MARKUP = ('md', 'ipynb')

DEFAULT_DATE_FORMAT = '%B %d, %Y'

SUMMARY_MAX_LENGTH = 150
DEFAULT_PAGINATION = 10

PAGE_DIRS = ['pages']
ARTICLE_DIRS = ['articles']

THEME = 'theme'
STATIC_PATHS = ['images']

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

RESEARCH_PAGE = "/pages/research.html"

PAGE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = PAGE_SAVE_AS

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'codehilite'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Paths are relative to `content`
STATIC_PATHS = ['images', 'favicon.ico', '404.html', 'robots.txt', 'CNAME']

# THEME SETTINGS
DEFAULT_HEADER_BG = '/images/station1.jpg'
ABOUT_PAGE = '/pages/about.html'
TWITTER_USERNAME = '__olamilekan__'
GITHUB_USERNAME = 'olamyy'
SHOW_ARCHIVES = True
SHOW_FEED = True

GOOGLE_ANALYTICS_CODE = 'UA-35523657-2'
GOOGLE_ANALYTICS_DOMAIN = 'danielfrg.com'

# PLUGINS SETTINGS
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'ipynb.markup', 'ipynb.liquid','liquid_tags.youtube', 'liquid_tags.b64img',
           'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook', 'just_table',
           'better_figures_and_images',
]

SITEMAP = {
    'format': 'xml'
}

IPYNB_EXTEND_STOP_SUMMARY_TAGS = [('h2', None), ('ol', None), ('ul', None)]

NOTEBOOK_DIR = 'notebooks'
 
# EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')
DEFAULT_METADATA = {
    'status': 'draft',
}

IMAGE_PROCESS = {
    'article-image': ["scale_in 300 300 True"],
    'thumb': ["crop 0 0 50% 50%", "scale_out 150 150 True", "crop 0 0 150 150"],
}