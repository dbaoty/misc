
def decode(message_file):
    messages = []
    with open(message_file) as message_file:
        for message in message_file:
            (line_no, word) = message.split()
            line_no = int(line_no)
            word = word.strip()

            messages.append([line_no, word])
    
    messages.sort()
    
    decoded_string = ""
    step = 1
    while step <= len(messages):
        decoded_string += (str(messages[:step][step - 1][1]))
        decoded_string += " "
        messages = messages[step:]
        step += 1

    return decoded_string


if __name__ == "__main__":
    print(decode("message_file.txt"))
