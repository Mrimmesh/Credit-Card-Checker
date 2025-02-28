from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# Card Validation Function
def validate_card_number(num):
    num = num.replace(" ", "").replace("-", "")  # Remove spaces and dashes
    num = num[::-1]  # Reverse the number

    sum_odd = sum(int(x) for x in num[::2])
    sum_even = sum((int(x) * 2 - 9) if (int(x) * 2 > 9) else (int(x) * 2) for x in num[1::2])

    return (sum_odd + sum_even) % 10 == 0

@app.route("/")
def index():
    return render_template("index.html")

# Handling Card Submission
@app.route("/verify", methods=["POST"])
def verify_card():
    card_number = request.form.get("card_number")
    is_valid = validate_card_number(card_number)

    if is_valid:
        return redirect(url_for('valid'))  # Redirect to valid.html if valid
    else:
        return redirect(url_for('invalid'))  # Redirect to invalid.html if invalid

@app.route("/valid")
def valid():
    return render_template("valid.html")  # Return valid HTML page

@app.route("/invalid")
def invalid():
    return render_template("invalid.html")  # Return invalid HTML page

if __name__ == "__main__":
    app.run(debug=True)
