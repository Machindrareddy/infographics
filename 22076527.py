
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import and Read the Dataset
df = pd.read_csv("air passenger data1.csv")

# Check for Null Values
null_values = df.isnull().sum()

df_cleaned = df.dropna()
df['Code'].fillna('UNKNOWN', inplace=True)



# Check Data Types
data_types = df.dtypes

# Summary Statistics
summary_statistics = df.describe()

# Define a function to plot line charts for top countries
def plot_line_charts_top_countries(df, ax, top_countries, title, x_label, y_label):
    for country in top_countries:
        sns.lineplot(x='Year', y='Air transport, passengers carried', data=df[df['Entity'] == country], label=country, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
    
# Create subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

# Sort the data and select top 15
df_sorted = df.sort_values(by='Air transport, passengers carried', ascending=False)
df_top25 = df_sorted.head(25)

# Plot
sns.barplot(x='Year', y='Air transport, passengers carried', data=df_top25, ci=None, ax=ax1)
ax1.set_title('Distribution of Air Passengers by Year (Top 25)')
ax1.set_xlabel('Year')
ax1.set_ylabel('Total Passengers Carried')
ax1.tick_params(axis='x', rotation=45)


# Plot 2: Pie chart
entity_counts = df['Entity'].value_counts().head(5)
explode = (0.1, 0.1, 0.1, 0.1, 0.1)
ax2.pie(entity_counts, labels=entity_counts.index, explode=explode, autopct='%1.1f%%', startangle=140)
ax2.set_title('Proportion of Air Passengers by Top 5 Countries')

# Plot 3: Line charts for top 10 countries
top_countries_line = df.groupby('Entity')['Air transport, passengers carried'].sum().nlargest(3).index
plot_line_charts_top_countries(df, ax3, top_countries_line, 'Air Passengers Over Time - Top 10 Countries', 'Year', 'Passengers Carried')

# Plot 4: Violin plot
top_entities_violin = df.groupby('Entity')['Air transport, passengers carried'].sum().nlargest(10).index
sns.violinplot(x='Entity', y='Air transport, passengers carried', data=df[df['Entity'].isin(top_entities_violin)], palette='Set2', ax=ax4)
ax4.set_title('Distribution of Air Passengers by Top 10 Entities')
ax4.set_xlabel('Entity (Country)')
ax4.set_ylabel('Passengers Carried')
ax4.tick_params(axis='x', rotation=45)

plt.tight_layout()

# Add analysis text
analysis_text = (
    "Analysis:\n\n"
    "1. Shows varieties that can be connected with significant events or changes in the Climate in Specific Years.\n\n"
    "2. European Unions are the top 5 countries with 20% of air passengers.\n\n"
    "3. The trend of air passengers over time for the top 3 countries.\n Brazil is the biggest contributor, with a consistent increase in the \ntotal no.of Travellers conveyed during 1970 - 2020 \n\n"
    "4. Distribution strategy of air travellers amooung strong countries as it develops.\n\n"
    "Overall it is identified Trends and Changes in the quantity of Travellers who fly among nations and over time."
)

fig.text(0.5, 1.02, 'GLOBAL TOURISM', ha='center', va='center', fontsize=44)  # Add dashboard title

fig.text(0.5, -0.05, analysis_text, ha='center', va='center', fontsize=10, bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

# Add name and student ID
name_id_text = r'$\bf{Name: Machindra Tati}$'+'\n'+ r'$\bf{ID: 22076527}$'
#name_id_text = "Machindra Tati\nYour Student ID"
fig.text(0.97, -0.12, name_id_text, ha='right', va='bottom', fontsize=10)

plt.tight_layout()


plt.savefig('22076527.png', bbox_inches='tight',dpi=300)

