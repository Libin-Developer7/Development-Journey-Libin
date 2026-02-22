def register_check(register):
    return list(register.values()).count('yes')

register = {'Michael':'yes','John':'no','Peter':'yes','Mary':'yes'}
print(register_check(register))