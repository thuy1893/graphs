import pandas as pd
import matplotlib.pyplot as plt

df2 = pd.read_csv("phyla_noUn.csv")
df2.plot.bar(stacked=True, x='taxon', rot=45, width=0.85) 
#the x='taxon' is to set the column 'taxon' as the lavels on the x-axis.]
#for colormap, see: http://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/Show_colormaps
#ax.invert_yaxis()
#plt.legend(bbox_to_anchor=(1.0, 1.0))
#plt.gca().legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.tight_layout()
#plt.legend(title = "Phyla")
current_handles, current_labels = plt.gca().get_legend_handles_labels()

# sort or reorder the labels and handles
reversed_handles = list(reversed(current_handles))
reversed_labels = list(reversed(current_labels))

# call plt.legend() with the new values
plt.legend(reversed_handles,reversed_labels, bbox_to_anchor=(1, 1), title='Phyla')#can add in there fontsize=11 if needed
plt.tight_layout()
plt.xlabel('Sample IDs', fontsize=16, fontweight='bold')
plt.ylabel('% Relative abundance', fontsize=16, fontweight='bold')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.show()
