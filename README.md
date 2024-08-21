# Aerospace-Project
RIPS 2024 Research project with the goal of an optimal diffusion Kalman filter on particular network topologies.

<h2>The Lunar Filters</h2>
Here we outline the files in their order of importance to you. Starting with the implementation of the Diffusion Kalman Filter for Lunar TIme Transfer and a simulated Centralized Kalman Filter for Lunar Time Transfer. Then we go into the code to simulate both filters simultaneously on the same measurements for the sake of comparison.

\
**CentralizedLunarKF**\
This is the class to simulate the Centralized Kalman FIlter for Lunar Time Transfer. A more classical Kalman Filter can be found in the Standard Filters class in KF.ipynb. This has been modified in two ways. First, since the number of visible satellites changes at each time step we have a function H_cf to give the correct measurement transformation matrix.\
\
Additionally, our filter needs to simulate cross-link measurements. Since the Centralized Kalman Filter on a network is fully connected, we simply calculate the global time estimate at each station and translate that to a bias measurement at every other station. This is outlined in the msmt_sharing method.\

* This filter is tested in the TestCentralized file. Additionally, this file specifically outlines the Covariances as defined in the paper by Gao et al. The code to get the covariances is written generally where you specify constants to get the covariance specific to your simulations. 

**DiffusionLunarKF**\
This is our implementation of the Diffusion Filter for Lunar Time Transfer outlined by Gao et. al. For an in-depth overview of their algorithm we direct you to their paper. We will highlight the choices made in this implementation which weren't outlined in their paper. 

The way we simulate timing in this implementation is with the true global time updating by 7 seconds each iteration. This is divided into 3 seconds for each cross-link signal period, of which there are two, and 1 second between the start of the algorithm and the end of the cross-link update. In the time steps outlined in our report this is (t_A' - t(n)).

Then to calculate the local times at each station. In your simulations you must keep track of the true global time and the true biases and true drifts. From these you can calculate the local time at the fixed intervals of n through the standard computation. At each iteration it is expected that the true global time and true biases are at instant t_A for that iteration. That means we have T_{l,A} = T_{gR, A} + b_A 

Then to get the local times at other time steps you apply the drift to the bias. For example, since t(n) is 3 seconds after t_A we would compute T_{l,n} as T_{l,n} = T_{l,A} + 3*drift  

Then to simulate the cross-link noise, we don't send the true global estimate, we sent the global estimate plus some noise as if was samepled from a slightly different time instance, which it would be in practice.

* This file is tested in TestDiffusionKF.ipynb

**FilterComparison**\
This file sets up the Centralized and Diffusion Filters to run simultaneously on the same measurements. In particular it is based around a function run_both_filters where you specify the station topology and the number of satellite measurements. Then, you also give it the initialized Centralized and Diffusion Filters and it will simulate both filters and return the relevant data.
* This is tested in TestFilterComparison which is an important file to look at to see how you initialize both filters correctly and use the returned data.

<h2>Other Files</h2>

**Networks**\
This folder contains some examples and exercises from when we were learning basic network theory for this project.

**Old Drafts**\
This folder contains some initial implementations of various pieces of our project. 
* DiffusionKF was our first implementation of the Diffusion Kalman Filter after Cativelli and Sayed.
* GPS Simulation was some code to model actual GPS satellites orbiting earth and track get their position and velocity as sources of measurements for the Lunar Time Transfer Diffusion Filter. In our final implementation we randomly sampled these measurements instead of simulating them.
* kf_temp_wdynamics was an exercise when we were first learning kalman filtering but can be seperated from all the other work in this project similar to the Networks folder.
* TimingDiffKFAlgorithm was a first implementation of the Lunar Time Transfer Diffusion Filter but a cleaner version can be found in DiffusionLunarKF

**Standard Filters**\
This folder contains implementations and tests for the classical Centralized Kalman Filter and Diffusion Kalman Filter as well as optimization of the diffusion weights for the Diffusion Kalman Filter.
* DiffKF outlines the Diffusion Kalman Filter after Cativelli and Sayed. Each node in the network is a class and all the updates occur at each node, as they would in reality. Then the larger DiffKF class is the system which simulates the communication between nodes for measurement and estimate sharing.
    * We test DiffKF in testDiffKF with an example tracking dynamical motion. The class however is designed to the same level of generality as Cativelli and Sayed's work
* KF outlines the centralized Kalman Filter which is then tested in testKF.ipynb on a similar dynamical motion example

* testStandardOptimize is a file which outlines how to set up both the DiffKF and the KF classes to run on the same model and measurements in order to use the difference between the two to optimize the DiffKF

*Standard Filter Optimization*\
The files TestOptimize_Anta_ST, testStandardOptimizeWITH_BFGS, and TraceVSDistance are different approaches to optimizing the diffusion weights with different cost functions and optimizers. These use a similar setup and output to testStandardOptimize and then use that output to compute the resulting "cost" to feed our optimizer.

**Standard Optimization**\
These are the files used to optimize the LTT Diffusion KF. Across all the files you will find various different cost functions, satellite setups, and optimizers. But a lot of our work has been to identify which of these works best. So we reccomend you read our paper or look over our presentation to see which optimizer and cost function might best serve your purposes. \

In general, if you have true values you'll want to optimize over MSE and if not you'll want to use MSE from the estimates of a simulated centralized filter. However, if you are able to implement a new cost function which applies a sort of MSE-based regularization to Bhattacharyya distance we have reason to belive that would perform best. \

In general this folder was for exploring and testing and shouldn't be used as a reference.

