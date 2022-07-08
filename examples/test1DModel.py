'''
In this example, we will solve a 1D model using the framework developed in
Hansen, Khorrami, and Tourre.
'''

## Step 0: import dependencies
#------------------------------------------#
import mfr.modelSoln as m
import numpy as np

## Step 1: Create a model
#------------------------------------------#

#### To creae a model, you need to input its parameters in a dictionary.
#### The eaiest way is to use the default parameters dictionary and make changes
#### based on it. The default parameters dictionary can be accessed through
#### m.paramsDefault.

params = m.paramsDefault.copy()

#### The default parameters set is a 1D model.

#### Now, create a Model
testModel = m.Model(params)

## Step 2: Solve the model
#------------------------------------------#

#### This step is very simple: use the .solve() method.
testModel.solve()
testModel.printInfo() ## This step is optional: it prints out information regarding time, number of iterations, etc.
testModel.printParams() ## This step is optional: it prints out the parameteres used.

## Step 3: Compute stationary density
#------------------------------------------#

#### This method can only be called after the model is solved.
testModel.computeStatDent()
#### After computing the stationary density, you can access the density through
#### testModel.dent and its CDFs and unconditional distributions of the state variables
#### through testModel.unconds and testModel.cdfs

## Step 4: Compute moments and correlation
#------------------------------------------#

#### This step can only be completed after computing the stationary dneisty.
testModel.computeMoments(['W', 'r'])

#### In this example, we want to see the mean and standard deviation of
#### the wealth share and interest rate. The input is a list of the variables
#### that you would like to compute moments for. The nomenclature is such that
#### the method minus "()". For example, you would access variable r through
#### testModel.r(). To configure the inputs for this function, ignore "()".

#### After computing moments, you can access them through testModel.moments,
#### where the first moment is the mean and second is sd.
print(testModel.macroMoments)
print(testModel.apMoments)

#### You can access the FK matrix used to compute for the stationary density
#### by testModel.FKmat

#### To compute correlations, the procedure is very similar. To access
#### the correlations, call testModel.corrs.
testModel.computeCorrs(['W', 'r'])
print(testModel.corrs)

## Step 5: Compute shock elasticities
#------------------------------------------#

#### To compute shock elsaticities, we recommend that you compute stationary density
#### beforehand, so that we can select quintiles from the distribution.

#### Method 1:
####  You may put in the quintiles of the state variable in a dictionary and use
####  it as the input for argument pcts (as shown below). Other arguments needed
####  include T, dt, and perturb, where perturb is the variable you want to shock.
####  If you'd like to shock consumption, put in "C" as you would normally use
####  testModel.C() to get consumption. By default, if we use zero first derivatives
####  as the boundary conditions. For a more detailed discussion, refer to documentation
####  on mfr.sem.

testModel.computeShockElas(pcts = {'W':[.3,.7]}, T = 100, dt = 1, perturb = 'C')

#### Method 2:
####  You may also put in the actual values of the starting points. All other
####  arguments are the same

testModel.computeShockElas(points = np.matrix([0.5]), T = 100, dt = 1, perturb = 'C')

#### Access
####  To access the shock elasticities, you can use the following three attributes.
####  Note that the output is the same as described in the documentation for mfr.sem.
####    testModel.expoElas  (exposure elasticities)
####    testModel.priceElasHouseholds (price elasticities using households sdf)
####    testModel.priceElasExperts  (price elasticities using experts sdf)
####  Furthermore, you can access the linear systems through
####    testModel.linSysExpo (linear system used to solve for the exposure elasticities)
####    testModel.linSysH   (linear system used to solve for households' elasticities)
####    testModel.linSysE   (linear system used to solve for experts' elasticities)
