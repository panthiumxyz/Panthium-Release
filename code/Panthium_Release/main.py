import customtkinter
import os
from PIL import Image
from ctypes import windll, Structure, c_long, byref
import webbrowser
from win32con import *
import multiprocessing
import subprocess as sp

# get mouse position for future reference


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


# start the class for the window
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        if not os.path.exists("configs"):
            os.makedirs("configs")

        if not os.path.exists("configs/default.ini"):
            fo = open(fr"configs/default.ini", "w")
            fo.close()

        # set random variables
        global fov_toggled
        fov_toggled = False

        self.attributes('-topmost', True)
        self.overrideredirect(True)

        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("green")

        self.title("DO - NOT - SHARE")
        self.geometry("600x500")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        keys = {
            'Left Mouse': "0x01",
            'Right Mouse': "0x02",
            'Mouse 4': "0x05",
            'Mouse 5': "0x06",
        }

        # define all the functions for the buttons in the UI
        def move_toggle():
            global move_toggle_val
            move_toggle_val = self.Global_Move_Button.get()

            if move_toggle_val == 1:
                self.bind('<B1-Motion>', move)

                if move_toggle_val == 0:
                    return

        def move(event):
            if move_toggle_val == 0:
                return

            else:
                pt = POINT()
                windll.user32.GetCursorPos(byref(pt))
                self.geometry(f"+{pt.x}+{pt.y}")
                print("window >", self.winfo_x(), self.winfo_y())
                print("cursor >", pt.x, pt.y, "\n")

        global extInsta
        extInsta = None

        def Instalock_On():
            global extInsta
            instalockval = self.InstalockToggle.get()

            if instalockval == 1:
                instalockval = "normal"
                self.InstalockChoose.configure(state=instalockval)
                self.InstalockApply.configure(state=instalockval)

                extInsta = sp.Popen(['python', 'utils/instalocker.py',
                                     str(self.InstalockChoose.get()),
                                     ])

            elif instalockval != 1 and extInsta is not None:

                sp.Popen("TASKKILL /F /PID {pid} /T".format(pid=extInsta.pid))
                extInsta = None

            if instalockval == 0:
                instalockval = "disabled"
                self.InstalockChoose.configure(state=instalockval)
                self.InstalockApply.configure(state=instalockval)

        def Instalock_Apply():
            self.InstalockToggle.toggle()
            self.InstalockToggle.toggle()

        def Smooth_val(val):
            val = round(val)
            self.Smoothing_Title.configure(text=f"Smoothing - {val}%")

        def FOV_val(val):
            val = round(val)
            self.FOV_Title.configure(text=f"FOV - {val} x {val}px")

        def Threshhold_val(val):
            val = round(val)
            self.Threshhold_Title.configure(text=f"Threshhold - {val}")

        def sensitivity_val(val):
            val = round(val)
            self.sensitivity_title.configure(text=f"Sensitivity - {val}%")

        def discord():
            webbrowser.open('https://panthium.xyz/')

        def force_quit():
            if self.Aimbot_Enabled.get() == 1:
                self.Aimbot_Enabled.toggle()
            exit()

        global apply_check
        apply_check = 0

        global extProc
        extProc = None

        def Aim_On():
            global extProc
            aimbval = self.Aimbot_Enabled.get()
            if aimbval == 1:
                aimbval = "normal"
                self.FOV_Slider.configure(state=aimbval)
                self.FOV_Title.configure(state=aimbval)
                self.Smoothing_Slider.configure(state=aimbval)
                self.Smoothing_Title.configure(state=aimbval)
                self.Aimbot_Key.configure(state=aimbval)
                self.Threshhold_Slider.configure(state=aimbval)
                self.Threshhold_Title.configure(state=aimbval)
                self.Aimbone.configure(state=aimbval)
                self.alt_aimbone.configure(state=aimbval)
                self.BhopToggle.configure(state=aimbval)
                self.Accelerate.configure(state=aimbval)
                self.sensitivity_slider.configure(state=aimbval)
                self.sensitivity_title.configure(state=aimbval)
            else:
                aimbval = "disabled"
                self.FOV_Slider.configure(state=aimbval)
                self.FOV_Title.configure(state=aimbval)
                self.Smoothing_Slider.configure(state=aimbval)
                self.Smoothing_Title.configure(state=aimbval)
                self.Aimbot_Key.configure(state=aimbval)
                self.Threshhold_Slider.configure(state=aimbval)
                self.Threshhold_Title.configure(state=aimbval)
                self.Aimbone.configure(state=aimbval)
                self.alt_aimbone.configure(state=aimbval)
                self.BhopToggle.configure(state=aimbval)
                self.Accelerate.configure(state=aimbval)
                self.sensitivity_slider.configure(state=aimbval)
                self.sensitivity_title.configure(state=aimbval)


            if self.Aimbot_Enabled.get() == 1:

                extProc = sp.Popen(['python', 'utils/aimbot.py',
                                    str(int(self.Smoothing_Slider.get())),
                                    str(int(self.FOV_Slider.get())),
                                    keys[self.Aimbot_Key.get()],
                                    self.Aimbone.get(),
                                    str(int(self.Threshhold_Slider.get())),
                                    str(self.BhopToggle.get()),
                                    str(self.alt_aimbone.get()),
                                    str(self.Triggerbot_enabled.get()),
                                    keys[self.triggerbot_key.get()],
                                    str(self.alt_aimbone.get()),
                                    str(self.alt_aimbone_select.get()),
                                    str("0"),
                                    str(self.Trigger_type.get()),
                                    str(self.Accelerate.get()),
                                    str(int(self.sensitivity_slider.get()))
                                    ])

            elif self.Aimbot_Enabled.get() != 1 and extProc is not None:
                sp.Popen("TASKKILL /F /PID {pid} /T".format(pid=extProc.pid))
                extProc = None

        def apply_aim():
            self.Aimbot_Enabled.toggle()
            self.Aimbot_Enabled.toggle()

        def alt_aimbone_enable():
            alt_aimbval = self.alt_aimbone.get()
            if alt_aimbval == 1:
                alt_aimbval = "normal"
                self.alt_aimbone_select.configure(state=alt_aimbval)
                self.Alt_Aimbot_Key.configure(state=alt_aimbval)
            else:
                alt_aimbval = "disabled"
                self.alt_aimbone_select.configure(state=alt_aimbval)
                self.Alt_Aimbot_Key.configure(state=alt_aimbval)
            print(self.Aimbot_Enabled.get())

        def Trigger_On():
            triggerval = self.Triggerbot_enabled.get()
            if triggerval == 1:
                triggerval = "normal"
                self.triggerbot_key.configure(state=triggerval)
                self.triggerbot_key.configure(state=triggerval)
                self.Trigger_type.configure(state=triggerval)
            else:
                triggerval = "disabled"
                self.triggerbot_key.configure(state=triggerval)
                self.triggerbot_key.configure(state=triggerval)
                self.Trigger_type.configure(state=triggerval)

            # ------------------ CONFIG STUFF ------------------ #

        def Create_config():

            config_name = self.ConfigInput.get()

            if not os.path.exists("configs"):

                os.makedirs("configs")

            if config_name != "":

                if not os.path.exists(fr"configs/{config_name}.ini"):

                    fo = open(fr"configs/{config_name}.ini", "w")
                    fo.close()

                    self.ConfigList.configure(values=os.listdir("configs"))
                    self.ConfigList.set(f"{config_name}.ini")

        def Delete_config():

            config_name = self.ConfigList.get()

            if config_name == "default.ini":
                return

            if not os.path.exists("configs"):
                os.makedirs("configs")

            if os.path.exists(fr"configs/{config_name}"):

                os.remove(fr"configs/{config_name}")

                self.ConfigList.configure(values=os.listdir("configs"))
                self.ConfigList.set(os.listdir("configs")[0])

        # load images with light and dark mode image
        # image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"Assets")

        self.aim_image = customtkinter.CTkImage(light_image=Image.open(os.path.join("imgs/aimlogoLIGHT.png")),
                                                dark_image=Image.open(os.path.join("imgs/aimlogoDARK.png")), size=(50, 50))
        self.aim_misc_image = customtkinter.CTkImage(light_image=Image.open(os.path.join("imgs/miscaimLIGHT.png")),
                                                     dark_image=Image.open(os.path.join("imgs/miscaimDARK.png")), size=(50, 50))
        self.visuals_image = customtkinter.CTkImage(light_image=Image.open(os.path.join("imgs/visualsLIGHT.png")),
                                                    dark_image=Image.open(os.path.join("imgs/visualsDARK.png")), size=(50, 50))
        self.gen_image = customtkinter.CTkImage(light_image=Image.open(os.path.join("imgs/generallogoLIGHT.png")),
                                                dark_image=Image.open(os.path.join("imgs/generallogoDARK.png")), size=(50, 50))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="", compound="right",
                                                             font=("Watchword Bold Demo", 14))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.navigation_frame_button = customtkinter.CTkButton(
            self.navigation_frame, text="panthium <3", command=discord, fg_color='gray17', hover_color='gray17', font=("Watchword Bold Demo", 15), text_color='gray99', width=1)
        self.navigation_frame_button.grid(row=0, column=0, padx=20, pady=20)

        self.Global_Move_Button = customtkinter.CTkSwitch(
            self.navigation_frame, text="", command=move_toggle)
        self.Global_Move_Button.place(x=20, y=428)

        self.force_quit = customtkinter.CTkButton(
            self.navigation_frame, text="Force Quit", command=force_quit, font=("Watchword Bold Demo", 14))
        self.force_quit.place(x=20, y=459)

        # create all the tabs
        self.aim_tab = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Aimbot",
                                               fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                               image=self.aim_image, anchor="w", command=self.aim_tab_event, font=("Watchword Bold Demo", 13))

        self.aim_tab.grid(row=1, column=0, sticky="ew")

        self.aim_misc_tab = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Aim Misc         ",
                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    image=self.aim_misc_image, anchor="w", command=self.aim_misc_tab_event, font=("Watchword Bold Demo", 13))

        self.aim_misc_tab.grid(row=2, column=0, sticky="ew")

        self.visuals_tab = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, width=190, border_spacing=10, text="Visuals",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.visuals_image, anchor="w", command=self.visuals_tab_event, font=("Watchword Bold Demo", 13))

        self.visuals_tab.grid(row=3, column=0)

        self.gen_tab = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, width=190, border_spacing=10, text="General",
                                               fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                               image=self.gen_image, anchor="w", command=self.gen_tab_event, font=("Watchword Bold Demo", 13))

        self.gen_tab.place(x=0, y=290)

        # add buttons below the tabs

        # create home frame
        self.aim_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.aim_frame.grid_columnconfigure(0, weight=1)

        # create all the buttons in the aimbot tab
        self.Aimbot_Enabled = customtkinter.CTkSwitch(self.aim_frame, text="Enable Aimbot", font=(
            "Watchword Bold Demo", 14), command=Aim_On)
        self.Aimbot_Enabled.place(x=20, y=20)

        self.FOV_Slider = customtkinter.CTkSlider(
            self.aim_frame, from_=30, to=300, command=FOV_val, state="disabled")
        self.FOV_Slider.place(x=15, y=65)

        self.FOV_Title = customtkinter.CTkLabel(
            self.aim_frame, text="FOV - 165 x 165px", font=("Watchword Bold Demo", 14), state="disabled")
        self.FOV_Title.place(x=225, y=58)

        self.Smoothing_Slider = customtkinter.CTkSlider(
            self.aim_frame, from_=1, to=100, command=Smooth_val, state="disabled")
        self.Smoothing_Slider.place(x=15, y=100)

        self.Smoothing_Title = customtkinter.CTkLabel(
            self.aim_frame, text="Smoothing - 50%", font=("Watchword Bold Demo", 14,), state="disabled")
        self.Smoothing_Title.place(x=225, y=93)

        self.Aimbot_Key = customtkinter.CTkOptionMenu(self.aim_frame, values=[
                                                      "Left Mouse", "Right Mouse", "Mouse 4", "Mouse 5"], state="disabled", font=("Watchword Bold Demo", 12))
        self.Aimbot_Key.place(x=20, y=133)

        self.Threshhold_Slider = customtkinter.CTkSlider(
            self.aim_frame, from_=0, to=10, command=Threshhold_val, state="disabled")
        self.Threshhold_Slider.place(x=15, y=175)
        self.Threshhold_Slider.set(0)

        self.Threshhold_Title = customtkinter.CTkLabel(
            self.aim_frame, text="Aim Threshhold - 0", font=("Watchword Bold Demo", 14), state="disabled")
        self.Threshhold_Title.place(x=225, y=167)

        self.Aimbone = customtkinter.CTkOptionMenu(self.aim_frame, values=[
                                                   "Head", "Neck", "Body"], state="disabled", font=("Watchword Bold Demo", 12))
        self.Aimbone.place(x=20, y=205)

        self.alt_aimbone = customtkinter.CTkSwitch(self.aim_frame, text="Alternate Aimbone", font=(
            "Watchword Bold Demo", 12), state="disabled", command=alt_aimbone_enable)
        self.alt_aimbone.place(x=20, y=245)

        self.alt_aimbone_select = customtkinter.CTkOptionMenu(self.aim_frame, values=[
                                                              "Head", "Neck", "Body"], state="disabled", font=("Watchword Bold Demo", 12), width=100)
        self.alt_aimbone_select.place(x=20, y=280)

        self.Alt_Aimbot_Key = customtkinter.CTkOptionMenu(self.aim_frame, values=[
                                                          "Left Mouse", "Right Mouse", "Mouse 4", "Mouse 5"], state="disabled", font=("Watchword Bold Demo", 12), width=100)
        self.Alt_Aimbot_Key.place(x=130, y=280)

        self.sensitivity_slider = customtkinter.CTkSlider(
            self.aim_frame, from_=1, to=50, command=sensitivity_val, state="disabled")
        
        self.sensitivity_slider.place(x=15, y=325)

        self.sensitivity_title = customtkinter.CTkLabel(
            self.aim_frame, text="Ingame Sensitivity - 25%", font=("Watchword Bold Demo", 14), state="disabled",)
        
        self.sensitivity_title.place(x=225, y=318)

        # define the aim misc frame
        self.aim_misc_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")

        # create all the buttons for the triggerbot
        self.Triggerbot_enabled = customtkinter.CTkSwitch(self.aim_misc_frame, text="Enable Triggerbot", font=(
            "Watchword Bold Demo", 14), command=Trigger_On)
        self.Triggerbot_enabled.place(x=20, y=20)

        self.triggerbot_key = customtkinter.CTkOptionMenu(self.aim_misc_frame, values=[
                                                          "Left Mouse", "Right Mouse", "Mouse 4", "Mouse 5"], state="disabled", font=("Watchword Bold Demo", 12))
        self.triggerbot_key.place(x=20, y=57)

        self.Trigger_type = customtkinter.CTkOptionMenu(self.aim_misc_frame, values=[
                                                        "Normal", "Hanzo", "Sojurn"], state="disabled", font=("Watchword Bold Demo", 12))
        self.Trigger_type.place(x=20, y=92)

        self.Accelerate = customtkinter.CTkSwitch(self.aim_misc_frame, text="Distance based Acceleration", font=(
            "Watchword Bold Demo", 12), state="disabled")
        self.Accelerate.place(x=20, y=150)

        # define the visuals frame
        self.visuals_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")

        # create all the butons inside the visuals frame

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.visuals_frame, values=[
                                                                "Dark", "Light"], command=self.change_appearance_mode_event, font=("Watchword Bold Demo", 12))
        self.appearance_mode_menu.place(x=20, y=20)

        # define the general frame
        self.general_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")

        self.BhopToggle = customtkinter.CTkSwitch(self.general_frame, text="Bhop", font=(
            "Watchword Bold Demo", 14), state="disabled")
        self.BhopToggle.place(x=20, y=135)

        self.InstalockToggle = customtkinter.CTkSwitch(self.general_frame, text="Instalocker", font=(
            "Watchword Bold Demo", 14), command=Instalock_On)
        self.InstalockToggle.place(x=20, y=20)

        self.InstalockChoose = customtkinter.CTkOptionMenu(self.general_frame, values=["Dva", "Doom", "Junker queen", "Orisa", "Remattra", "Rein", "Hog", "Sigma", "Winston", "Ball", "Zarya", "Ashe", "Bastion", "Cassidy", "Echo", "Genji", "Hanzo",
                                                           "Junkrat", "Mei", "Pharah", "Reaper", "Sojurn", "Soldier", "Sombra", "Symmetra", "Torb", "Tracer", "Widow", "Ana", "Baptiste", "Brigitte", "Kiriko", "Lucio", "Mercy", "Moira", "Zenyatta"], font=("Watchword Bold Demo", 12), state="disabled")
        self.InstalockChoose.place(x=20, y=50)

        self.InstalockApply = customtkinter.CTkButton(self.general_frame, text="Apply", font=(
            "Watchword Bold Demo", 12), state="disabled", command=Instalock_Apply)
        self.InstalockApply.place(x=20, y=87)

        # create apply buttons

        self.apply_aimbot = customtkinter.CTkButton(self.aim_frame, text="Apply", width=75, font=(
            "Watchword Bold Demo", 12), command=apply_aim)
        self.apply_aimbot.place(x=325, y=465)

        self.apply_misc = customtkinter.CTkButton(self.aim_misc_frame, text="Apply", width=75, font=(
            "Watchword Bold Demo", 12), command=apply_aim)
        self.apply_misc.place(x=325, y=465)

        self.apply_visual = customtkinter.CTkButton(self.visuals_frame, text="Apply", width=75, font=(
            "Watchword Bold Demo", 12), command=apply_aim)
        self.apply_visual.place(x=325, y=465)

        self.apply_gen = customtkinter.CTkButton(self.general_frame, text="Apply", width=75, font=(
            "Watchword Bold Demo", 12), command=apply_aim)
        self.apply_gen.place(x=325, y=465)

        self.select_frame_by_name("Aimbot")

    # create the function to change tabs

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.aim_tab.configure(fg_color=("gray75", "gray25")
                               if name == "Aimbot" else "transparent")
        self.aim_misc_tab.configure(fg_color=(
            "gray75", "gray25") if name == "Triggerbot         " else "transparent")
        self.visuals_tab.configure(
            fg_color=("gray75", "gray25") if name == "Visuals" else "transparent")
        self.gen_tab.configure(fg_color=("gray75", "gray25")
                               if name == "General" else "transparent")

        # show selected frame
        if name == "Aimbot":
            self.aim_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.aim_frame.grid_forget()
        if name == "Triggerbot         ":
            self.aim_misc_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.aim_misc_frame.grid_forget()
        if name == "Visuals":
            self.visuals_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.visuals_frame.grid_forget()
        if name == "General":
            self.general_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.general_frame.grid_forget()

    def aim_tab_event(self):
        self.select_frame_by_name("Aimbot")

    def aim_misc_tab_event(self):
        self.select_frame_by_name("Triggerbot         ")

    def visuals_tab_event(self):
        self.select_frame_by_name("Visuals")

    def gen_tab_event(self):
        self.select_frame_by_name("General")

    def apply():
        print("apply")

    def change_appearance_mode_event(self, new_appearance_mode):
        if new_appearance_mode == 'Dark':
            self.navigation_frame_button.configure(
                fg_color='gray17', hover_color='gray17', text_color='gray99')
        else:
            self.navigation_frame_button.configure(
                fg_color='gray85', hover_color='gray85', text_color='gray1')
        customtkinter.set_appearance_mode(new_appearance_mode)



# keycheck()

def main_func():
    while True:
        app = App()
        app.mainloop()


if __name__ == '__main__':

    multiprocessing.freeze_support()

    p1 = multiprocessing.Process(target=main_func)
    p1.start()
    p1.join()
    print("UI RUNNING")

# (['python', 'utils/aimbot.py',
# str(int(self.Smoothing_Slider.get())),
# str(int(self.FOV_Slider.get())),
# keys[self.Aimbot_Key.get()],
# self.Aimbone.get(),
# str(int(self.Threshhold_Slider.get())),
# str(self.BhopToggle.get()),
# str(self.alt_aimbone.get()),
# str(self.Triggerbot_enabled.get()),
# keys[self.triggerbot_key.get()],
# str(self.alt_aimbone.get()),
# str(self.alt_aimbone_select.get()),
# str(self.DebugToggle.get()),
# str(self.Trigger_type.get()),
# str(self.Accelerate.get()),
# ])