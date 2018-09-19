##Python class
##Venn Diagram
## Data vizualization using python

### installed packages ### 
## pandas
## matplotlib
## scipy
## seaborn


### modules ### 

import numpy as np
import pandas as pd
from matplotlib_venn import venn2, venn2_circles
import matplotlib.pyplot as plt
from pylab import savefig
plt.switch_backend('Agg')

print ("modules...")

### import data ### 

data = pd.read_csv ("venn.csv")
print(data [:7])

### Venn diagram ###


v = venn2(subsets = {'10': 1, '01': 1, '11': 1}, set_labels = ('Summer', 'Winter'))
v.get_patch_by_id('10').set_alpha(0.5)
v.get_patch_by_id('10').set_color('blue')
v.get_patch_by_id('01').set_alpha(0.5)
v.get_patch_by_id('01').set_color('red')
v.get_patch_by_id('11').set_alpha(0.75)
v.get_patch_by_id('11').set_color('purple')
v.get_label_by_id('10').set_text('')
v.get_label_by_id('01').set_text('')
v.get_label_by_id('11').set_text('')
v.get_label_by_id('A').set_text('')
v.get_label_by_id('B').set_text('')
v.get_label_by_id('A').set_size(20)
v.get_label_by_id('B').set_size(20)
plt.title("Summer vs Winter roosts")
plt.annotate('Summer', xy = v.get_label_by_id('10').get_position(), xytext = (-30,-70), size = 'xx-large',
            ha = 'center', textcoords = 'offset points', bbox = dict(boxstyle = 'round, pad=0.5', fc = 'white', alpha = 0.8),
            arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3, rad = 0.5', color = 'black'))

plt.annotate('Winter', xy = v.get_label_by_id('01').get_position(), xytext = (30,-70), size = 'xx-large',
            ha = 'center', textcoords = 'offset points', bbox = dict(boxstyle = 'round, pad = 0.5', fc = 'white', alpha = 0.8),
            arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad = -0.5',color = 'black'))
plt.savefig("venntest.png")

