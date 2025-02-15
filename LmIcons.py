### Livebox Monitor icons module ###

import base64

from PyQt6 import QtGui


# ############# Icons #############

class LmIcon:

	TickPixmap = None
	TickData = '''
		iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAxlBMVEUAAAAAAAAAqhUAXQJU32UA
		oBIAlA8AhwwPyx8XyygjwDYAmhEAjQ4AXQIAqhUApRQAfQoASgIAqhUAqBQAbQYADgEAAAAAqRUA
		AABP2mAIkhIHkhBGz1dO1l8R0SIR2SIRyCI9xU7n5+fj4+MRviIRtSLe3t5d5W5c5G3X19c3v0gS
		niMRriJP12BBylIxukInsDgbqSwRsiIRqiIRpyIRoiL////4+Pjr6+ui16me4qcww0EttT4rszwg
		xjEcpC0XrygSoiOQ/0eIAAAAHHRSTlMAGczM+8zMzPn83czMvLq6uoNzc3MzEgwJ+d3dEPRlegAA
		AKNJREFUGNNlyNcSwVAUQNEgiPSe4IpUpHe9/v9POTcyZoz1tjfxz5D5YY+XDRgKTW7BDpC0AkMg
		V19zAcaYRB9RhtIxHqnTyfdnB+HBoOga5cXD89y4YGBM0O1QvuINdFtO8MhO4bGBbuv6iQd7ScIQ
		ugkAC2N69xPoxMemeMxsu3Iru4OHOLMsK7A6lAhDXVDrHrVUCULXJG7U4yRNJ8zBD/MNwiEWhSUh
		NaMAAAAASUVORK5CYII='''

	CrossPixmap = None
	CrossData = '''
		iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJ
		bWFnZVJlYWR5ccllPAAAAe5JREFUeNqkk89KG1EUxr+ZubnUjJaipgtNtTZKxE1AVIi4yM5tF30H
		oe/iA3TnQkTBRbZFKApCAl1142CJqLR0ZUNJJpPJZP70nJvcEK0SpAPfzD3n5vedM2dujCRJ8D+X
		ODIMGMA4aYfibdLkCKZO+kxlP5FcwRla7MytrHxcLhazMp2WT5HcbeB5gVOp5H44Dqd2RdTb217a
		2Mi6vi/h+6O6lu9WV7M3jsPd7ppsQJqMTVO6rgtWdn8fev1YrpskkhlmzZBuLJ8qN5tNLJfLqgw/
		OX4sxyaaE2G/L8/z0Gq1cLy4iA+1mjKcOzhQ+RrFpmniy9oaUqkUMpkMNDcwCIIAYRhiwraxNz2N
		wskJLMtSgJQSZwSr6Xa7aDca/xowHFB7Xr0OO47vwazx4W9PJpozu2xK6hCY3N1hLIqQPz29Bwsh
		ULq8RJp+x5JUTHODIRpkkKbv/GYI/ra+jq+FgjJgbV5dKYMX1KHmBh1ImgFv3pZKCr4geJZiVjWf
		V+2e53K9LqiQ5kSnfzwjmuIY+cxT8J3g+aF35nWVYJ1rx3HQ6R1pWNd0ewu8bkdRfkYI2zYMi/8M
		4oF0juGq7//8FUWHh0DF4L2XwMIW8H4KKFL8asRR/vObwHOg3ACu2YA6x0S/wHMunmHzrwADAPb0
		7huzEp/RAAAAAElFTkSuQmCC'''

	DenyPixmap = None
	DenyData = '''
		iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAzFBMVEUAAAAAAACqAABdAADlXFzq
		YWGgAACUAACLAAAAAADLDw/vYmLGKSmTBweaAACEAABdAACqAAClAAB9AABKAACqAACoAABtAAAO
		AACpAAAAAADLFhaZMzP////48fHcuLjZERH1bGz/dnbhwcHChISrVlaeNjacMjLSExOyQ0PIERH2
		7e37c3PdX1+wQUHMQECnNTW/Ly+oKyvBISHQHx+9GhrAFRX5cXHtZWXZXFzhWVnNUFDDTU3bTEzC
		MTHRMDChLS2zKiq7JSWzHR3L21+eAAAAHHRSTlMAGszM/v3MzMwU+fnd3czMvLq6uoNzc3MzDAn5
		AP8ibQAAALhJREFUGNNlyEcSgjAUAFDUoIK90QzBSO8de7//ncyfYeGMb/m4f+pm0W0tNioLaTyi
		exDR0VhiseTRIfYdx48pQksWfZ5GvkWIaV951Iegp4RiQ9dD+3KGmNLEwgjGzNIpi8HRIQZO2RA3
		H0DwDtENfMcGcd8Qw1tm6mxKbD3rIcQjt0OYBn8aiFlVvWyTEAsHQTBjsdp6Xlm4blF7nrhiIU/E
		XUucyBwnKOt5rzVfKwKnCZ0fgvYFaUkWa6ms/VgAAAAASUVORK5CYII='''

	NotifPixmap = None
	NotifData = '''
		iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAArlBMVEUAAAAAAADLsgGWgAC1nQG8
		pAHDqgHMswHj0yL68p7g0EqVfwCslQDLsgHMswF3ZQCfiAAXEwAAAADMswEAAADj1S747ZK6pxC6
		pg3q3Cb76oHZ1Dfe1jLj2S3/9qj35nnz4nAAAADV0TzQz0D16YXw32n68Zz47ZDt6oH07Xp1dXVm
		Zmbq22HUzEjSyUXp4Wjt3WTe2GPl2VbV1FDa1E3k3EvX1Ebn3T4wMDAYGBhq6pIiAAAAGXRSTlMA
		GazMurWyYPj1x7utnZyDbzMSCgn39dnZsf32zgAAAJhJREFUGNNlyNcOgkAQQFFEYendgoA6C0jH
		3v7/x5wxGxPjebgPV/oXMkcWHBbiYIa+EXSD4bD19dfCxiHvt6htqZX8GTvUddSChlqVZdk/X8M4
		DieVRnHsrzlAji40lOLMOQfg6K7QOCSorhNCY3ZLEUBKZjQeGQLICA1rHqOmoWoWDm+pxYK28iQp
		8F1zKpiuH0jR5Ef0Bky6E46+fts4AAAAAElFTkSuQmCC'''

	WifiSignal0Pixmap = None
	WifiSignal0Data = '''
		iVBORw0KGgoAAAANSUhEUgAAACUAAAAPAgMAAAAex+7AAAAADFBMVEUAAADf39/ZERHa2tphOsv0
		AAAAAXRSTlMAQObYZgAAAFBJREFUCNdjgIFQBwwm0wKmpTDm6lNw5qpXMCbDqlVTIcz/B16tgmq7
		euDWChgTLAqWvnoApBYsdvUQ0AQYcyXQXKA0iLn0EJAJZIBhKDITAMjJOrW9TNAYAAAAAElFTkSu
		QmCC'''

	WifiSignal1Pixmap = None
	WifiSignal1Data = '''
		iVBORw0KGgoAAAANSUhEUgAAACUAAAAPBAMAAACRhxtgAAAAD1BMVEUAAADf39/a2traMiHlMiRE
		TMbOAAAAAXRSTlMAQObYZgAAADRJREFUGNNjQAdKSgoYYoqCeMQQ+tDFgHz8Ygh9EIxQg18MoQ+O
		oWoIixkbG2CImbgQJQYAZsMPo/Tq1Q8AAAAASUVORK5CYII='''

	WifiSignal2Pixmap = None
	WifiSignal2Data = '''
		iVBORw0KGgoAAAANSUhEUgAAACUAAAAPBAMAAACRhxtgAAAAD1BMVEUAAADf39/a2trZcB/gcCw6
		QFeFAAAAAXRSTlMAQObYZgAAADRJREFUGNNjQAdKSgoYYoqCeMQQ+tDFgHz8Ygh9EIxQQ1jM2NgA
		Q8zEhaAYSB+6GJBPlBgA18sRg3n5NH0AAAAASUVORK5CYII='''

	WifiSignal3Pixmap = None
	WifiSignal3Data = '''
		iVBORw0KGgoAAAANSUhEUgAAACUAAAAPBAMAAACRhxtgAAAAD1BMVEUAAADf39/a2tr23k721T3R
		dx7KAAAAAXRSTlMAQObYZgAAADRJREFUGNNjQAdKSgoYYoqCeMQQ+tDFgHzCYi4uDhhizsZ4xWD6
		0MWAfIJiIH3oYhA+YTEAR8oVzR2vvj8AAAAASUVORK5CYII='''

	WifiSignal4Pixmap = None
	WifiSignal4Data = '''
		iVBORw0KGgoAAAANSUhEUgAAACUAAAAPBAMAAACRhxtgAAAAD1BMVEUAAAC35Uip30nf39/a2trZ
		6zb+AAAAAXRSTlMAQObYZgAAADRJREFUGNNjQAcuLg4YYs7GhMWUlBQwxBQF8Ygh9KGLAfl4xWD6
		0MWAbIJiCH0IMSBNlBgAiOsUoXoH5kYAAAAASUVORK5CYII='''

	WifiSignal5Pixmap = None
	WifiSignal5Data = '''
		iVBORw0KGgoAAAANSUhEUgAAACUAAAAPAgMAAAAex+7AAAAACVBMVEUAAACC7kl36DUwSfEIAAAA
		AXRSTlMAQObYZgAAACxJREFUCNdjgIFVDXDmVGQmXBrOnIrKhErDmVPRmWBpOHMqJhMoDWdOxcYE
		AGqZMRs0hralAAAAAElFTkSuQmCC'''


	### Load all icons from base64 data
	@staticmethod
	def load():
		LmIcon.TickPixmap = QtGui.QPixmap()
		LmIcon.TickPixmap.loadFromData(base64.b64decode(LmIcon.TickData))

		LmIcon.CrossPixmap = QtGui.QPixmap()
		LmIcon.CrossPixmap.loadFromData(base64.b64decode(LmIcon.CrossData))

		LmIcon.DenyPixmap = QtGui.QPixmap()
		LmIcon.DenyPixmap.loadFromData(base64.b64decode(LmIcon.DenyData))

		LmIcon.NotifPixmap = QtGui.QPixmap()
		LmIcon.NotifPixmap.loadFromData(base64.b64decode(LmIcon.NotifData))

		LmIcon.WifiSignal0Pixmap = QtGui.QPixmap()
		LmIcon.WifiSignal0Pixmap.loadFromData(base64.b64decode(LmIcon.WifiSignal0Data))

		LmIcon.WifiSignal1Pixmap = QtGui.QPixmap()
		LmIcon.WifiSignal1Pixmap.loadFromData(base64.b64decode(LmIcon.WifiSignal1Data))

		LmIcon.WifiSignal2Pixmap = QtGui.QPixmap()
		LmIcon.WifiSignal2Pixmap.loadFromData(base64.b64decode(LmIcon.WifiSignal2Data))

		LmIcon.WifiSignal3Pixmap = QtGui.QPixmap()
		LmIcon.WifiSignal3Pixmap.loadFromData(base64.b64decode(LmIcon.WifiSignal3Data))

		LmIcon.WifiSignal4Pixmap = QtGui.QPixmap()
		LmIcon.WifiSignal4Pixmap.loadFromData(base64.b64decode(LmIcon.WifiSignal4Data))

		LmIcon.WifiSignal5Pixmap = QtGui.QPixmap()
		LmIcon.WifiSignal5Pixmap.loadFromData(base64.b64decode(LmIcon.WifiSignal5Data))
