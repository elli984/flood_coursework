def plot_water_levels(station, dates, levels):
    import matplotlib.pyplot as plt

    t = dates
    level = levels

    # Plot
    plt.plot(t, level)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p): 
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib

    x = matplotlib.dates.date2num(dates)
    y = levels

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(x-x[-1], y, p)

    # Convert coefficient into a polynomial that can be evaluated,
    poly = np.poly1d(p_coeff)

    # Plot original data points
    plt.plot(x-x[-1], y, '.')

    # Plot polynomial fit at 30 points along interval
    x1 = np.linspace(x[-1], x[0], 100)
    plt.plot(x1-x[-1], poly(x1-x[-1]))


    tp = station.typical_range
    y1 = []
    y2 = []
    for n in range(len(x1)):
        y1.append(tp[0])
        y2.append(tp[1])

    plt.plot(x1-x[-1],y1,linestyle='dashed',label = 'typical range low')
    plt.plot(x1-x[-1],y2,linestyle='dashed',label = 'typical range high')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('time minus time shift')
    plt.ylabel('water level (m)')
    plt.title(station.name)
    plt.legend()
    
    # Display plot
    plt.show()
