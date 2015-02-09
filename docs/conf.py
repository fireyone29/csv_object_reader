# -*- coding: utf-8 -*-
import sys
import pkg_resources

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary'
]

source_suffix = '.rst'

master_doc = 'index'

project = u'csv_object_reader'
copyright = u'2015, fireyone29'

try:
    release = pkg_resources.get_distribution('csv_object_reader').version
except pkg_resources.DistributionNotFound:
    print 'To build the documentation, The distribution information of'
    print 'csv_object_reader has to be available.  Either install the package'
    print 'into your development environment or run "setup.py develop" to'
    print 'setup the metadata.  A virtualenv is recommended!'
    sys.exit(1)
del pkg_resources
version = '.'.join(release.split('.')[:2])

autoclass_content = 'both'
pygments_style = 'sphinx'
html_theme = 'default'
html_theme_options = {
    "sidebarwidth": 300
}
htmlhelp_basename = 'csv_object_readerdoc'

latex_elements = {}
latex_documents = [
  ('index', 'csv_object_reader.tex', u'csv\\_object\\_reader Documentation',
   u'fireyone29', 'manual'),
]
man_pages = [
    ('index', 'csv_object_reader', u'csv_object_reader Documentation',
     [u'fireyone29'], 1)
]
texinfo_documents = [
  ('index', 'csv_object_reader', u'csv_object_reader Documentation',
   u'fireyone29', 'csv_object_reader', 'One line description of project.',
   'Miscellaneous'),
]
