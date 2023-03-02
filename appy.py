import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# define a lista de caracteres permitidos no CAPTCHA
captcha_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# define a função para gerar um novo CAPTCHA
def generate_captcha():
    captcha = ""
    for i in range(6): # define um CAPTCHA com 6 caracteres
        captcha += random.choice(captcha_chars) # escolhe um caractere aleatório
    return captcha

# define a função para criar uma imagem do CAPTCHA com distorção
def create_image(captcha):
    width = 200 # define a largura da imagem
    height = 80 # define a altura da imagem
    image = Image.new('RGB', (width, height), (255, 255, 255)) # cria uma nova imagem em branco
    font = ImageFont.truetype('arial.ttf', 50) # define a fonte e o tamanho do texto
    draw = ImageDraw.Draw(image) # cria um objeto para desenhar na imagem
    # desenha cada caractere do CAPTCHA com uma cor e posição aleatória
    for i, char in enumerate(captcha):
        x = 40 * i + random.randint(-10, 10) # posição horizontal aleatória com distorção
        y = random.randint(10, 30) # posição vertical aleatória
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # cor aleatória
        draw.text((x, y), char, font=font, fill=color) # desenha o caractere na imagem
    # adiciona distorção à imagem
    image = image.filter(ImageFilter.GaussianBlur(radius=2)) # adiciona um filtro de desfoque gaussiano
    image = image.transform((width + 20, height + 10), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0), Image.BICUBIC) # adiciona uma transformação afim
    return image

# define a função para verificar se o usuário inseriu o CAPTCHA corretamente
def check_captcha(user_input, captcha):
    return user_input.lower() == captcha.lower() # compara sem diferenciar maiúsculas e minúsculas

# exemplo de uso
captcha = generate_captcha()
image = create_image(captcha)
image.show() # exibe a imagem do CAPTCHA
user_input = input("Digite o CAPTCHA: ")
if check_captcha(user_input, captcha):
    print("CAPTCHA correto!")
else:
    print("CAPTCHA incorreto.")