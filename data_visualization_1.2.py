import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)

def plot_numerical_data(df):
    """Plot histograms for numerical columns."""
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numerical_cols:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[col].dropna(), kde=True, color='blue')
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Count')
        plt.show()

def plot_categorical_data(df):
    """Plot bar charts for categorical columns using the actual names."""
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    for col in categorical_cols:
        plt.figure(figsize=(10, 6))
        value_counts = df[col].value_counts().head(10)  # Limit to top 10 categories
        sns.barplot(x=value_counts.index, y=value_counts.values, palette='coolwarm')
        plt.title(f'Top Categories in {col}')
        plt.xlabel(col)
        plt.ylabel('Count')
        plt.xticks(rotation=45)  # Rotate x labels for better visibility
        plt.show()

def plot_pairplot(df):
    """Generate a pairplot for numerical columns to show relationships."""
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    if len(numerical_cols) > 1:
        sns.pairplot(df[numerical_cols].dropna())
        plt.show()

def main():
    # Prompt user for the file path to the dataset
    file_path = input("Please enter the path to your dataset (CSV file): ")

    # Load the data
    df = load_data(file_path)

    # Plot numerical data
    plot_numerical_data(df)

    # Plot categorical data
    plot_categorical_data(df)

    # Generate pairplots for numerical data
    plot_pairplot(df)

if __name__ == "__main__":
    main()
