from flask import Flask, render_template

app = Flask(name)

@app.route('/fizzbuzz')
def fizzbuzz():
    numbers = list(range(1, 101))  # Generate a list of numbers from 1 to 100
    fizzbuzz_list = []  # Create an empty list to store the FizzBuzz outputs
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            fizzbuzz_list.append('FizzBuzz')
        elif num % 3 == 0:
            fizzbuzz_list.append('Fizz')
        elif num % 5 == 0:
            fizzbuzz_list.append('Buzz')
        else:
            fizzbuzz_list.append(num)
    return render_template('fizzbuzz.html', fizzbuzz_list=fizzbuzz_list