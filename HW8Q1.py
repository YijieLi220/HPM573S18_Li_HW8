import Parameters as P
import HW6reference as Cls
import SupportSteadyState as Support

FairGames = Cls.SetOfGames(id=1, prob_head=0.5, n_games=P.SIM_POP_SIZE)
UnfairGames = Cls.SetOfGames(id=1, prob_head=0.45, n_games=P.SIM_POP_SIZE)
outcomes1 = FairGames.simulation()
outcomes2 = UnfairGames.simulation()
GamesOutcomes1 = Cls.SetOfGamesOutcomes(FairGames)
GamesOutcomes2 = Cls.SetOfGamesOutcomes(UnfairGames)

# print outcomes of each cohort
Support.print_outcomes(GamesOutcomes1,'If we flip a fair coin, we got ')
Support.print_outcomes(GamesOutcomes2,'If we flip a unfair coin, we got ')

# print comparative outcomes
Support.print_comparative_outcomes(GamesOutcomes1, GamesOutcomes2)