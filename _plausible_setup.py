"""Sphinx extension to add Plausible analytics to Jupyter Book."""


def setup(app):
    """Add Plausible analytics scripts to the site."""
    # Add the external Plausible script for jupyter.org
    app.add_js_file(
        "https://plausible.io/js/pa-B75UO5--FNXYQSG7GBWkf.js",
        loading_method="async"
    )

    # Add the inline initialization script
    plausible_init = """
  window.plausible=window.plausible||function(){(plausible.q=plausible.q||[]).push(arguments)},plausible.init=plausible.init||function(i){plausible.o=i||{}};
  plausible.init({hashBasedRouting:true})
"""
    app.add_js_file(None, body=plausible_init)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
