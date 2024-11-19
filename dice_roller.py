# Code used in this assignment was originally taken from Eric Matthes - Python Crash Course book
# Code was catabolized by Ronald Kiprono
# Cannabalized by Ian Cowie

import random
import pandas as pd
import plotly.express as px

def roll_dice():
    return random.randint(1, 6)

def play_dice():
    rolls = []
    rolling = True
    print("Welcome to the Dice Roller!")
    while rolling:
        result = roll_dice()
        print(f"You rolled a {result}!")
        rolls.append(result)
        choice = input("Do you want to roll again? (yes/no): ").lower()
        if choice != 'yes':
            rolling = False
    print("Thanks for playing! Now visualizing your results...")
    return rolls


def visualize_rolls(rolls):
    df = pd.DataFrame(rolls, columns=['Rolls'])
    fig = px.histogram(df, x='Rolls', title='Distribution of Dice Rolls',
                       labels={'Rolls': 'Dice Value'},
                       nbins=6)
    fig.update_layout(xaxis_title='Dice of value', yaxis_title='count', bargap=0.2)
    fig.show()

# Start the dice roller and collect the results
rolls = play_dice()

# Visualize the results
visualize_rolls(rolls)

# Function to roll the dice multiple times and store results
def roll_multiple_times(num_rolls):
    rolls = []
    for _ in range(num_rolls):
        rolls.append(roll_dice())
    return rolls

# Roll the dice 1000 times
num_rolls = 1000
rolls = roll_multiple_times(num_rolls)

# Convert the list of rolls into a Pandas DataFrame
df = pd.DataFrame(rolls, columns=['Dice Rolls'])

# Create a histogram of the dice rolls
fig = px.histogram(df, x='Dice Rolls', title='Dice Roll Frequency',
                   labels={'Dice Rolls': 'Dice Value'}, nbins=6)

# Show the histogram
fig.show()

def visualize_rolls(rolls):
    df = pd.DataFrame(rolls, columns=['Rolls'])
    fig = px.histogram(df, x='Rolls', title='Distribution of Dice Rolls',labels={'Rolls': 'Dice Value'},
                       opacity =0.7)
    fig.update_layout(xaxis_title='Dice value', yaxis_title='Frequency', bargap=0.2)
    fig.show()

# Start the dice roller and collect the results
rolls = play_dice()

# Visualize the results
visualize_rolls(rolls)

import random
import plotly.express as px

def roll_two_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

# Roll the dice 1000 times and store the sums
rolls = [roll_two_dice() for _ in range(1000)]

# Plot the histogram using plotly
fig = px.histogram(rolls, nbins=11, title="Distribution of Two Dice Rolls (1000 Rolls)", labels={'value':'Sum of Dice'}, opacity=0.7)
fig.update_layout(xaxis_title='Sum of Dice', yaxis_title='Frequency', bargap=0.2)
fig.show()

num_rolls = 100
rolls = roll_multiple_times(num_rolls)

# Convert the list of rolls into a Pandas DataFrame
df = pd.DataFrame(rolls, columns=['Dice Rolls'])

# Create a histogram of the dice rolls
fig = px.histogram(df, x='Dice Rolls', title='Dice Roll Frequency',
                   labels={'Dice Rolls': 'Dice Value'}, nbins=6)

# Show the histogram
fig.show()

import plotly.express as px

# Create a histogram of the dice rolls
fig = px.histogram(df, x='Dice Rolls', title='Dice Roll Frequency',
                   labels={'Dice Rolls': 'Dice Value'}, nbins=6)  # 6 bins for 6 dice values

# Show the plot
fig.show()

fig.write_html('dice_visual_d6d10.html')