"""
4 - To uses as 'Internalization(i18n)' or 'Localization(l10n)' functions.

It is just convention, does not have any syntactic functions. That is, the
underscore does not means i18n/l10n, and it is just a convention that binds
the i18n/l10n to underscore variable has been from C convention.

The built-in library gettext which is for i18n/l10n uses this convention,
and Django which is Python web framework supports i18n/l10n also introduces
and uses this convention.

https://docs.python.org/3/library/gettext.html
"""

import gettext
gettext.bindtextdomain('myapplication', '/path/to/my/language/directory')
gettext.textdomain('myapplication')
_ = gettext.gettext
# ...
print(_('This is a translatable string.'))
