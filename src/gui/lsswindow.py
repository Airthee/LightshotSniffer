# *-* coding: utf8

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
import requests
from io import BytesIO
from tools import Generator
from tools import Downloader


class LssWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        self.pack()
        self.__create_widgets()
        self.__init_generator()
        self.__init_events()

    def __init_events(self):
        """
            Init all events for this widget or for the entire application
        """
        self.bind_all("<KeyPress>", self.__key_down)
        pass

    def __key_down(self, e):
        """
            Called when key is pressed in the application
            Param e is the event
        """
        upper_char = e.char.upper()

        # On press N
        if upper_char == "N":
            self.next_image()

        # On press P
        elif upper_char == "P":
            self.previous_image()

        # On press S
        elif upper_char == "S":
            self.save_image()

    def __close(self):
        """
            Close the window
        """
        self.master.destroy()

    def __create_widgets(self):
        """
            Create all widgets for this window
        """
        # Create frame form
        self.frame_settings = tk.Frame(self)
        self.frame_settings.input_start = tk.Entry(self.frame_settings)
        self.frame_settings.input_start.pack(side="left")
        self.frame_settings.input_start.focus_set()
        self.frame_settings.input_end = tk.Entry(self.frame_settings)
        self.frame_settings.input_end.insert(0, "000000")
        self.frame_settings.input_end.pack(side="left")
        self.frame_settings.button_save = tk.Button(
            self.frame_settings, text="Enregistrer", command=self.save_settings
        )
        self.frame_settings.button_save.pack(side="left")
        self.frame_settings.pack()

        #  Create canvas
        self.canvas = tk.Canvas(self, width=700, height=500, bg="ivory")
        self.photo = self.url_to_photoimage(
            "https://via.placeholder.com/700x500/O%20https://placeholder.com/"
        )
        self.canvas.image_on_canvas = self.canvas.create_image(
            0, 0, anchor=tk.NW, image=self.photo
        )
        self.canvas.pack()

        # Add buttons
        self.frame_buttons = tk.Frame(self)
        self.frame_buttons.button_previous = tk.Button(
            self.frame_buttons, text="Previous", command=self.previous_image
        )
        self.frame_buttons.button_previous.pack(side="left")
        self.frame_buttons.button_save = tk.Button(
            self.frame_buttons, text="Save", command=self.save_image
        )
        self.frame_buttons.button_save.pack(side="left")
        self.frame_buttons.button_next = tk.Button(
            self.frame_buttons, text="Next", command=self.next_image
        )
        self.frame_buttons.button_next.pack(side="left")
        self.frame_buttons.pack()

    def __init_generator(self):
        """
            Init the generator according to input fields values
            Attach the generator to current window
        """
        self.generator = Generator(
            self.frame_settings.input_start.get(), self.frame_settings.input_end.get()
        )

    def previous_image(self):
        """
            Display previous image according to the generator
        """
        if self.check_settings():
            print("previous !")
            self.generator.previous()
            try:
                self.preview_image()
            except requests.exceptions.MissingSchema:
                self.previous_image()

    def next_image(self):
        """
            Display next image according to the generator
        """
        if self.check_settings():
            print("next !")
            self.generator.next()
            try:
                self.preview_image()
            except requests.exceptions.MissingSchema:
                self.next_image()

    def save_image(self):
        """
            Save displayed image to the file system
        """
        if self.check_settings():
            print("save !")

    def preview_image(self):
        """
            Display the current image into the canvas
        """
        image_id = self.generator.value()
        image_url = Downloader.get_url_by_id(image_id)
        print("URL : {}".format(image_url))
        self.display_image_from_url(image_url)

    def save_settings(self):
        """
            Apply input fields values to the generator
            Preview the image
        """
        if self.check_settings():
            self.__init_generator()
            self.preview_image()

    def check_settings(self):
        """
            Check input fields values, if at least one is empty, display alert
        """
        if (
            self.frame_settings.input_start.get() != ""
            and self.frame_settings.input_end.get() != ""
        ):
            return True
        else:
            messagebox.showwarning(
                "Paramètres invalides", "Un des paramètres est invalide"
            )
            return False

    def url_to_photoimage(self, url):
        """
            Return ImageTk from the url passed in parameter
        """
        image = Image.open(BytesIO(requests.get(url).content))
        image.resize((700, 500), Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)

    def display_image_from_url(self, url):
        """
            Display the image from url to the canvas
        """
        self.photo = self.url_to_photoimage(url)
        self.canvas.itemconfig(self.canvas.image_on_canvas, image=self.photo)
