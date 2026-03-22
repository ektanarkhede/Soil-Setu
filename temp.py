import h5py
f = h5py.File("models/DL_models/strawberry_model.h5", "r")
print(f.attrs["keras_version"])
print(f.attrs["backend"])
