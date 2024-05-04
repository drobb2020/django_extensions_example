# Django Extensions

Django extensions are a collection of custom extensions for Django. These extensions enhance the development experience for users coding a django application.

## Installation

*You should have a virtual environment created prior to installing any package*

To install django extensions use pip with the following command:

```sh
    pip install django-extensions
```

Once the package is installed in your environment, you need to add it to your INSTALLED_APPS in settings.py

```sh
    INSTALLED_APPS = [
        ...
        "django_extensions",
        ...
    ]
```

## Full List of Command Extensions

* admin_generator - Generate automatic Django Admin classes by providing an app name. Outputs source code at STDOUT.Generate automatic Django Admin classes by providing an app name. Outputs source code at STDOUT.
* clean_pyc - Removes all python bytecode compiled files from the project.
* clear_cache - Fully clear site-wide cache.
* compile_pyc - Compile python bytecode files for the project.
* create_command - Creates a Django management command directory structure for the given app name in the app's directory.
* create_jobs - Creates a Django jobs command directory structure for the given app name in the current directory.
* create_template_tags - Creates a template tag directory structure within the specified application.
* delete_squashed_migrations - Deletes leftover migrations after squashing and converts squashed migration to a normal one.
* describe_form - Outputs the specified model as a form definition to the shell.
* drop_test_database - Drops test database for this project.
* dumpscript - Generates a standalone Python script that will repopulate the database using objects.
* export_emails - export the email addresses for your users in one of many formats
* find_template - Finds the location of the given template by resolving its path
* generate_password - Generates a new password that can be used for a user password.
* generate_secret_key - Generates a new SECRET_KEY that can be used in a project settings file.
* graph_models - Renders a graphical overview of your project or specified apps.
* list_model_info - Lists out all the fields and methods for models in installed apps.
* list_signals - Lists all signals defined in the project grouped by model and signal type
* mail_debug - Starts a test mail server for development.
* managestate - Saves current applied migrations to a file or applies migrations from this file.
* merge_model_instances - Merges duplicate model instances by reassigning related model references to a chosen primary model instance.
* notes - Show all annotations like TODO, FIXME, BUG, HACK, WARNING, NOTE or XXX in your py and HTML files.
* pipchecker - Scan pip requirement files for out-of-date packages.
* print_settings - Django management command similar to diffsettings but shows selected active Django settings or all if no args passed.
* print_user_for_session - print the user information for the provided session key. this is very helpful when trying to track down the person who experienced a site crash.
* raise_test_exception - Raises a test Exception named DjangoExtensionsTestException. Useful for debugging integration with error reporters like Sentry.
* reset_db - Fully resets your database by running DROP DATABASE and CREATE DATABASE
* reset_schema - Recreates the public schema for this project.
* runjob - Run a single maintenance job.
* runjobs - Runs scheduled maintenance jobs.
* runprofileserver - Starts a lightweight Web server with profiling enabled.
* runscript - Runs a script in the Django context.
* runserver_plus - RunServerPlus-typical runserver with Werkzeug debugger baked in
* set_default_site - Set parameters of the default django.contrib.sites Site
* set_fake_emails - DEBUG only: give all users a new email based on their account data ("%(username)s@example.com" by default). Possible parameters are: username, first_name, last_name
* set_fake_passwords - DEBUG only: sets all user passwords to a common value ("password" by default)
* shell_plus - Django shell with autoloading of the apps database models and subclasses of user-defined classes.
* show_template_tags - Displays template tags and filters available in the current project.
* show_urls - Displays all of the url matching routes for the project.
* sqlcreate - Helps you setup your database(s) more easily
* sqldiff - Prints the ALTER TABLE statements for the given appnames.
* sqldsn - Prints Data Source Name connection string on stdout
* sync_s3 - sync your MEDIA_ROOT and STATIC_ROOT folders to S3
* syncdata - Makes the current database have the same data as the fixture(s), no more, no less.
* unreferenced_files - Prints a list of all files in MEDIA_ROOT that are not referenced in the database.
* update_permissions - reloads permissions for specified apps, or all apps if no args are specified
* validate_templates - Checks templates on syntax or compile errors.

## My Favorite Extensions

* shell_plus
* dumpscript
* export_emails
* generate_password
* Graph models
* reset_db
* runserver_plus
* generate_secret_key
* admin_generator

### shell_plus

* A Django shell with auto-loading of the configured apps database models and subclasses of user-defined classes.
* You can also exclude models by adding the --dont-load app1 to the command line.
* Has a built-in collision resolver.

### dumpscript

* Generates a standalone python script that can be used to repopulate the database using objects.
* Save crucial data when you modify your models.
* Edit the script to create 1000's of entries using for loops, and generated names.

### export_emails

* Exports the email addresses of registered users in the format you specify.
* formats are:
  * address
  * google
  * outlook
  * linkedin
  * vcard
* You can use the generated list for a mailer to all your users.

### generate_password

* Generates a new password that you can then use for a user password.
* Uses the default django password generator.
* You are able to specify the length of the password by adding the --length=XX switch.

### Graph models

* Renders a graphical representation of your entire project or of a specific application.
* You need Graphvis installed on the OS, as well as pygraphviz for this to work.
* Use the GRAPH_MODELS option in settings.py to specify default options.

### reset_db

* Fully resets your current database by running a DROP DATABASE followed by a CREATE DATABASE
* This is a destructive operation!
* You will be prompted to confirm the operation.

### runserver_plus

* This is the typical runserver command with the Werkzeug debugger baked in.
* Requires the Werkzeug package to be installed (Kick ass debugger).
* Allows you to run your development server over https by specifying the --cert-file option.

### generate_secret_key

* Creates a new secret key that you can put in your settings.py module, or more appropriately place it in a dot env file.

### admin_generator

* Generates the class based admin registration code for a give app.
* The admin_generator reads the necessary models.py file and generates the code for you.
* The results are displayed on STDOUT (command prompt).
* The only downside is that it adds all fields to the registration, in the order that they are found. I typically remove "id", from the list.
