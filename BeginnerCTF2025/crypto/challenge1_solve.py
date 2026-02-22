g = 2
p = int(input("p: "))
public = int(input("public: "))

for guess in range(p):
    if pow(g, guess, p) == public:
        print(f"secret: {guess}")
        exit(1)
