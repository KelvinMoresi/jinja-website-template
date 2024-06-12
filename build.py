import datetime
import logging
import pathlib
import sass
import staticjinja

staticjinja.logger.setLevel(logging.DEBUG)


def compile_sass():
    # compile our sass into a single css file first
    css_path = pathlib.Path("static/css")
    css_path.mkdir(parents=True, exist_ok=True)
    sass_output = sass.compile(
        filename="_sass/styles.sass",
        include_paths="_sass",
        output_style="nested",
    )
    with open(f"{css_path}/styles.css", "w") as css_file:
        css_file.writelines(sass_output)


def render_site():
    # setup the jinja site with ability to update from changes
    site = staticjinja.Site.make_site(
        outpath="build/html",
        searchpath="templates",
        env_globals={
            "time": datetime.datetime.now(),
        }
    )
    site.render(use_reloader=True)  # enable automatic reloading


def main():
    compile_sass()
    render_site()


main()
