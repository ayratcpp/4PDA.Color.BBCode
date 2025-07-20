import os

print("4PDA.Color.BBCode")
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def rainbow_bbcode(text):
    colors = ['red', '#FFA500', 'yellow', 'green', 'blue', '#800080']
    result = []
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        result.append(f"[color={color}]{char}[/color]")
    return ''.join(result)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def interpolate_color(c1, c2, factor: float):
    return tuple(int(a + (b - a) * factor) for a, b in zip(c1, c2))

def gradient_bbcode(text, start_color, end_color):
    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)
    length = len(text)
    result = []
    for i, char in enumerate(text):
        factor = i / max(length - 1, 1)
        rgb = interpolate_color(start_rgb, end_rgb, factor)
        hex_color = rgb_to_hex(rgb)
        result.append(f"[color={hex_color}]{char}[/color]")
    return ''.join(result)

def main():
    while True:
        print("\nВыбери опцию:")
        print("1 - Радужный текст")
        print("2 - Градиентный текст")
        print("3 - Очистка экрана")
        print("4 - Выход")
        choice = input("Номер опции: ").strip()

        if choice == '1':
            text = input("Текст для оформления: ")
            print("\nРезультат:")
            print(rainbow_bbcode(text))
        elif choice == '2':
            text = input("Текст для оформления: ")
            start = input("HEX-цвет начала (например, #FF0000): ").strip()
            end = input("HEX-цвет конца (например, #0000FF): ").strip()
            print("\nРезультат (bbcode):")
            print(gradient_bbcode(text, start, end))
        elif choice == '3':
            clear_screen()
        elif choice == '4':
            print("Выход.")
            break
        else:
            print("Неверная опция! Введите что то другое..")

if __name__ == "__main__":
    main()
