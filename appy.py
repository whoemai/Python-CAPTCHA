import random

# lista de caracteres permitidos no CAPTCHA
captcha_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# gera um novo CAPTCHA aleatório
def generate_captcha():
    captcha = ""
    for i in range(6): # define um CAPTCHA com 6 caracteres
        captcha += random.choice(captcha_chars) # escolhe um caractere aleatório
    return captcha

# verifica se o usuário inseriu o CAPTCHA corretamente
def check_captcha(user_input, captcha):
    return user_input.lower() == captcha.lower() # compara sem diferenciar maiúsculas e minúsculas

# exemplo de uso
captcha = generate_captcha()
print("Digite o seguinte CAPTCHA:", captcha)
user_input = input()
if check_captcha(user_input, captcha):
    print("CAPTCHA correto!")
else:
    print("CAPTCHA incorreto.")
