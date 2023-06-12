def fonts(value, color:str="", style:str=""):
    color, style = color.lower(), style.lower()
    fmt = {
        "reset" : "\033[0m",
        "bold" : "\033[1m",
        "italic" : "\033[3m",
        "underline" : "\033[4m",
        ""        :        "",
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "orange": "\033[38;2;255;165;0m",
        "pink": "\033[38;2;255;105;180m",
        "purple": "\033[38;2;128;0;128m",
        "sky": "\033[38;2;135;206;250m",
        "teal": "\033[38;2;0;128;128m",
        "lime": "\033[38;2;0;255;0m",
        "brown": "\033[38;2;165;42;42m",
    }
    return f"{fmt[style]}{fmt[color]}{value}{fmt['reset']}"

def input_email(prompt):
    while True:
        try:
            user_input = input(prompt)
            if len(user_input) == 0:
                raise ValueError("Email tidak boleh kosong.")
            elif not user_input.lower().endswith(("gmail.com", "yahoo.com", "outlook.com")):
                raise ValueError("Email tidak valid. Email harus diakhiri dengan gmail.com, yahoo.com, atau outlook.com.")
            return user_input
        except ValueError as error:
            print(f"Error: {str(error)}")
            continue
        
def input_pw(prompt):
    count = 0
    while True: 
        try:
            if count == 3:
                print("Kamu gagal login")
                break
            count += 1
            pw = input(f"Masukkan Password  : ")
            assert len(pw) == 5, "Password harus terdiri dari 5 digit."
            with open('Daftar akun.txt', 'r') as file:
                for line in file:
                    data = line.strip().split(",")
                    if data[1] == pw:
                        print("Selamat Anda sudah login")
                        return
            raise AssertionError("Password salah!")
        except AssertionError as error:
            print(error)

