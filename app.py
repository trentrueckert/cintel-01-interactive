import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render


# Add page options for the overall app
ui.page_opts(title="Trent's PyShiny App with Plot", fillable=True)

# Create a sidebar woth a slider input
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 120, 30)

@render.plot(alt="A histogram showing random data distribution")
def histogram():
    count_of_points: int = 437
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    plt.hist(x, input.selected_number_of_bins(), color="red", density=True)
