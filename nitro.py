import random
import string
import requests

def generate_nitro_code():
    alphabet = string.ascii_letters + string.digits
    code = ''.join(random.choice(alphabet) for _ in range(16))
    return f"https://discord.gift/{code}"

def is_valid_nitro_code(code):
    response = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}")
    return response.status_code == 200

def main():
    num_codes = 999999  # Вы можете изменить это значение, чтобы сгенерировать больше или меньше кодов.

    with open('work.txt', 'w') as work_file, open('not_work.txt', 'w') as not_work_file:
        for _ in range(num_codes):
            code = generate_nitro_code()
            if is_valid_nitro_code(code):
                work_file.write(f"{code}\n")
            else:
                not_work_file.write(f"{code}\n")

if __name__ == "__main__":
    main()
