import numpy as np
import os
lib_dir = os.path.dirname(os.path.realpath(__file__))

def neuro(W1,W2,X):

 # evaluate neural networks
 #   feed forward nnet, with single hidden layer
 #
 #  Y = neuro(W1,W2,X)
 #  Input:
 #  W1(nh,ni+1) = Weights to hidden layer 
 #  W2(no,nh+1) = Weights to output
 #  X(N,ni)     = data
 #  Output:
 #  Y(N,no)     = predicted
 #
 #   Budiman (01.2004)
 [N,ni]=X.shape
 # from input layer to hidden layer
 tmp = np.vstack((X.T,np.ones((1,N))))
 h = np.dot(W1,tmp)
 y1 = np.tanh(h)
 # from hidden layer to output layer
 tmp = np.vstack((y1,np.ones((1,N))))
 h2 = np.dot(W2,tmp)
 Y = h2.T

 return Y

def transfp(Y,opt):

 # transform VG parameter so has normal dist & value >1

 if opt==1:
    #transformtion
    Y[:,0] = np.sqrt(Y[:,0]) #theta_r
    Y[:,1] = np.log(Y[:,1]) #alfa
    Y[:,2] = np.log(Y[:,2]-1) #n
 else:
    # back transformation
    Y[:,0] = Y[:,0]**2 #theta_r (cm3/cm3)
    Y[:,1] = 10*np.exp(Y[:,1]) #alfa (cm-1)
    Y[:,2] = np.exp(Y[:,2])+1 #n

 return Y

def ptf_van_genuchten(X,nbag):

 # load the parameters
 Wr1 = np.loadtxt('%s/Wrs1a.txt' % lib_dir)
 Wr2 = np.loadtxt('%s/Wrs2a.txt' % lib_dir)

 # evaluate the function
 ni = 6   # no. inputs
 no = 3   # no. outputs
 nh = 5   # no. hidden units
 #nbag = 100 # no. bootstrap

 #X=[sand,clay,bd,theta_s,theta_33,theta_1500];   % input data
 npred = X.shape[0] # no. predictions

 #Initialize prediction
 pred = np.zeros((npred,nbag,no))

 for ibag in xrange(nbag): # loop through n bootstrap
  W1 = np.reshape(Wr1[ibag,:].T,(ni+1,nh)).T
  W2 = np.reshape(Wr2[ibag,:].T,(nh+1,no)).T
  bp = neuro(W1,W2,X) # evaluate the nnet
  bp = transfp(bp,0) # back transform to parameter  values
  pred[:,ibag,:] = bp # predicted parameters

 output = {'alpha':pred[:,:,1],
           'n':pred[:,:,2],
           'theta_r':pred[:,:,0]}

 return output

def ptf_brooks_corey(X,nbag):

 #Retrieve van genuchten parameters
 pred = ptf_van_genuchten(X,nbag)

 #Create output dictionary
 output = {'theta_r':pred['theta_r']}

 #Convert parameters to brooks corey
 output['lambda'] = -0.631 + 0.71*pred['n'] #Lambda
 output['hb'] = 1/pred['alpha'] #Hb

 return output

def van_genuchten(X,nbag=100):

 #Calculate the parameters sets
 vg = ptf_van_genuchten(X,nbag=nbag)

 #For each variable calculate the 5th percentile, median, and 95th percentile
 output = {}
 for var in vg: 
  p5 = np.percentile(vg[var],5)
  p50 = np.percentile(vg[var],50)
  p95 = np.percentile(vg[var],95)
  output[var] = {'pct5':p5,'median':p50,'pct95':p95}
 
 return output

def brooks_corey(X,nbag=100):

 #Calculate the parameters sets
 vg = ptf_brooks_corey(X,nbag=nbag)

 #For each variable calculate the 5th percentile, median, and 95th percentile
 output = {}
 for var in vg:
  p5 = np.percentile(vg[var],5)
  p50 = np.percentile(vg[var],50)
  p95 = np.percentile(vg[var],95)
  output[var] = {'pct5':p5,'median':p50,'pct95':p95}
  
 return output

