import numpy as np

def calculate(input_list):

  if len(input_list)<9:
    raise ValueError("List must contain nine numbers.")
  else:
    input_list=input_list[:9]

  np_list = np.array(input_list)
  np_mat=np_list.reshape(3,3)

  calculations={}

  mean1=list(np_mat.mean(axis=0))
  mean2=list(np_mat.mean(axis=1))
  mean3=np_mat.mean()
  calculations['mean']=[mean1,mean2,mean3]

  var1=list(np_mat.var(axis=0))
  var2=list(np_mat.var(axis=1))
  var3=np_mat.var()
  calculations['variance']=[var1,var2,var3]

  std1=list(np_mat.std(axis=0))
  std2=list(np_mat.std(axis=1))
  std3=np_mat.std()
  calculations['standard deviation']=[std1,std2,std3]

  max1=list(np_mat.max(axis=0))
  max2=list(np_mat.max(axis=1))
  max3=np_mat.max()
  calculations['max']=[max1,max2,max3]

  min1=list(np_mat.min(axis=0))
  min2=list(np_mat.min(axis=1))
  min3=np_mat.min()
  calculations['min']=[min1,min2,min3]

  sum1=list(np_mat.sum(axis=0))
  sum2=list(np_mat.sum(axis=1))
  sum3=np_mat.sum()
  calculations['sum']=[sum1,sum2,sum3]

  return calculations