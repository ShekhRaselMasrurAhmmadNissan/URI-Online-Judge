# import numpy as np
#
# for i in np.arange(0.0, 2.2, 0.2):
#     for j in range(1, 4):
#         if (i == 0 or i == 1 or i == 2):
#             print(f'I={i:0.0f} J={(i + j):0.0f}')
#         else:
#             print(f'I={i:0.1f} J={(i + j):0.1f}')

#URI Online Judge | 1098 Sequencia IJ 4
v = 0
for i in range(11):
  for j in range(3):
    k = (j + 1) + (0.2 * i)
    if(i == 0) or (i == 5) or (i == 10):
      print('I=%d J=%d' %(v+0.2, k))
    else:
      print('I=%.1f J=%.1f' %(v, k))
  v += 0.2
