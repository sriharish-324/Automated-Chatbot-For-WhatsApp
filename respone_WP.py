def response(input_message):
    message = input_message.lower()

    if message == '1':
        return 'noted'

    elif message == '0':
        return 'ok call me after'
    else:
        return ' I am A automated bot.. He is on Driving If it is an emergency Send me 1 I will acknowledge Him else Send me 0 '