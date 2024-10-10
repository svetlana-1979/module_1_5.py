immutable_var = (1, 2, 3, False, "job")
tuple_ = immutable_var
print(tuple_)
mutable_list = ['a', 'b', 'c', 'корова']
print(mutable_list)
mutable_list [3] = 'сорока'
print(mutable_list)
tuple_[4] = 'work'
print(tuple_)