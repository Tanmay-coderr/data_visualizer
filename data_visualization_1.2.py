import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)

def plot_top_goal_scorers(df):
    """Plot the top 10 goal scorers from the dataset."""
    plt.figure(figsize=(10, 6))
    top_scorers = df['scorer'].value_counts().head(10)  # Get top 10 scorers
    sns.barplot(x=top_scorers.values, y=top_scorers.index, palette='coolwarm')
    plt.title('Top 10 Goal Scorers')
    plt.xlabel('Goals Scored')
    plt.ylabel('Player')
    plt.show()  # Show the plot

def plot_goals_by_team(df):
    """Plot the goals scored by the top 10 teams."""
    plt.figure(figsize=(12, 8))  # Increase figure size for better visibility
    goals_by_team = df['team'].value_counts().sort_values(ascending=False).head(10)  # Get top 10 teams
    sns.barplot(y=goals_by_team.index, x=goals_by_team.values, palette='viridis', orient='h')
    plt.title('Top 10 Teams by Goals Scored', fontsize=16)
    plt.ylabel('Team', fontsize=14)
    plt.xlabel('Goals Scored', fontsize=14)
    for index, value in enumerate(goals_by_team.values):
        plt.text(value, index, str(value), va='center')  # Show the count of goals on the bars
    plt.show()  # Show the plot

def plot_goals_distribution(df):
    """Plot the distribution of goals by minute."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df['minute'].dropna(), bins=30, kde=False, color='blue')
    plt.title('Distribution of Goals by Minute')
    plt.xlabel('Minute')
    plt.ylabel('Number of Goals')
    plt.show()  # Show the plot

def plot_penalty_vs_non_penalty(df):
    """Plot the number of penalty vs non-penalty goals."""
    plt.figure(figsize=(8, 6))
    penalty_count = df['penalty'].value_counts()
    sns.barplot(x=penalty_count.index, y=penalty_count.values, palette='Set1')
    plt.title('Penalty vs Non-Penalty Goals')
    plt.xlabel('Penalty (True/False)')
    plt.ylabel('Number of Goals')
    plt.show()  # Show the plot

def main():
    # Define the path to the CSV file
    file_path = r'C:\Users\USER NAME\Desktop\FILE NAME\DIRECTORY\goalscorers.csv'
    #ENTER YOUR DATASET PATH
    # Load the data
    df = load_data(file_path)

    # Plotting sections
    plot_top_goal_scorers(df)
    plot_goals_by_team(df)
    plot_goals_distribution(df)
    plot_penalty_vs_non_penalty(df)

if __name__ == "__main__":
    main()
