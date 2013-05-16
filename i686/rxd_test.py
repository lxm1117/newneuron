"""
to add species to plot
bring up a state axis plot from neuron gui
g=h.Graph[0]
g.addvar("calcium", ca.nodes[0]._ref_concentration)
g.addvar("calmodulin", calm.nodes[0]._ref_concentration)
g.addvar("ca-calm", cacalm.nodes[0]._ref_concentration)	

"""
from neuron import h, rxd
from matplotlib import pyplot
import numpy

h.load_file('stdrun.hoc')
h.load_file('nrngui.hoc')

#dend=h.Section() I think this is not good. because not shown in the hoc plotwhat Browser
h('create dend')
dend=h.dend
dend.nseg=2
dend.diam=1
dend.L=100
dend.insert("Ica")
dend.insert("pas")
dend.insert("hh")

dend.cao=1000 #1mM cao0_ca_ion=1000 dosen't work

stim=h.IClamp(dend(0))
stim.amp=1
stim.dur=1


diff_ca=0.005 #5nM
diff_calm=0.001

r_react=rxd.Region(h.allsec(), nrn_region='i')#geometry=rxd.Shell) #rxd.Region(sections, nrn_region, goemetry)
r_diff=rxd.Region(h.allsec())

calm=rxd.Species(r_react,diff_calm, initial=10)
ca=rxd.Species(r_react, diff_ca, name='ca', charge=2, initial=0.05)
cacalm=rxd.Species(r_react, initial=0)
reaction=rxd.Reaction(calm+ca<>cacalm,5,1)
diffusion=rxd.Rate(ca,0)

h.finitialize()



def plot_it(color='k', *arg):
	#print arg  #arg is a tuple
	y=arg[0].nodes.concentration
	x=arg[0].nodes.x
	x=dend.L*numpy.array(x)
	pyplot.plot(x,y,color)
	pyplot.xlabel("location")
	#pyplot.ylabel("[Ca2+]")

#concentration as a function of space
"""def spatialplot(t, *arg):
	n=int(t/h.dt)
	//for i in xrange(1,n):
		h.continuerun(i)
		plot_it(color='r',*arg)
	pyplot.show()
"""

