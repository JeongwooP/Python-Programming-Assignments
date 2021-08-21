def security(password):
    if len(password)>=9:
        message='Good'
    elif len(password)<9 & len(password)>=5:
        message='Normal'
    else:
        message='Bad'
    return print(message)

ps=input('패스워드를 입력하시오:')
security(ps)
    
