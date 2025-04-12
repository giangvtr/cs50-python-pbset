def convert(user_input):
    user_input = user_input.replace(":)", "🙂").replace(":(","🙁")
    return user_input
def main():
    emo = input("How are you feeling? ")
    print(convert(emo))
main()
