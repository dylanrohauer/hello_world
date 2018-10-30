# testing mathematics
from matplotlib import pyplot as plt
import numpy as np

fig, (ax_1) = plt.subplots(1,1)

fig.suptitle("MATH CHARTS")

def plug_axes(axe,x, y, z, a):
    """Take 3 ARGVS:
    axe - represents an axe that's apart of the
    x - an array of numbers representing the x values
    y - an array of numbers representing the y values
    extra_dict - assigns any extra attributes the plotter might want
    """
    axe.plot(x,y,z,label=a)

def get_inputs():
    print("Please write your answer in this form:")
    print("y=mx+b")

    ipt = input("What y intercept graph would you like to map? ")
    # gets rid of y and =
    lst = ipt.split('=')
    # captures last part of the sequence mx+b
    nums = lst[-1]
    # vertval becomes b in str form
    # numx becomes mx in str form
    vert_val = nums.split("+")
    # xmult is the mx without b
    xmult = vert_val.pop(0)
    # x_mlt is the mulitplyer of x
    x_lst = xmult.split("x")
    x_mlt = x_lst[0]
    x_flt = float(x_mlt)
    # b_val is the true value of b
    b = vert_val[0]
    b_val = float(b)

    return(x_flt, b_val)

x_1, b_1 = get_inputs()

x_ray = np.arange(-10,10,0.1)
y_1 = (x_1 * x_ray) + b_1

y_2 = (x_ray/x_1) - (b_1/x_1)
plug_axes(ax_1, x_ray, y_1, "b", "Original")
plug_axes(ax_1, x_ray, y_2, "r", "Inverse")
ax_1.axhline(y=0, color='k', ls='--')
ax_1.axvline(x=0, color='k', ls='--')
plt.legend()
plt.show()
