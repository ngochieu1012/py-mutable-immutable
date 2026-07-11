lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {
    "John": 4,
    "Sergio": 3,
}
collection_of_coins = {1, 2, 25}

# write your code here
# Get all variables from main module
all_vars = {k: v for k, v in globals().items() 
            if not k.startswith('_') 
            and k not in ('all_vars', 'mutable', 'immutable', 'sorted_variables')}
# Separate mutable and immutable
mutable = []
immutable = []
for name, value in all_vars.items():
    if isinstance(value, (list, dict, set)):
        mutable.append(value)
    else:
        immutable.append(value)
sorted_variables = {
    "mutable": mutable,
    "immutable": immutable
}
