import numpy as np

def brooks_corey(h,parameters):
 
 #Define the parameters
 hb = parameters['hb']
 theta_r = parameters['theta_r']
 theta_s = parameters['theta_s']
 l = parameters['lambda']

 #Compute the volumetric water content
 theta = np.zeros(h.size)
 m = h >= hb
 theta[m==1] = theta_r + (theta_s - theta_r)*(h[m]/hb)**-l
 theta[m==0] = theta_s

 return theta

def van_genuchten(h,parameters):

 #Define the parameters
 alpha = parameters['alpha']
 theta_r = parameters['theta_r']
 theta_s = parameters['theta_s']
 n = parameters['n']

 m = 1 - 1/n
 theta = theta_r + (theta_s - theta_r)/(1 + (alpha*h)**n)**m

 return theta
