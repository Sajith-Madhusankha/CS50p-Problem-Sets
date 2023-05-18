def main():
    text = input("")
    convert(text)

def convert(emote):
    emote = emote.replace(":)", "🙂")
    emote = emote.replace(":(", "🙁")
    print(emote)



main()