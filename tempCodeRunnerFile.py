import numpy as np
notes = np.empty([3,4]) #n lines, 4 columns
notes = np.random.rand(3, 4)
print(notes)
print(notes[0,:]) #prints 3rd column