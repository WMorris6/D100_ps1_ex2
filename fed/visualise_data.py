import matplotlib.pyplot as plt
import seaborn as sns

def plot_gdp(df, value_col="gdp_trillions"):
    """
    Plot GDP over time for multiple countries.
    """
    plt.figure(figsize=(10,6))
    sns.lineplot(data=df, x="year", y=value_col, hue="country", marker="o")
    plt.title("GDP (Trillions of USD), 2000–2022")
    plt.xlabel("Year")
    plt.ylabel("GDP (Trillions USD)")
    plt.tight_layout()
    plt.show()