import random
import os
import shutil
import requests
import tkinter as tk
import pygame
from PIL import Image, ImageTk
import psutil
import ttkbootstrap as ttk


def get_drive_with_most_space():
    partitions = psutil.disk_partitions()
    max_free_space = 0
    best_drive = None

    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            if usage.free > max_free_space:
                max_free_space = usage.free
                best_drive = partition.mountpoint
        except PermissionError:
            continue

    return best_drive if best_drive else "C:/"


best_drive = get_drive_with_most_space()
folder_path = os.path.join(best_drive, "Zgadywanie")


url = "https://kropa.pl/data/gfx/pictures/large/7/4/110147_1.jpg"
music_path = "D:/music/papiez.mp3"
source_image = os.path.join(folder_path, "obraz.jpg")
gif_path = "D:/papiez.gif"


pygame.mixer.init()


incorrect_attempts = 0


def start_game():
    global number, attempts, incorrect_attempts
    incorrect_attempts = 0
    attempts = 0


    if os.path.exists(music_path):
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
    else:
        print("Plik muzyczny nie istnieje!")


    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


    if not os.path.exists(source_image):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(source_image, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
        else:
            print("Nie udało się pobrać obrazu!")
            return


    number = random.randint(1, 1000)
    feedback_label.config(text="Zgadnij liczbę od 1 do 1000!")


def check_guess():
    global attempts, incorrect_attempts


    user_input = guess_var.get()
    if user_input.isdigit():
        guess = int(user_input)
        incorrect_attempts = 0
    else:
        incorrect_attempts += 1
        if incorrect_attempts >= 4:
            feedback_label.config(
                text=f"Niepoprawny format bakłażanie, \n python się na ciebie obraził: \n {len(user_input)} ", justify="center"
            )
        else:
            feedback_label.config(text="Proszę podać prawidłową liczbę!", justify="center")
        return


    attempts += 1


    if guess == number:
        feedback_label.config(text=f"Brawo! Zgadłeś w {attempts} próbach.", justify="center")
        pygame.mixer.music.stop()  # Stop music
        ask_play_again()
    elif guess > number:
        feedback_label.config(text="Za dużo! Spróbuj ponownie.")
    elif guess < number:
        feedback_label.config(text="Za mało! Spróbuj ponownie.")


    image_path = os.path.join(folder_path, f"papaj{attempts}.jpg")
    shutil.copyfile(source_image, image_path)


def ask_play_again():
    def play_again():

        start_game()
        play_again_popup.destroy()

    def exit_game():

        root.destroy()

    play_again_popup = tk.Toplevel(root)
    play_again_popup.geometry("300x200")
    play_again_popup.title("Play Again?")
    play_again_popup.resizable(False, False)

    label = ttk.Label(play_again_popup, text="Czy chcesz zagrać ponownie?", font=("Arial", 14))
    label.pack(pady=20)

    play_again_btn = ttk.Button(play_again_popup, text="Zagraj ponownie", command=play_again, style="success.TButton")
    play_again_btn.pack(pady=5)

    exit_btn = ttk.Button(play_again_popup, text="Wyjdź z gry", command=exit_game, style="danger.TButton")
    exit_btn.pack(pady=5)


root = ttk.Window(themename="darkly")
root.geometry("500x600")
root.title("Zgadywanie liczb")


try:
    gif = Image.open(gif_path)
    frames = []

    for frame in range(getattr(gif, "n_frames", 1)):
        gif.seek(frame)
        frames.append(ImageTk.PhotoImage(gif.copy()))

    if len(frames) > 1:
        gif_label = ttk.Label(root)
        gif_label.pack()

        def update_frame(index):
            frame = frames[index]
            gif_label.configure(image=frame)
            root.after(100, update_frame, (index + 1) % len(frames))

        update_frame(0)
    else:
        gif_label = ttk.Label(root, image=frames[0])
        gif_label.pack()

except Exception as e:
    print("Błąd przy otwieraniu pliku GIF:", e)
    gif_label = ttk.Label(root, text="Nie udało się wczytać GIF-a")
    gif_label.pack()

# Game UI
feedback_label = ttk.Label(root, text="Kliknij 'Start', aby rozpocząć grę!", font=("Arial", 14) , justify="center")
feedback_label.pack(pady=10)

guess_var = tk.StringVar()
guess_entry = ttk.Entry(root, textvariable=guess_var, font=("Arial", 14))
guess_entry.pack(pady=5)

submit_btn = ttk.Button(root, text="Zgadnij", command=check_guess, style="success.TButton")
submit_btn.pack(pady=5)

start_btn = ttk.Button(root, text="Start", command=start_game, style="primary.Outline.TButton")
start_btn.pack(pady=10)


root.mainloop()
