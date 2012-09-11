# Some of the modules (filenames) are not compatible with Python 2.5, but we
# don't want to prevent you from using all of them because of it.

import_errors = []

try:
    from actions import *
except ImportError:
    import_errors.append('actions')

if import_errors:
    import logging
    logger = logging.getLogger('admintools')
    logger.warning('There were errors importing the following admintools'
         ' modules: %s. They will not be available. To see the errors, import'
         ' the modules directly.')
