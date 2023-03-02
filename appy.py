from PIL import Image, ImageDraw, ImageFont
import random

# lista de caracteres permitidos no CAPTCHA
captcha_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# gera um novo CAPTCHA aleatório
def generate_captcha():
    captcha = ""
    for i in range(6): # define um CAPTCHA com 6 caracteres
        captcha += random.choice(captcha_chars) # escolhe um caractere aleatório

    # cria uma nova imagem com tamanho 200x80 e fundo branco
    image = Image.new('RGB', (200, 80), (255, 255, 255))

    # adiciona o texto do CAPTCHA à imagem com uma fonte aleatória
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 36)
    for i in range(len(captcha)):
        x = random.randint(10, 40) + i * 30
        y = random.randint(10, 40)
        draw.text((x, y), captcha[i], font=font, fill=(0, 0, 0))

    # adiciona linhas aleatórias à imagem
    for i in range(random.randint(2, 5)):
        x1 = random.randint(0, 200)
        y1 = random.randint(0, 80)
        x2 = random.randint(0, 200)
        y2 = random.randint(0, 80)
        draw.line((x1, y1, x2, y2), fill=(0, 0, 0), width=1)

    # salva a imagem em disco
    image.save('captcha.png')

    return captcha

# declarando variavel
def check_captcha(user_input, captcha):
    return user_input.lower() == captcha.lower() # compara sem diferenciar maiúsculas e minúsculas

# exemplo de uso
captcha = generate_captcha()
print("Digite o seguinte CAPTCHA:")
print("![Captcha Image](captcha.png)")
user_input = input()
if check_captcha(user_input, captcha):
    print("CAPTCHA correto!")
else:
    print("CAPTCHA incorreto.")
