for i in range(1, 101):
    # 現在の変数iの値を表示
    print(i)
    # iが3の倍数の場合、Fizzと表示
    if i % 3 == 0:
        print("Fizz")
    # iが5の倍数の場合、Buzzと表示
    if i % 5 == 0:
        print("Buzz")
    # iが3の倍数、かつ5の倍数の場合、FizzBuzzと表示
    if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
