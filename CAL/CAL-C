import pylab

theta = pylab.linspace(-pylab.pi/3, pylab.pi/3, 1000)
tan_graph = pylab.tan(theta)

pylab.plot(theta, tan_graph, label = "$tan(x)$")
pylab.xlabel("$x$")
pylab.ylabel("$y$")

pn_range = pn(1, theta)
pylab.plot(theta, pn_range, label = "$p_1(x)$")

pn_range2 = pn(2, theta)
pylab.plot(theta, pn_range2, label = "$p_2(x)$")

pn_range3 = pn(3, theta)
pylab.plot(theta, pn_range3, label = "$p_3(x)$")

pylab.legend(loc = "upper left")
pylab.title("GRAPHS OF PN AND TANGENT")

pylab.savefig("outputimage.png")
