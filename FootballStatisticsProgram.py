# Lesson 8, Written by David Turner
# AAAAAAAAAAAAAAAAAAAAAAAA , 24 chars for testing the opponent input

print("St. John's Pebbles Football Team")
print("Games Statistics Program")
print()
print("Please enter the following required values:")
print()
gameDate = input("Game date (yyyy-mm-dd) :  ")
opponent = input("Opponent : ")
print()
numPassAttempts = int(input("Number of pass attempts :      "))
numCompletions = int(input("Number of Completions :        "))
totPassYards = int(input("Total passing yards :          "))
numTouchdowns = int(input("Number of touchdowns :         "))
numIntercept = int(input("Number of interceptions :      "))
print()
numRushAttempt = int(input("Number of rushing attempts :   "))
totRushingYards = int(input("Total rushing yards :          "))
numRushTouchdowns = int(input("Number of rushing touchdowns : "))
print()

# Percent Passing Completion and yards per pass
passCompletion = (numCompletions/numPassAttempts)*100
yrdPerPass = (totPassYards/numCompletions)

# QB rating, includes ratings on passing, yards, TD, interceptions
passRate = ((numCompletions/numPassAttempts)-0.3)/0.2
yrdsRate = ((totPassYards/numPassAttempts)-3)/4
tdRate = (numTouchdowns/numPassAttempts)/0.05
intRate = (0.095-(numIntercept/numPassAttempts))/0.04
QB_Rating = ((passRate+yrdsRate+tdRate+intRate)*100)/6

# Rushing stats, average yards, TD efficiency
aveRushYrds = totRushingYards/numRushAttempt
TD_Efficiency = (numRushTouchdowns/numRushAttempt)*100

# formatting for output for QB Stats
passCompletionDsp = "{:.0f}%".format(passCompletion)
QB_RatingDsp = "{:.1f}".format(QB_Rating)

# formatting for output for rushing Stats
yrdPerPassDsp = "{:.0f}".format(yrdPerPass)
aveRushYrdsDsp = "{:.1f}".format(aveRushYrds)
TD_EfficiencyDsp = "{:.1f}%".format(TD_Efficiency)

# Program output
print("St. John's Pebbles Football Team")
print("Games Statistics Program")
print()
print("Game Statistics vs {:<24} on {:>10}".format(opponent, gameDate))
print("-"*58)
print("Quarterback Statistics:")
print()
print("Number of pass attempts:  {:>3d}    Pass Completion %:   {:>4}".format(numPassAttempts, passCompletionDsp))
print("Number of completions:    {:>3d}".format(numCompletions))
print("Total passing yards:      {:>3d}    Yards Per Pass:       {:>3}".format(totPassYards, yrdPerPassDsp))
print("Number of touchdowns:     {:>3d}".format(numTouchdowns))
print("Number of interceptions:  {:>3d}    Quarterback Rating: {:>5}".format(numIntercept, QB_RatingDsp))
print()
print("Number of rushing atts:   {:>3d}    Avg Yards Per Rush:  {:>4}".format(numRushAttempt, aveRushYrdsDsp))
print("Total rushing yards:      {:>3d}".format(totRushingYards))
print("Number of rushing TD's:   {:>3d}    TD Efficiency:      {:>5}".format(numRushTouchdowns, TD_EfficiencyDsp))
print("-"*58)
