for messages_count in range(0, 100):
    remainder = messages_count % 10
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif (remainder == 1) and (messages_count != 11):
        print('У вас', messages_count, 'новое сообщение')
    elif (remainder == 0) or (remainder >= 5) or ((remainder > 10) and (remainder < 20)):
        print('У вас', messages_count, 'новых сообщений')
    else:
        print('У вас', messages_count, 'новых сообщения')