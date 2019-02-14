from tkinter import *
import caliroots_captcha


def callback():
    get_link = product_link.get()
    get_webhook = discord_link.get()
    get_interval = monitor_rate.get()
    caliroots_captcha.inputted_link(get_link)
    caliroots_captcha.inputted_webhook(get_webhook)
    caliroots_captcha.inputted_interval(get_interval)
    caliroots_captcha.loop()


#title
gui = Tk()
gui.title("Caliroots Carter (1.0.0)")


#image
logo = PhotoImage(file = "logo.png")
l = Label(gui,image=logo)
l.pack()

#url_getter
url = Label(gui, text="Product URL:")
url.pack()

product_link = StringVar()
url = Entry(gui, textvariable=product_link)
url.pack()
url.insert(0, "https://caliroots.com/dr-martens-jadon-15265001/p/72222")


#webhook_getter
discord = Label(gui, text="Discord Webhook URL:")
discord.pack()

discord_link = StringVar()
discord = Entry(gui, textvariable=discord_link)
discord.pack()
discord.insert(0, "https://discordapp.com/api/webhooks/537906296154882048/DMVYB0MabZBJvt5w4izViERx13LL3_8DMWBfbBPA682p5pw2VdkpkqIfC1QYKJyBINPU")


#interval_getter
rate = Label(gui, text="Monitor rate in seconds:")
rate.pack()

monitor_rate = StringVar()
rate = Entry(gui,textvariable=monitor_rate)
rate.pack()
rate.insert(0, "3")

#run_button
run_button = Button(gui, text="Start Task", command=callback,padx=10,pady=5)
run_button.pack(pady=20)

ps = Label(gui, text="*Please make sure your Chrome is opened with Gmail logged in before starting.",font=("Helvetica", 10))
ps.pack()


#geo
width_of_window = 388
height_of_window = 299
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width_of_window / 2)
y_coordinate = (screen_height / 2) - (height_of_window / 2)
gui.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
gui.mainloop()
