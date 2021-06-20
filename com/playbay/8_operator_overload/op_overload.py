
class Snow:

    snowflake_amount = 0

    def __add__(self, other):
        self.snowflake_amount += other

    def __sub__(self, other):
        self.snowflake_amount -= other

    def __mul__(self, other):
        self.snowflake_amount *= other

    def __truediv__(self, other):
        self.snowflake_amount = self.snowflake_amount // other

    def __call__(self, n):
        self.snowflake_amount = n

    def make_snow(self, n):
        snw_string = ''
        for _ in range(self.snowflake_amount // n):
            snw_string += '*' * n + '\n'
        snw_string += (self.snowflake_amount % n) * '*'
        return snw_string


jaja = Snow()

jaja(23)
jaja + 42
jaja / 2
jaja(100)
print(jaja.make_snow(25))


