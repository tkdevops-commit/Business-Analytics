import os
import json
import warnings
import matplotlib
from IPython.core.display import HTML

"""
def css_styling():
    styles = open("../styles/custom.css", "r").read()
    return HTML(styles)
css_styling()


s = json.load( open("../styles/bmh_matplotlibrc.json") )
matplotlib.rcParams.update(s)
"""

def load_style(directory = ""):
	# recent matplotlibs are raising deprecation warnings that
	# we don't worry about.
	warnings.filterwarnings("ignore")

	# update the default matplotlib's formating
	s = json.load( open( os.path.join( directory, "plot.json" ) ) )
	matplotlib.rcParams.update(s)

	# load the styles for the notebooks
	styles = open( os.path.join( directory, "custom.css" ), "r" ).read()
	return HTML(styles)