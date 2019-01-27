#  We have a string and width W.
# Write code to wrap the string into a paragraph of width W.

import textwrap

inputString = 'Sunset is the time of day when our sky meets the outer space solar winds. There are blue, pink, and purple swirls, spinning and twisting, like clouds of balloons caught in a blender. The sun moves slowly to hide behind the line of horizon, while the moon races to take its place in prominence atop the night sky. People slow to a crawl, entranced, fully forgetting the deeds that still must be done. There is a coolness, a calmness, when the sun does set.'
W = 60

# Wrap this string.
a = textwrap.TextWrapper(width=W)
outputString = a.wrap(text=inputString)

# Print each line.
for item in outputString:
    print(item)
