import matplotlib.pyplot as plt
import pandas as pd

female_color = "#FA2379"

# read csv
df = pd.read_csv("train.csv")

# configure graph
fig = plt.figure(figsize=(18,6))
alpha = alpha_scatterplot = 0.2
alpha_bar_chart = 0.55

# survived vs deceased
fig.add_subplot(3,4,1)
df.Survived.value_counts().plot(kind='bar', alpha=alpha_bar_chart)
plt.title("Sobreviveram")

# male survived vs male deceased
fig.add_subplot(3,4,2)
df.Survived[df.Sex == "male"].value_counts().plot(kind='bar', alpha=alpha_bar_chart)
plt.title("Homens que sobreviveram")

# female survived vs female deceased
fig.add_subplot(3,4,3)
df.Survived[df.Sex == "female"].value_counts().plot(kind='bar', color=female_color, alpha=alpha_bar_chart)
plt.title("Mulheres que sobreviveram")

# gender distribution of survival
fig.add_subplot(3,4,4)
df[df.Survived == 1].Sex.value_counts().plot(kind='bar', color=[female_color, 'b'], alpha=alpha_bar_chart)
plt.title("Distribuição dos Sexos que sobreviveram")

# survival distribution within class
fig.add_subplot(3,1,2)
for x in [1,2,3]:
    df.Survived[df.Pclass == x].plot(kind="kde")
plt.title("Distribuição dos sobreviventes por classes")
plt.legend(("1 Classe", "2 Classe", "3 Classe"))

# low class male survived vs male deceased
fig.add_subplot(3,4,9)
df.Survived[(df.Sex == "male") & (df.Pclass == 3)].value_counts().plot(kind='bar', color="lightblue", alpha=alpha_bar_chart)
plt.title("Homens da Classe 3 que sobreviveram")

# high class male survived vs male deceased
fig.add_subplot(3,4,10)
df.Survived[(df.Sex == "male") & (df.Pclass == 1)].value_counts().plot(kind='bar', alpha=alpha_bar_chart)
plt.title("Homens da Classe 1 que sobreviveram")

# low class female survived vs female deceased
fig.add_subplot(3,4,11)
df.Survived[(df.Sex == "female") & (df.Pclass == 3)].value_counts().plot(kind='bar', color="pink", alpha=alpha_bar_chart)
plt.title("Mulheres da Classe 3 que sobreviveram")

# high class female survived vs female deceased
fig.add_subplot(3,4,12)
df.Survived[(df.Sex == "female") & (df.Pclass == 1)].value_counts().plot(kind='bar', color=female_color, alpha=alpha_bar_chart)
plt.title("Mulheres da Classe 1 que sobreviveram")

plt.show()