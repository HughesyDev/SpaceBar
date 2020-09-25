# for ID selection, names : drinks
# ID names = enumerate names
# ID drink = enumerate drinks
# ID both to print selection for i.e. 
#    -- for person, drink in zip(people, drinks)
#    --     print(f"{enumnames} {enumdrinks}")

# TODO: 6  Can you add drink preferences by ID of person/drink?
# TODO: 7  Can you create a round? (round class)
# TODO: 8  Are drink preferences persisted?
# TODO: 9  Are round information persisted?
# TODO: 11 Can the payer assign a round to themselves?
# DONE: 12 Is there a sensible directory structure?
# DONE: 13 Is data saving logic extracted to its own module?
# TODO: 14 Are other classes extracted to their own module?
# TODO: 15 Create Round, use ID for names, drinks in the order

# TESTS NEEDED for technical rubric
# TODO: Test for drink / person validation
# TODO: Test that preferences are added correctly
### TODO: Making a round (isInstance?)
### TODO: Assign a brewer to a Round
### TODO: Printing a Round

# Do clear() after every command? Make it look "cleaner"

# __init__(self, brewer, order={})

# Separate Testing logic to new module
# Make Python --m Unittest.py or something work. Test Suite

# EXTRA FEATURES
# - Leaderboards
# - Brew stats: most popular brew, brews per round etc.
# - A Slack bot
# - Suggest new drinks to try based on people's brew history?