Version 0.5.6 - 2013-09-04
--------------------------
- Added `multiple_checkbox_field` macro for `wtf.SelectMultipleField`
- Brought back the `spinner-icon` div in the NProgress lib

Version 0.5.5 - 2013-09-01
--------------------------
- Added `sitemap.xml`
- Added `/signin/*/` in `robots.txt`
- Added `util.slugify` function into Jinja2 templates
- For the welcome logo the slugified name of the brand is used
- No more custom brand names and logos in forks, to avoid conflicts

Version 0.5.4 - 2013-08-30
--------------------------
- Introduced `util.jsonpify()`, which is like flask.jsonify but returns JSONP if callback is provided
- All the services now support a `callback` argument to get JSONP
- Updated `run.py` script so the `--clean` argument is obsolete when `--start` is used

Version 0.5.3 - 2013-08-28
--------------------------
- Error checkings in the `auth` functions
- Added 405 error
- Minor reformats and few comments

Version 0.5.2 - 2013-08-27
--------------------------
- Added a nanoscopic progress bar: NProgress
- Removed empty `<p>` in footer
- Third party libs are decleared in `appengine_config.py`

Version 0.5.1 - 2013-08-23
--------------------------
- Refactored `auth.py`
- Updated Twitter's links
- Added announcement message in the admin config

Version 0.5.0 - 2013-08-20
--------------------------
- Boostrap 3 is in da house! Strongly recommended to read the docs
- All of the templates are affected
- `top_bar.html` renamed to `header.html`
- `base.html` is much simpler
- `footer` is using centered align
- Jinja2 macros are used for the form controls instead of `field_*_input.html`
- Added `# -*- coding: utf-8 -*-` to every source file
- HTML5 elements `<header>`, `<nav>`, `<footer>`
- The `build.py` script renamed to `run.py`
- Dev server starts with `-s` or `--start` instead of `-r` argument in the `run.py`
- Bunch of small changes
- Merge at your own risk!
