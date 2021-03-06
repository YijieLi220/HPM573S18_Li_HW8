
HEAD_PROB = 0.5        # annual probability of mortality
HEAD_PROB_WRONG = 0.45    # drug effectiveness:
                            # ratio the annual mortality probability when using the drug to when not using the drug.
TIME_STEPS = 100    # simulation length
ALPHA = 0.05        # significance level

# settings for steady-state simulation
SIM_POP_SIZE = 1000     # population size of the simulated cohort

# settings for transient-state simulation
REAL_POP_SIZE = 100     # size of the real cohort to make the projections for
NUM_SIM_COHORTS = 1000  # number of simulated cohorts used for making projections