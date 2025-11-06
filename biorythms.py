import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
df = pd.read_csv("biorythms_students.csv")

# Настройки визуализации
sns.set(style="whitegrid", font="Times New Roman", font_scale=1.2)

# --- График 1: Тест Купера утром и вечером ---
plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x="session_time", y="cooper_distance", palette="pastel")
plt.title("Результаты теста Купера в зависимости от времени суток")
plt.xlabel("Время занятий")
plt.ylabel("Дистанция (м)")
plt.savefig("plot_cooper_by_time_of_day.png", dpi=300, bbox_inches="tight")
plt.close()

# --- График 2: Влияние индекса согласованности биоритмов ---
plt.figure(figsize=(7, 5))
sns.regplot(data=df, x="alignment_index", y="cooper_distance",
            scatter_kws={"alpha": 0.6}, line_kws={"color": "red"})
plt.title("Связь согласованности биоритмов с результатом теста Купера")
plt.xlabel("Индекс согласованности биоритмов")
plt.ylabel("Дистанция (м)")
plt.savefig("plot_alignment_vs_cooper.png", dpi=300, bbox_inches="tight")
plt.close()

# --- График 3: Совпадение хронотипа и времени занятий ---
plt.figure(figsize=(7, 5))
sns.barplot(data=df, x="match_chronotype", y="reaction_time", palette="pastel", ci="sd")
plt.title("Влияние совпадения хронотипа и времени занятий на скорость реакции")
plt.xlabel("Совпадение хронотипа (0 — нет, 1 — да)")
plt.ylabel("Время реакции (мс)")
plt.savefig("plot_reaction_chronotype.png", dpi=300, bbox_inches="tight")
plt.close()

print("Графики сохранены как:")
print("plot_cooper_by_time_of_day.png")
print("plot_alignment_vs_cooper.png")
print("plot_reaction_chronotype.png")
