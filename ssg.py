#!/usr/bin/env python
"""Static Site Generator."""

import typer
from ssg.site import Site
import ssg.parsers

def main(source="content", dest="dist"):
    """Build the static site"""

    config = {"source":source, "dest":dest, "parsers":[ssg.parsers.ResourceParser()]}

    Site(**config).build()

typer.run(main)