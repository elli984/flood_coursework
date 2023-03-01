def polyfit(dates, levels, p):
    import numpy as np
    import matplotlib.dates

    x = matplotlib.dates.date2num(dates)
    y = levels

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(x-x[-1], y, p)

    # Convert coefficient into a polynomial that can be evaluated,
    poly = np.poly1d(p_coeff)

    output1 = (poly, x[-1])

    return output1

