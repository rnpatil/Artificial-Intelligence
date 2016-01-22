'''
 B551 Hw6      rnpatil                  #

'''
import math
import random
import pickle
import copy
import numpy as np
import pandas as pd
from scipy.stats import norm

def fitness(max_volume,volumes,prices):
    totalVolume=0
    totalBenefit=0
    
    for index in range(len(volumes)):
        totalVolume=totalVolume + volumes[index]
             
    if totalVolume <=  max_volume:              # Total volume is less than max volume i.e. knapsack can be filled for this chromosome
        for index in range(len(prices)):
         totalBenefit=totalBenefit + prices[index]   
  
    return totalBenefit
    
def randomSelection(population,fitnesses):
    totalfitness=0
    probabilities=[]
    
    
    rand_range = len(population)-1
    totalfitness = sum(fitnesses)

    if totalfitness==0:
        return population[random.randint(0, rand_range)] 
          
          
    for index in range(len(fitnesses)):
         fitnessprobability=float(fitnesses[index])/totalfitness
         probabilities.append(fitnessprobability)
              
               
    pick = random.random()   # picks a random probability 
    current=0
    for index in range(len(probabilities)):
     current += probabilities[index]
     if current > pick:
        return population[index]     # return random selected chromosome from the population based on weighted probability of fitnesses
        
        

def reproduce(mom,dad):
 rand_range = len(mom) - 1
 crossover_point =  random.randint(0, rand_range)
 offspring= np.concatenate((mom[:crossover_point],dad[crossover_point:]), axis=0)
 return offspring


def mutate(child):
 
   rand_range = len(child) - 1
   mutation_point =  random.randint(0, rand_range)   # select a mutation point
  
   for index in range(len(child)):
	if (mutation_point == index):
		if (child[index] == 0):
			child[index] = 1
		else:
		 child[index] = 0
  
   return child                                     # return mutated child
  

def compute_fitnesses(world,chromosomes):
    
    return [fitness(world[0], world[1] * chromosome, world[2] * chromosome) for chromosome in chromosomes]



def genetic_algorithm(world,popsize,max_years,mutation_probability):


   
    volumes= world[1]
    lengthofchromosomes=len(volumes)
    fitnesses=[] 
    chromosomes=[]
    finalchromosomes=[]
    totalfitness=0
    elistismRate= 0.3
    elitenumber = int(math.ceil(elistismRate*popsize))
     
    
    
    
    #initial population creation start
    
    while(totalfitness<=0):
     chromosomes=[]
     for index in range(popsize):
        numpyarray =np.array(np.random.randint(2, size=lengthofchromosomes))
        chromosomes.append(numpyarray)
  
     fitnesses=np.array(compute_fitnesses(world,chromosomes))
     totalfitness = sum(fitnesses)
   
    #initial population creation end 
    
    
   # loop start count 0 to max years
    count = 0 
    while (count < max_years):
     newpopulation=[]
     
     #elitism start
     
     elitismcounter=0
     elitechromosomes = copy.deepcopy(chromosomes) 
     elitefitnesses = copy.deepcopy(fitnesses) 

     while (elitismcounter < elitenumber):
      eliteindex=np.argmax(elitefitnesses)
      newpopulation.append(elitechromosomes[eliteindex])
      elitechromosomes=np.delete(elitechromosomes, eliteindex, axis=0)
      elitefitnesses=np.delete(elitefitnesses, eliteindex, axis=0)
      elitismcounter= elitismcounter + 1
      
     #elitism end
     
     
     

     while(len(newpopulation)<popsize):
         
      mom=randomSelection(chromosomes,fitnesses)  #random selected mom
      dad=randomSelection(chromosomes,fitnesses)  #random selected dad
    
      offspring=reproduce(mom,dad)               # crossover completed offspring
    
      pick = random.random()   
      if pick < mutation_probability:
       offspring=mutate(offspring)
        
      newpopulation.append(offspring)
      
      # inner while end 
     
     chromosomes = copy.deepcopy(newpopulation)  
     fitnesses=np.array(compute_fitnesses(world,chromosomes))
     tupleEntry =chromosomes,fitnesses
     finalchromosomes.append(tupleEntry)  # add one entry per year
     
     count = count + 1
     
     #outer while end
    return finalchromosomes
  
   
def run(popsize,max_years,mutation_probability):
    '''
    The arguments to this function are what they sound like.
    Runs genetic_algorithm on various knapsack problem instances and keeps track of tabular information with this schema:
    DIFFICULTY YEAR HIGH_SCORE AVERAGE_SCORE   BEST_PLAN
    '''
    table = pd.DataFrame(columns=["DIFFICULTY", "YEAR", "HIGH_SCORE", "AVERAGE_SCORE", "BEST_PLAN"])
    sanity_check = (10, [10, 5, 8], [100,50,80])
    chromosomes = genetic_algorithm(sanity_check,popsize,max_years,mutation_probability)
    for year, data in enumerate(chromosomes):
        year_chromosomes, fitnesses = data
        table = table.append({'DIFFICULTY' : 'sanity_check', 'YEAR' : year, 'HIGH_SCORE' : max(fitnesses),
            'AVERAGE_SCORE' : np.mean(fitnesses), 'BEST_PLAN' : year_chromosomes[np.argmax(fitnesses)]}, ignore_index=True)
    easy = (20, [20, 5, 15, 8, 13], [10, 4, 11, 2, 9] )
    chromosomes = genetic_algorithm(easy,popsize,max_years,mutation_probability)
    for year, data in enumerate(chromosomes):
        year_chromosomes, fitnesses = data
        table = table.append({'DIFFICULTY' : 'easy', 'YEAR' : year, 'HIGH_SCORE' : max(fitnesses),
            'AVERAGE_SCORE' : np.mean(fitnesses), 'BEST_PLAN' : year_chromosomes[np.argmax(fitnesses)]}, ignore_index=True)
    medium = (100, [13, 19, 34, 1, 20, 4, 8, 24, 7, 18, 1, 31, 10, 23, 9, 27, 50, 6, 36, 9, 15],
                   [26, 7, 34, 8, 29, 3, 11, 33, 7, 23, 8, 25, 13, 5, 16, 35, 50, 9, 30, 13, 14])
    chromosomes = genetic_algorithm(medium,popsize,max_years,mutation_probability)
    for year, data in enumerate(chromosomes):
        year_chromosomes, fitnesses = data
        table = table.append({'DIFFICULTY' : 'medium', 'YEAR' : year, 'HIGH_SCORE' : max(fitnesses),
            'AVERAGE_SCORE' : np.mean(fitnesses), 'BEST_PLAN' : year_chromosomes[np.argmax(fitnesses)]}, ignore_index=True)
    hard = (5000, norm.rvs(50,15,size=100), norm.rvs(200,60,size=100))
    chromosomes = genetic_algorithm(hard,popsize,max_years,mutation_probability)
    for year, data in enumerate(chromosomes):
        year_chromosomes, fitnesses = data
        table = table.append({'DIFFICULTY' : 'hard', 'YEAR' : year, 'HIGH_SCORE' : max(fitnesses),
            'AVERAGE_SCORE' : np.mean(fitnesses), 'BEST_PLAN' : year_chromosomes[np.argmax(fitnesses)]}, ignore_index=True)
    for difficulty_group in ['sanity_check','easy','medium','hard']:
    #for difficulty_group in ['sanity_check']:
        group = table[table['DIFFICULTY'] == difficulty_group]
        bestrow = group.ix[group['HIGH_SCORE'].argmax()]
        print("Best year for difficulty {} is {} with high score {} and chromosome {}".format(difficulty_group,int(bestrow['YEAR']), bestrow['HIGH_SCORE'], bestrow['BEST_PLAN']))
    table.to_pickle("results.pkl") 
    
    #saves the performance data, in case you want to refer to it later. pickled python objects can be loaded back at any later point.

def main():

 run(40,30,0.3) 
 
main() 
