import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
from calendar import month_name
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates = ['date'], index_col = "date")

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16,8))
    ax.plot(df.index, df['value'], color = 'red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # create the month column
    months = month_name[1:]
    df['months'] = pd.Categorical(df.index.strftime('%B'), categories=months, ordered=True)
    
    # pivot the dataframe into the correct shape
    dfp = pd.pivot_table(data=df, index=df.index.year, values='value', columns='months')
    
    # Plot
    ax = dfp.plot(kind='bar', figsize=(8,8))
    ax.set_ylabel('Avarage Page Views')
    ax.set_xlabel('Years')
    ax.legend(title="Months")

    # Save image and return fig (don't change this part)
    plt.savefig('bar_plot.png')
    return plt

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16,7))
    axes[0] = sns.boxplot( x=df_box.year, y=df_box['value'], ax=axes[0]).set(title='Year-wise Box Plot (Trend)', xlabel='Year', ylabel='Page Views')
    axes[1] = sns.boxplot( x=df_box.month, y=df_box['value'], ax=axes[1]).set(title='Month-wise Box Plot (Seasonality)',xlabel='Month', ylabel='Page Views')
    fig.show()
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig