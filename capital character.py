def capitalize_lines():
    while True:
        try:
            line = input()
            print(line.upper())
        except EOFError:
            break

capitalize_lines()