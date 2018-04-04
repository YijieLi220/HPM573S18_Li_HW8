import Parameters as P
import HW6reference as Cls
import SupportTransientState as Support

# create multiple cohorts for when the coin is head
Fairgame = Cls.MultipleGameSets(
    ids=range(1000),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    n_games_in_a_set=[P.REAL_POP_SIZE]*P.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    prob_head=[P.HEAD_PROB]*P.NUM_SIM_COHORTS # [p, p, ...]
)
# simulate all cohorts
Fairgame.simulation()

# create multiple cohorts for when the coin is tail
Unfairgame = Cls.MultipleGameSets(
    ids=range(1000,2000),   # [NUM_SIM_COHORTS, NUM_SIM_COHORTS+1, NUM_SIM_COHORTS+2, ...]
    n_games_in_a_set=[P.REAL_POP_SIZE]*P.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    prob_head=[P.HEAD_PROB_WRONG]*P.NUM_SIM_COHORTS
)
# simulate all cohorts
Unfairgame.simulation()

# print outcomes of each cohort
Support.print_outcomes(Fairgame, 'When coin with 0.5:')
Support.print_outcomes(Unfairgame, 'When coin with 0.45:')

# print comparative outcomes
Support.print_comparative_outcomes(Fairgame, Unfairgame)

