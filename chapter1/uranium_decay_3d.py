#!/usr/bin/env python
# encoding: utf-8

import pylab as pl
import pickle
import visual as vs
import easygui


class Uranium:
    """
        Show the radioactive decay of U235
    """
    def __init__(self, n = 1000, tau = 1.0, dt = 0.1, time = 3.0):
        self.tau = tau
        self.dt = dt
        self.N = n
        self.time = time

    def __str__(self):
        msg = "There are %d U235 nuclei at the beginning, and the decay time constant is set to be %f"%(self.N, self.tau)
        return msg

    def calculate(self):
        self.n_uranium = []
        self.T = []
        self.n_uranium.append(self.N)
        self.T.append(0)
        nsteps = int(self.time / self.dt)
        for i in range(1, nsteps):
            self.n_uranium.append(self.n_uranium[i - 1] - self.n_uranium[i - 1] / self.tau * self.dt)
            self.T.append(self.T[i - 1] + self.dt)
        return 0

    def plot2D(self):
        pl.plot(self.T, self.n_uranium, '-*')
        pl.title("U235 Radioactive Decay")
        pl.xlabel("time")
        pl.ylabel("Number of U235 Nuclei")
        pl.show()
        savefig("radioactive_decay.jpg")

    def plot3D(self):
        axis_length = 10.0
        xaxis = vs.arrow(pos = (-5, -5, 0), axis = (axis_length, 0, 0), shaftwidth = 0.01)
        yaxis = vs.arrow(pos = (-5, -5, 0), axis = (0, axis_length, 0), shaftwidth = 0.01)
        balls = []
        for (i, j) in zip(self.n_uranium, self.T):
            balls.append(vs.sphere(pos = ((j / self.time) * axis_length * 0.9- 4.9, (i / self.N) * axis_length * 0.9 - 4.9, 0), radius = 0.2, color = vs.color.red))
        xlabel = vs.label(text = "time", pos = (5, -5, 0))
        ylabel = vs.label(text = "Number of Nuclei", pos = (-5, 5, 0))
        while 1:
            pass

    def set_parameters(self):
        self.N = float(easygui.enterbox("How many nuclei at the beginning?"))


A = Uranium(1000, 1.0, 0.1, 3)
print A.__doc__
print A

A.set_parameters()

A.calculate()
A.plot2D()

