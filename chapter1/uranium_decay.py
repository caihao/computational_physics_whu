#!/usr/bin/env python
# encoding: utf-8

from pylab import *
import pickle

n_uranium = []
t = []
tau = 0
dt = 0
n = 0

def initialize(n_uranium, t, _tau, _dt, _n):
    global tau, dt, n
    print "initial number of nuclei -> ",
    n_uranium.append(float(raw_input()))
    print "time constant -> ",
    tau = float(raw_input())
    print "time step -> ",
    dt = float(raw_input())
    print "total time -> ",
    time = float(raw_input())
    t.append(0)
    n = int(time / dt)
    return 0

def calculate(n_uranium, t, tau, dt, n):
    print n_uranium
    print t
    print tau
    print dt
    print n
    for i in range(1, n):
        n_uranium.append(n_uranium[i - 1] - n_uranium[i - 1] / tau * dt)
        t.append(t[i - 1] + dt)
    return 0

def store(n_uranium, t, n):
    mfile = open("notes.txt", "a")
    for i in range(n):
        print >> mfile, t[i], n_uranium[i]
    mfile.close()

    pickle_file = open("pickled_data.pkl", "w")
    pickle.dump(t, pickle_file)
    pickle.dump(n_uranium, pickle_file)

    return 0

def read():
    pickle_file = open("pickled_data.pkl", "r")
    t = pickle.load(pickle_file)
    n_uranium = pickle.load(pickle_file)
    print t
    print n_uranium

initialize(n_uranium, t, tau, dt, n)
calculate(n_uranium, t, tau, dt, n)
store(n_uranium, t, n)

plot(t, n_uranium, '--*')
# scatter(t, n_uranium)
show()
savefig("test_.jpg")

read()


