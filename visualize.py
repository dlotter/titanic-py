import matplotlib.pyplot as plt
import pandas as pd

# read csv
df = pd.read_csv("train.csv")

# configure graph
fig = plt.figure(figsize=(18,6))
alpha = alpha_scatterplot = 0.2
alpha_bar_chart = 0.55

# survived vs deceased
plt.subplot2grid((2,3),(0,0))
df.Survived.value_counts(normalize=True).plot(kind='bar', alpha=alpha_bar_chart)
plt.title("Distribuição dos Sobreviventes, (1 = Sobreviveu)")

# survival by age
plt.subplot2grid((2,3),(0,1))
plt.scatter(df.Survived, df.Age, alpha=alpha_scatterplot)
plt.ylabel("Age")
plt.grid(b=True, which="major", axis="y")
plt.title("Idade e Sobreviventes, (1 = Sobreviveu)")

# class distribution
plt.subplot2grid((2,3),(0,2))
df.Pclass.value_counts().plot(kind="barh", alpha=alpha_bar_chart)
plt.title("Classes")

# age distribution within class
plt.subplot2grid((2,3),(1,0), colspan=2)
for x in [1,2,3]:
    df.Age[df.Pclass == x].plot(kind="kde")
plt.xlabel("Age")
plt.title("Distribuição de Idades nas Classes")
plt.legend(("1 Classe", "2 Classe", "3 Classe"))

# passengers boarding location
plt.subplot2grid((2,3),(1,2))
df.Embarked.value_counts(normalize=True).plot(kind='bar', alpha=alpha_bar_chart)
plt.title("Localização de embarque")

plt.show()