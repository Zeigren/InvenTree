InvenTree Development
===================

.. toctree::
   :titlesonly:
   :maxdepth: 2
   :caption: Development
   :hidden:

Development and Testing
-----------------------

Shorthand functions are provided for the development and testing process:

* ``make install`` - Install all required underlying packages using PIP
* ``make update`` - Update InvenTree installation (after database configuration)
* ``make superuser`` - Create a superuser account
* ``make migrate`` - Perform database migrations
* ``make mysql`` - Install packages required for MySQL database backend
* ``make postgresql`` - Install packages required for PostgreSQL database backend
* ``make translate`` - Compile language translation files (requires gettext system package)
* ``make backup`` - Backup database tables and media files
* ``make test`` - Run all unit tests
* ``make coverage`` - Run all unit tests and generate code coverage report
* ``make style`` - Check Python codebase against PEP coding standards (using Flake)
* ``make docreqs`` - Install the packages required to generate documentation
* ``make docs`` - Generate this documentation

Dependency Documentation
-----------------------

Documentation/Project links for packages found in ``requirements.txt``:

`coreapi <https://github.com/core-api/python-client>`_
`coverage <https://github.com/nedbat/coveragepy>`_
`Django <https://docs.djangoproject.com/>`_
`django-cleanup <https://github.com/un1t/django-cleanup>`_
`django-cors-headers <https://github.com/adamchainz/django-cors-headers/>`_
`django-crispy-forms <https://github.com/django-crispy-forms/django-crispy-forms>`_
`django-dbbackup <https://github.com/django-dbbackup/django-dbbackup>`_
`django-guardian <https://github.com/django-guardian/django-guardian>`_
`django-import-export <https://github.com/django-import-export/django-import-export>`_
`django-mptt <https://github.com/django-mptt/django-mptt>`_
`django-qr-code <https://github.com/dprog-philippe-docourt/django-qr-code>`_
`django_filter <https://github.com/carltongibson/django-filter>`_
`djangorestframework <https://www.django-rest-framework.org/>`_
`djangorestframework-guardian <https://github.com/rpkilby/django-rest-framework-guardian>`_
`flake8 <https://gitlab.com/pycqa/flake8>`_
`fuzzywuzzy <https://github.com/seatgeek/fuzzywuzzy>`_
`pillow <https://pillow.readthedocs.io/en/stable/>`_
`pygments <https://pygments.org/>`_
`python-coveralls <https://github.com/z4r/python-coveralls>`_
`python-Levenshtein <https://github.com/ztane/python-Levenshtein>`_
`tablib <https://tablib.readthedocs.io/en/stable/>`_

Permissions List
-----------------------

python manage.py get_all_permissions

admin.add_logentry
admin.change_logentry
admin.delete_logentry
admin.view_logentry
auth.add_group
auth.add_permission
auth.add_user
auth.change_group
auth.change_permission
auth.change_user
auth.delete_group
auth.delete_permission
auth.delete_user
auth.view_group
auth.view_permission
auth.view_user
authtoken.add_token
authtoken.change_token
authtoken.delete_token
authtoken.view_token
build.add_build
build.add_builditem
build.change_build
build.change_builditem
build.delete_build
build.delete_builditem
build.view_build
build.view_builditem
common.add_currency
common.add_inventreesetting
common.change_currency
common.change_inventreesetting
common.delete_currency
common.delete_inventreesetting
common.view_currency
common.view_inventreesetting
company.add_company
company.add_contact
company.add_supplierpart
company.add_supplierpricebreak
company.change_company
company.change_contact
company.change_supplierpart
company.change_supplierpricebreak
company.delete_company
company.delete_contact
company.delete_supplierpart
company.delete_supplierpricebreak
company.view_company
company.view_contact
company.view_supplierpart
company.view_supplierpricebreak
contenttypes.add_contenttype
contenttypes.change_contenttype
contenttypes.delete_contenttype
contenttypes.view_contenttype
guardian.add_groupobjectpermission
guardian.add_userobjectpermission
guardian.change_groupobjectpermission
guardian.change_userobjectpermission
guardian.delete_groupobjectpermission
guardian.delete_userobjectpermission
guardian.view_groupobjectpermission
guardian.view_userobjectpermission
order.add_purchaseorder
order.add_purchaseorderlineitem
order.change_purchaseorder
order.change_purchaseorderlineitem
order.delete_purchaseorder
order.delete_purchaseorderlineitem
order.view_purchaseorder
order.view_purchaseorderlineitem
part.add_bomitem
part.add_part
part.add_partattachment
part.add_partcategory
part.add_partparameter
part.add_partparametertemplate
part.add_partstar
part.change_bomitem
part.change_part
part.change_partattachment
part.change_partcategory
part.change_partparameter
part.change_partparametertemplate
part.change_partstar
part.delete_bomitem
part.delete_part
part.delete_partattachment
part.delete_partcategory
part.delete_partparameter
part.delete_partparametertemplate
part.delete_partstar
part.view_bomitem
part.view_part
part.view_partattachment
part.view_partcategory
part.view_partparameter
part.view_partparametertemplate
part.view_partstar
sessions.add_session
sessions.change_session
sessions.delete_session
sessions.view_session
stock.add_stockitem
stock.add_stockitemtracking
stock.add_stocklocation
stock.change_stockitem
stock.change_stockitemtracking
stock.change_stocklocation
stock.delete_stockitem
stock.delete_stockitemtracking
stock.delete_stocklocation
stock.view_stockitem
stock.view_stockitemtracking
stock.view_stocklocation

