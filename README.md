# jinja-website-template
This is a repo to use as a template for creating a new group website

## Dependencies

- [Bootstrap 5.0](https://getbootstrap.com/docs/5.0)
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/templates/)
- [Font Awesome 6](https://fontawesome.com/v6/icons?o=r&m=free)
- [Python 3.12](https://python.org)
- [SASS](https://sass-lang.com/)

## Setting up your local machine

If you're building this on your own machine, we suggest starting with a Python
virtual environment for the project.
You can do this in the repo's root directory with the following:

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

This will set up your entire environment to start rendering the static HTML
pages.

## Building the website

To build the website and view any changes to your local version of the website,
simply run `python build.py` after sourcing the virtual environment.
This will generate your HTML pages in a directory named `build/html`.

> [!Note]
> If you're using vscode, you can install the "Live Server" extension to server
the files as a web server would.

### Building examples

By default, we do not explicit have any HTML files that render.
However, we do provide some examples in the `templates/_examples` directory.
If you would like to see how these examples render, you can either modify the
`build.py` file, or more simply rename the `templates/_examples` directory to
`templates/examples` (notice the removal of the `_`.)

## Custom Style Files

We use SASS to create our CSS files that the site will use to define the style
for the pages.
By default we have two example `.sass` files in our `_sass/_examples` directory
that actually define the style, and a `styles.sass` file that loads these two
other files to create our final `static/css/styles.css` file.
This last file is used in the `base.html` template for defining consistent
styling of the webpages.