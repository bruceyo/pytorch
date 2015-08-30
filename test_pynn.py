from __future__ import print_function
import PyTorch
import array
import numpy

A = numpy.random.rand(6).reshape(2,3).astype(numpy.float32)

tensorA = PyTorch.asTensor(A)

nn = PyTorch.Nn()
linear = nn.Linear(3, 8)
linear.updateOutput(tensorA)
output = linear.getOutput()
print('output', output)

