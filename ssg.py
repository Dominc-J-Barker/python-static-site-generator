import typer
from ssg.site import Site

def main(source="content", dest="dist"):
    """Build the static site"""

    config = {"source":source, "dest":dest}
    Site(**config).build()

typer.run(main)