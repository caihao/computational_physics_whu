N_U = []
t = []
tau = 10
dt = 0.1
N_U.append(1000.)
t.append(0)
end_time = 20

for i in range(int(end_time / dt)):
	tmp = N_U[i] - N_U[i] / tau * dt
	N_U.append(tmp)
	t.append(dt * (i + 1))
	print t[-1], N_U[-1]

