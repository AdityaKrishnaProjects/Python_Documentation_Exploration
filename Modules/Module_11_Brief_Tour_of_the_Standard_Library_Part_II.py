# # # Experiments with reprlib

# import reprlib

# i = set("aoueq9gfp9qEFHPEQFYGH9PHUFODSBVPDisbfibfpbp;")

# # The following should print the full contents of the container object
# print(repr(i))

# # The following should do the same, but abbreviate the contents
# print(reprlib.repr(i))

# # We get what we expect!

# # # Experiments with Template (submodule of string)

# from string import Template

# # We expect the following to create a template that can be substituted into 
# # using the substitute() method
# t = Template("$country_one is in conflict with ${country_two}'s people over $$1.")

# # We expect the following to substitute in the two values and then print the 
# # string
# print(t.substitute(country_one="Iran", country_two="France"))

# # We get what we expect!