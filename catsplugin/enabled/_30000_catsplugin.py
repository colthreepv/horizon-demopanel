# The name of the panel to be added to HORIZON_CONFIG. Required.
PANEL = 'catsplugin'

# The name of the dashboard the PANEL associated with. Required.
PANEL_DASHBOARD = 'identity'

# Python panel class of the PANEL to be added.
ADD_PANEL = 'catsplugin.content.catspanel.panel.CatsPanel'

# A list of applications to be prepended to INSTALLED_APPS
ADD_INSTALLED_APPS = ['catsplugin']

# Automatically discover static resources in installed apps
AUTO_DISCOVER_STATIC_FILES = True

# A list of js files to be included in the compressed set of files
ADD_JS_FILES = []

# A list of template-based views to be added to the header
ADD_HEADER_SECTIONS = ['catsplugin.content.catspanel.views.IndexView']
