# 8.9-8.11
msg = ['Did you go to the store?', 'Yes', 'Did you get milk?', 'No', 'Could you get some?', 'Ok']
def show_messages(msgs):
    for msg in msgs:
        print(msg)

show_messages(msg)

print('\n')

def send_message(msg, sent_messages):
    while msg:
        sending = msg.pop(0)
        print(f"sending text: {sending}")
        sent_messages.append(sending)


msg = ['Did you go to the store?', 'Yes', 'Did you get milk?', 'No', 'Could you get some?', 'Ok']
sent_messages = []

send_message(msg[:], sent_messages)
print(f'msg list: {msg}')
print(f'sent_messages list: {sent_messages}')