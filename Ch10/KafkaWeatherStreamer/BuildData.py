import json
import numpy as np
from datetime import datetime


class BuildData:

    def loadTemplate(self,path):
        with open(path) as data_file:    
         data = json.load(data_file)

        return  data

    def getDistribution(self,json_object):
      
      
        
        data = {}
        mu, sigma, arrayLen = 0, 0.1,1 # mean and standard deviation
        loc, scale = 10, 1
        beginning, end = 1,10

        for key,value in json_object.items():
            if('Random'in value):
                data[key] = np.random.randint(beginning,end)
            
            if('Time' in value):
                now = datetime.utcnow() # current date and time
                data[key] =str(now)

            if ('NormalDistribution' in value):
                data[key] = np.random.normal(mu, sigma, arrayLen)[0]
        
            if ('Logicstic' in value):
                data[key] = np.random.logistic(loc, scale, arrayLen)[0]
    
            #Shape\
            if ('Triangular' in value):
                data[key] = np.random.triangular(-3, 0, 8, 1)[0]
    
            #beta is a distribution of shape using A & B
            #The beta distribution is a suitable model for the random behavior of percentages and proportions.
            if ('Beta' in value):
                data[key] = np.random.beta(10, 20, 1)[0]
   
            #Dirichlet is a multidementional beta
            #s = np.random.dirichlet((10, 5, 3), 1).transpose()
            #data['Dirichlet1'] = s[0][0]
            #data['Dirichlet2'] = s[1][0]
            #data['Dirichlet'] = s[2][0]

        return json.dumps(data)




    

