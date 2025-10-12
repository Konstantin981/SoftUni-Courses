electrons = int(input())
current_layer = 0
layers = []
while electrons > 0:
    current_layer += 1
    electrons_in_layer = 2*(current_layer**2)
    if electrons_in_layer > electrons:
        electrons_in_layer = electrons
    layers.append(electrons_in_layer)
    electrons -= electrons_in_layer
print(layers)