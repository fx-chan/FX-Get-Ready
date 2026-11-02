"""WSGI entry point for PythonAnywhere.

In the PythonAnywhere "Web" tab, point the WSGI configuration file at this
module, e.g.:

    import sys
    sys.path.insert(0, "/home/<user>/Prep_web_proj")
    from wsgi import application
"""
from prep import create_app

application = create_app()
