from pathlib import Path

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

csv_path = Path(__file__).resolve().parent / '15_programming_languages_2026.csv'

df = pd.read_csv(csv_path)

print('Primeros registros:')
print(df.head())
print('\nÚltimos registros:')
print(df.tail())
print('\nDataFrame completo:')
print(df)

df.isnull().sum()
df.duplicated().sum()
df.info()
df.describe()
df['Language'].unique() 
df['Creator'].unique()
df['Paradigm']
df['Paradigm'] = df['Paradigm'].str.lower()
df['Paradigm'].unique()
df[df['Paradigm'] == 'visual']
df['Typing'] = df['Typing'].str.lower()
df['Typing']
df['Typing'].unique()
df = df.drop_duplicates()
df.duplicated().sum()
df = df.fillna('N/A')
df.isnull().sum()
df.info()
df['Paradigm'] = df['Paradigm'].replace({'visual':'multi-paradigm'})
df['Paradigm'].unique()

# Distribución de Rating
plt.figure(figsize=(10,6))
sns.histplot(df['Rating'], bins=15, kde=True)
plt.title("Distribución de Rating")
plt.xlabel("Rating (%)")
plt.ylabel("Frecuencia")
plt.show()

# Boxplot de Change_Rate
plt.figure(figsize=(10,6))
sns.boxplot(x=df['Change_Rate'])
plt.title("Boxplot de Change_Rate 2025-2026")
plt.show()

# Scatter Plot Rating vs Change
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x="Rating", y="Change_Rate", hue="Paradigm")
plt.title("Relación entre Rating y Change Rate")
plt.xlabel("Rating (%)")
plt.ylabel("Cambio (%)")
plt.show()

plt.figure(figsize=(12,6))
sns.barplot(
    data=df.head(10),
    x="Language",
    y="Rating",
    hue="Language",       
    palette="viridis",
    legend=False         
)
plt.title("Top 10 Lenguajes por Rating")
plt.xticks(rotation=45)
plt.show()

# Heatmap de correlaciones
plt.figure(figsize=(8,6))
sns.heatmap(df[['Rating','Change_Rate','Year_Created']].corr(), annot=True, cmap="coolwarm")
plt.title("Correlaciones entre variables")
plt.show()

# Violin plot por paradigma (ajustado a nuevas versiones de Seaborn)
plt.figure(figsize=(12,6))
sns.violinplot(
    data=df,
    x="Paradigm",
    y="Change_Rate",
    hue="Paradigm",     
    palette="muted",
    legend=False          
)
plt.title("Distribución de Change_Rate por Paradigma")
plt.xticks(rotation=45)
plt.show()

# Treemap de participación en Rating
import squarify
plt.figure(figsize=(12,8))
squarify.plot(sizes=df['Rating'], label=df['Language'], alpha=.8)
plt.title("Proporción de Rating por Lenguaje")
plt.axis('off')
plt.show()

# Bubble chart
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x="Rating", y="Change_Rate",
                size="Year_Created", hue="Paradigm", alpha=0.7, sizes=(50,500))
plt.title("Bubble Chart: Rating vs Change vs Año de Creación")
plt.show()

# Insights (conocimientos que aportan valor)
top_growth = df.sort_values("Change_Rate", ascending=False).head(5)
top_decline = df.sort_values("Change_Rate").head(5)

print("\nLenguajes con mayor crecimiento:\n", top_growth[['Language','Change_Rate']])
print("\nLenguajes con mayor caída:\n", top_decline[['Language','Change_Rate']])

